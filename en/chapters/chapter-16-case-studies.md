\pagebreak

# Case Studies of Various Applications

Here we'll discuss and analyze different implementation cases, talk about decisions and System Design, why something is done one way and not another, etc.

## URL Shortener

The task was to design a URL shortening system, assuming we would handle quite significant traffic. I won't describe it step by step, instead I'll include here the notes from the conversation, a brief description, and the questions I asked.

1. Do we include authentication, or will it be handled outside the service? What's the business need?
   `What do you think?`
   For GET requests decoding shortened URLs, auth isn't needed. For creation, it might be useful to be able to assign a user to the link they shortened. This would allow for future editing or management of shortened URLs.
   `So we'll include it`
   In this case, I would use JWT auth, simply due to preferences plus the possibility of later pushing auth to the Load Balancer level when we scale.
2. What will be the write-to-read ratio? That is, how many GETs per each created URL.
   `Let's assume many many reads per one write.`
   Then a regular database like Postgres. If needed, we can add batch creation of reads with intermediate cache storage and scale the database first vertically, then create a cluster with a write-only master and several read-only replicas/slaves.

```
/ - base url for our api
/v1 - base url for v1 api
POST /v1/registration
POST /v1/login -> return a JWT token
POST /v1/short-urls
GET /v1/short-urls/{unique-id}

Table: users
Email: email | varchar
Password: --- (hashed)

Table: urls
id: integer | pk
unique_id: url | varchar | unique
original_url: url | varchar
created_at: datetime

POST[create] /short-urls 
Request: {"url": https://google.com} -> 
Response: {"shortened_url": "{api_entrypoint}/short-urls/{unique-id}"}
1. authenticate and authorize the user
2. take the payload and validate it ->
-> it has required fields + required fields are of proper type
3. save it to the database after generating a random unique id for the url
id in this case might be eg. couple char long alphanumeric value or a slug
4. put in cache (up for debate)
5. return the response with shortened url

GET[detail] /short-urls/{unique-id} -> {"url": "https://google.com"}
1. get the unique-id from the url
2. check if it's present in the cache
3. if it is, just return the value from cache
4. if it's not, then query the database for that given unique id
5. if not found, return 404
6. if found return the object from the db and also add it to the cache with a proper lifetime

FastAPI - async framework at the front
Cache will improve the perf drastically
As it'll be mainly reads and waiting for the network calls, cache will
help a lot here.

Route53 <- domain parked
Load Balancer <- from AWS
Microservice <- 1. EC2 that has scaling enabled or managed k8s cluster 
-> or AWS provided container runtime service
Microservice cache <- redis
Persistent storage <- RDS with Postgres
```

## How One Digit Can Break an Application - A Case Study

Recently at work, I came across what I consider a quite interesting case to investigate. We received a report from a client that files for selected resources stopped working - clients couldn't access thumbnails, information, sometimes there were problems with downloading itself, and so on, generally a major screw-up that needed to be fixed ASAP.

Well, I sat down to it then.

My first suspicion fell on myself. Why? Well, a few months ago, I clearly remember fiddling with something about how files are returned and so on, in any case, I was practically certain it was my doing.

I looked a bit like Nawałka after the World Cup.

### Phew
Nevertheless, after analyzing the reports, it turned out that the problem started appearing even before I modified anything in this particular module, so I had to exclude the possibility that it was my doing.

Hmm, okay, what now. Well, let's move on, maybe something interesting will come up.

Looking through the code, I didn't find anything interesting, no changes, nothing. So what could have caused the problem to appear suddenly?

Well, to find the answer to this question, I had to look at how files are served in the client's application.

It turns out they are hosted on external servers, depending on the region, which process everything, handle authentication and so on, and then return the requested content.

Okay. Time to look at this process more closely.

### File Path
The first common feature that emerged among all reported problematic files was that they came from one area - meaning they were all served by one server. Good, that's some clue.

I tried then to recreate the path that a typical user and their request takes, and check the application's behavior during such a path. I dug through the source code, found the code responsible for handling the display and delivery of content links to users, and generated a regular URL to a given resource, and indeed - it doesn't display at all, receiving some error. But wait. Let's look at the request itself, what's happening there.

No error appears in the response, so the server doesn't see any problem and returns a normal response. Hmmm, interesting...

### What Turns Out?
It turns out that although the request we're making should clearly return us a response with video files, for some reason, instead of returning what it should, the response has the type... of an image.

Let's check what's in the response body. First the size - compared to the original files it roughly matches. And what do the headers say?

After a small analysis, it turns out that although the response type contains an image, the server in the response body serves nothing else but the given video file, which if saved, is a correct movie, hmm interesting. And now we know why the content isn't displayed at all - how is the browser/application supposed to display a movie when the response tells it to display this content as an image?

### Let's Look in the Database
I decided then to browse through the database in search of other video files, to see what mimetype the server would generate for them.

Well, my search quickly showed me that the server has no problem identifying files of type .avi or .mpa as video and returns them with the correct mimetype, enabling the browser to behave properly. Why this behavior?

### Format?

Could it be the format's fault? Because .avi works, .mpa too, but it turns out that certain .mp4 files don't.

Not at all, as I managed to find working .mp4 files - that's not it.

And how is it on other servers? On others everything works - no .mp4 file that wouldn't work for unknown reasons. Even more interesting.

How the file looks on disk
I remembered a bit about how files are generally saved on disk, how you can recognize that a given file is of a particular type - certainly not by extension, and I thought that this might be it - something might be wrong in the file headers and that's why the server doesn't correctly recognize the type. Maybe something goes wrong during saving. I compared then two files in the same format using HxD - one working, the other not.

Unfortunately, despite small obvious differences in the hex code, where it should be the same, everything matched, even though at first it seemed I found an error in the file structure.

Damn.

I came up with another idea then - I'll check it with another program, mediainfo, let's see if it correctly decodes the information about the file format and so on.

And here again surprise - mediainfo had no problem reading the file correctly, all information about it. Why then, if other programs correctly recognize files as video, does the server not do it? I don't know, but nothing, I'll try on others, maybe I'll get lucky here.

And I started browsing and browsing. Nothing. Completely nothing. Suddenly...

### Eureka
...I noticed a certain fact. It turned out that every working, correctly recognized file was encoded using a certain library in version let's say 2.11.2 or older, while all those files that were encoded with this library in any later version were incorrectly recognized by the server. And here everything became clear.

I looked at the library's website and what turned out? Around the same time when the problem started appearing, there was a release of a new version of the library. This confirmed my belief that someone somewhere updated one library on just one server, not taking into account the fact that the code of the application running on the server uses dependencies in a certain specific version and older versions, and is adapted to them, which is why files encoded with newer versions are not correctly detected, and every file that lands on the server, before being served to users, is processed using the currently installed library.

### Summary
Even though there was no actual programming here, I must admit I had great fun while performing this task. A bit like a detective uncovering the secrets of a great crime.

It also showed me that general knowledge, about which people often say 'why do I need this', sometimes comes in handy.

To sum up, sometimes it's enough to change one digit from 2.11.2 to 2.11.3 for something to suddenly stop working somewhere, and a developer's work isn't always just churning out new landing pages.

\pagebreak 