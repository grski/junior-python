\pagebreak

# Case Studies of Different Applications

Here we'll discuss and analyze various specific implementation cases, talk about decisions and System Design, why something is done one way and not another, etc.

## URL Shortener

The task was to design a URL shortening system, assuming we'll be handling fairly heavy traffic. Instead of writing step by step, I'm including my notes from the conversation here, a brief description, and the questions I asked.

1. Do we consider authentication, or will it be handled outside the service? What's the business need?
   `What do you think?`
   For GETs decoding shortened URLs, auth isn't needed. For creation, it might be useful to assign a user to the link they shortened. This will allow editing in the future or managing shortened URLs.
   `So we'll include it`
   In this case, I'd use JWT auth, simply due to preference plus the possibility of later pushing auth to the Load Balancer level when we scale.
2. What will be the ratio of writes to reads? How many GETs per created URL.
   `Let's assume many, many reads per one write.`
   So a regular database like Postgres. If needed, we can add batch read creation with intermediate cache storage and scale the database first vertically, then create a cluster with a write-only master and several read-only replicas/slaves.

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
-> it has required fields + required filds are of proper type
3. save it to the database after generating a random unique id for the url
id in this case might be eg. couple char long alphanumeric value or a slug
4. put in cache (up for debate)
5. return the response with shorten url

GET[detail] /short-urls/{unique-id} -> {"url": "https://google.com"}
1. get the unique-id from the url
2. check if it's present in the cache
3. if it is, just return the value from cache
4. if its not, then query the database for that qiven unique id
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
Microsver cache <- redis
Persistent storage <- RDS with Postgres
```



## How One Digit Can Break an Application - A Case Study

Recently at work, I came across what I consider a fairly interesting case to investigate. We received a report from a client that files had stopped working for selected resources - clients couldn't access thumbnails, information, sometimes there were problems with downloading itself, and so on. Overall, a major fuckup, needs to be fixed ASAP.

Well, I sat down to work on it.

My first suspicion fell on myself. Why? Well, a few months ago, I clearly remember tinkering with how files are returned and so on. In any case, I was practically certain it was my doing.

### Phew

Nevertheless, after analyzing the reports, it turned out that the problem started appearing even before I modified anything in this specific module, so I had to rule out the possibility that it was my fault.

Hmm, okay, what now. Well, nothing, let's move on, maybe something interesting will turn up.

Going through the code, I didn't find anything interesting, no changes, nothing. So what could have caused the problem to suddenly appear?

Well, to find the answer to that question, I had to look at how files are served in the client's application.

They're hosted on external servers, depending on the region, which process everything, handle authentication, and so on, then return the requested content.

Okay. Time to take a closer look at this process.

### The File Path
The first common feature that emerged among all reported problematic files was that they came from one area - meaning they were all served by one server. Good, that's already a clue.

So I tried to recreate the path that a typical user and their request takes, and check the application's behavior during that path. I dug through the source code, found the code responsible for handling the display and delivery of content links to users, and generated a regular URL to the resource, and indeed - it doesn't display at all, I get some error. But wait. Let's look at the request itself, what's happening there.

No error appears in the response, so the server sees no problem and returns a normal response. Hmmm, interesting...

### What Turns Out?
It turns out that despite the fact that the request we're making should obviously return a response with video files, for some reason, instead of returning what it should, the response has the type of... an image.

Let's check what's in the response body. First the size - compared to the original files, it roughly matches. And what do the headers say?

After a little analysis, it turns out that despite the fact that the response type contains an image, the server is serving nothing other than the video file in the response body, which if saved, is a valid video file. Hm, interesting. And now we know why the content isn't displayed at all - how is the browser/application supposed to display a video when the response tells it to display this content as an image?

### Let's Look at the Database
So I decided to browse the database looking for other video files to see what mimetype the server would generate for them.

Well, my search quickly showed me that the server has no problem identifying .avi or .mpa files as video and returns them with the correct mimetype, allowing the browser to behave properly. Where does this behavior come from?

### Format?

Could it be the format's fault? Because .avi works, .mpa too, but it turns out that certain .mp4 files don't.

Not at all, because I managed to find working .mp4 files - that's not it.

And how is it on other servers? Everything's fine on others - no .mp4 file that doesn't work for unknown reasons. Even more interesting.

### How the File Looks on Disk
However, I remembered a bit about how files are actually stored on disk, how you can tell that a given file is of a particular type - definitely not by the extension. I thought that maybe this could be it - something might be wrong in the file headers, and that's why the server doesn't correctly recognize the type. Maybe something goes wrong during saving. So I compared two files in the same format using HxD - one working, one not.

Unfortunately, despite minor obvious differences in the hex code, where it should be the same, everything matched, even though at first I thought I had found an error in the file structure.

Damn.

So I came up with another idea - I'll check it with another program, mediainfo, let's see if it correctly decodes information about the file format and so on.

And here again surprise - mediainfo read the file correctly without any problem, all information about it. Why then, since other programs correctly recognize files as video, doesn't the server do this? I don't know, but anyway, I'll try on others, maybe I'll get lucky there.

And I started browsing and browsing. Nothing. Absolutely nothing. Suddenly...

### Eureka
...I noticed a certain fact. Every working, correctly recognized file was encoded using a certain library in version, let's say 2.11.2 or older, while all those files that were encoded with this library in any later version were incorrectly recognized by the server. And here everything became clear.

I looked at this library's page and what turned out? Around the same time when the problem started appearing, a new version of the library was released. This confirmed my belief that someone somewhere updated one library on only one server, not taking into account the fact that the application code running on the server uses dependencies in a specific version and older versions, and is adapted to them, which is why files encoded with newer versions aren't detected correctly. Every file that lands on the server, before being served to users, is processed using the currently installed library.

### Summary
Even though there was virtually no actual programming here, I admit I had a great time doing this task. A bit like a detective uncovering the secrets of a great crime.

It also showed me that general knowledge, which people often say 'why do I need this', sometimes comes in handy.

In summary, sometimes it's enough to change one digit from 2.11.2 to 2.11.3, and suddenly something somewhere stops working. A developer's job isn't always just churning out new landing pages.

\pagebreak
