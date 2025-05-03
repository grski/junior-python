\pagebreak

# Internet

Here we'll discuss various issues related to networks, the Internet, and everything else. Even though as a junior-python wannabe we're most concerned with Python itself and programming, we need to remember that the code we write and then run doesn't operate in a vacuum.

All our web apps, programs, etc. are run in some specific environment. This environment affects how our programs are executed and how they work. Additionally, we often need to interact with it in some way, often bidirectionally. What does this mean? Well, besides Python itself, it's worth knowing about the whole environment where it runs and so on, because otherwise, you might sometimes shoot yourself in the foot. Plus, knowledge about the environment and related things that we use directly or indirectly, often without being aware of it, meaning simply other components of the 'System' that we design, create, or maintain, are its integral part and something that affects our work and our code.

By System here, I mean some arrangement, set of elements. In IT, this is usually, for example, our web app, the servers where it runs, the client, etc.

Let's talk about this whole system and environment.

## Request Journey

Most web applications work in a client-server model. The client makes requests to the server, the server returns a response.

But how does it happen that we're able to send this request? What happens when you type `grski.pl` in the browser bar and then see my blog?

Well, the matter looks like this.

Assuming you're connected to the Internet, your request will be processed by your ISP (Internet Service Provider), which will hit something called DNS. DNS is the Domain Name Server, like a phone book that contains mappings of domains/addresses like grski.pl to locations (IP) on the network.

What does this mean? Every server has its more or less unique IP. The so-called IP address. It's like a residential address.

IP looks like this: **172.16.254.1**. It's a 32-bit number, at least in the case of IPv4 standard. Something like this is hard to remember, right? For me it is. But `grski.pl` isn't. Hence this mapping and domains came about. Domains make it easier to remember and make life easier for users.

I'll throw in an interesting fact. If IPv4 defines an IP address as a 32-bit number, then the question for you is, what problem might arise here in today's times? Well, a 32-bit number is small by today's standards. Think about how many devices are connected to the Internet, most of them have unique public addresses. Holy moly. Generally, we're approaching a point where there won't be free unique IP addresses. Sad situation.

Therefore, IPv6 was created, which solves this problem. Example of IPv6: **2001:0db8:85a3:0000:0000:8a2e:0370:7334**. Here the size is already 128 bits. 2 to the power of 128 gives a ton of options, this address space will last us for a while.

Alright, let's get back to the request though.

Currently we have: your browser (client) -> ISP -> DNS -> Server.

Then on the server there are often Load Balancers/Proxy, which are pieces of software that appropriately direct requests coming to them to matching local resources/services/APIs etc.

From LB/Proxy the request goes to the target service. Then we receive a response and done.

There might be many other services in between like cache, CDN etc., but I presented the shortened version here. And speaking of CDN...

## CDN

What is CDN and why is it important? It's actually thanks to them that we can use mobile networks without problems, pay less for Internet, it's thanks to CDNs that your funny cat video on wykop doesn't stutter, and your operator can handle the current number of clients instead of, say, half. I know, I'm exaggerating a bit, but only a little bit. So what is it?

### Introduction

First though, a handful of information to gain some perspective. We live in times where existence without the Internet is practically impossible, or at least very inconvenient. Most of today's luxuries somehow base on/use this invention. Often, however, we don't realize how huge this Internet is and how quickly it's growing, let me explain.

In 2018, we crossed another barrier - that's when Earth hit a new record of internet users - 4 billion people using the Internet, which is as much as 53% of the population. This is an amazing increase, considering that just 4 years earlier there were about 2.4 billion Internet users.

In 2016, 44 billion GB of data flew through the Internet per day. Taking into account that there were significantly fewer users then, considering users in 2018, this gives us about 51 billion GB per day. Of course, this is a heavily underestimated result, because not only are users increasing, but they're also consuming more and more data, but for the purposes of this article it's enough, as it gives us some picture. Currently it's 2022 and about 5 billion. 62.5% of the population.

The average smartphone user consumes 2.9 GB of mobile transfer during a month (data from January 2018). That's 50% more than a year earlier.. The network is growing at an alarming rate. Why alarming? Well, while for cable connection there isn't such a tragedy, because you can add a cable or two, although this is also all complicated and costly, the real problem arises with mobile data network, as it's heavily limited by physics, and considering continuous growth... Well, we have something to worry about a bit or our network might get a bit clogged.

### And Then Enters CDN, All in White

Yes. The whole situation is mitigated by CDN. What is this? These are servers that cache the most popular content on the Internet to generally offload the network, reduce loading times and prevent certain problems, improve security. These servers are scattered across the Earth in geographically strategic locations for the network.

In the network, we have content providers. This content is various, text, pictures, videos, multimedia. Content providers place them on their websites, servers and it's cool. When you want to read or watch something on the Internet, your device connects through the Internet with the content provider's server and transmits specific content to you. All cool, right? Well, no.

The problem appears when this data and users increase worldwide. The problem stems from the Internet's architecture. When you watch an episode of your favorite series, your computer doesn't connect directly with the provider's server, no. Before that happens it must go through dozens of other devices that will direct it to the right place, same with the response from that server.

Imagine you're in an office and to handle a specific matter you need signatures from ten different officials and at the end also a signature from a supervisor in America, to whom there's a long queue. It takes a lot of time, energy and so on, right? Yes. Complicated matter overall. The role of CDN is to shorten this list of needed signatures to one official who is in the local office.

So like with servers - your request instead of beating its way to a server in Asia or America and tiring one server, will first ask a local guy who is in the next city. In 99% of cases he will be enough. In the remaining 1% we'll have to drag to America, but we'll handle the matter quickly on site, because thanks to help with handling petitioners locally, Uncle Sam has less to handle, making the queue much shorter.

### Details

From the Content Provider's server to CDNs, certain data is transmitted and cached - what kind? Those that are most popular - it's very important to maintain mainly that data on CDNs that is most popular, because thanks to this CDNs take over most of the traffic, reducing network load achieving high hit rate.

It's a complicated process, because after all different content is popular in different regions, and how they will change is not trivial to predict.

The algorithms used here to predict what and where will be popular is really a very interesting matter and important - CDN space and resources are limited, so the choice of this content is difficult. An amazing example of such optimization and prediction of what will be popular right now can be observed on the example of Netflix and how they solve this.

### What is hit rate, lifetime?

I used the term hit rate earlier. This is a term that determines what percentage of user requests can be processed by CDN and only CDN, and what needs help from the Content Provider's server. Currently, some can optimize their servers so well that the hitrate to cache can be even around 99%. Amazing results.

Additionally, there's also determining the time for which once uploaded content should be available - lifetime - after its expiration the cache is 'removed' from the server and new (or still the same if they're still popular)/updated data jumps in its place. It's completely different depending on the data, region, the service provider itself.

### Is CDN one huge server?

No, it's often whole clusters of geographically distributed servers. Hundreds of thousands of machines that have a certain hierarchy and work according to it. How? More or less like this. The content provider's server is CP.

Then we have CD & LCF - that's like headquarters you could say.

Then there's CCF and under it CDPF. CCF is the local office, and CDPF is the official.

By default, when you make some request for content, it lands in CCF, CCF checks if what you need is somewhere in its resources, meaning on CDPF servers where cached content is kept. So in short it checks if what you're asking for is somewhere 'copied' on the local server.

If it's not on one, it goes to the next of the CDPFs under its control. What if it doesn't find it on any of its CDPFs? Then it reports the fact to CD & LCF, which asks the remaining CCFs in turn.

If each CCF states that this content isn't on CDPFs under their control? Then CD & LCF makes a request to the content creator's server, gets the data from there and keeps it locally. So the original server is bothered in a very small number of cases, thanks to which the server itself and its surrounding network is significantly offloaded, traffic gets scattered across local and distributed CCFs instead of being concentrated in one location.

It's partly thanks to such solutions (or similar) that GitHub with help from Akamai company, were able to handle the recent record DDOS attack directed against this popular platform, which in its peak phase reached the size of 1.35 Tbps - almost one and a half Tb per second. Amazing. This is why Wykop works somewhat. This is why Netflix doesn't clog the entire Internet.

### Summary

There are many things thanks to which our days are easier, and we don't even know it. CDNs were probably something like that for most of you. Of course there are a lot of simplifications in the text, so bear with it.

## Cache

What is cache? Cache is like a database, but with a somewhat different purpose. By default, cache keeps data for a specified amount of time, usually quite short, relative to databases which sometimes keep data permanently.

So cache is like a database with a short expiration date, in which we store remembered results of computations, those that are usually costly and only those that concern reading and not writing to the database for example.

So if we have some view/function, anything that takes an argument, in our case it will be some request, then for similar or the same ones, cache will return the result 'from memory' instead of calculating/fetching anew.

For reading:

1. https://www.techtarget.com/searchstorage/definition/cache
2. https://realpython.com/lru-cache-python/
3. https://realpython.com/python-memcache-efficient-caching/

## Cloud

AWS, Azure, GCP are cloud service providers. What does this mean? What is the cloud? Cloud is simply like a server room, but at someone else's house. Someone else worries about certain things.

For an appropriate fee, cloud providers handle certain things for us, provide additional services, take care of most things.

These are often such conveniences where in exchange for some cost and the fact that cloud providers sometimes decide for us on certain issues, we shift the burden of taking care of some matters to an external company. In a nutshell.

AWS is the cloud from Amazon, Azure from Microsoft, and GCP from Google.

Which is better? The one your target employer uses. Basically though, they are similar to each other, only some service names change. Additionally however, one cloud will have a better toolset for specific tasks, another for others.

IMO if it's about corporations then probably mostly Azure/AWS.

Startups mainly AWS.

GCP is a mix.

Source: institute of data from ass.

I personally most often encountered AWS, but that's just me. I recommend getting familiar and playing a bit with setting up different services in the cloud on your own. Each of them offers programs where for registering we'll receive some amount of cash to burn on our games. Use it, because it's worth it. It will add independence to you and +10 to fame if you learn basic things from DevOps. And what is this whole devops thing? Link number 4. In short, it's a guy from infrastructure and handling servers, meaning the place where our applications are run.

Anyway.

For reading:

1. https://azure.microsoft.com/pl-pl/resources/cloud-computing-dictionary/what-is-the-cloud/
2. https://experience.dropbox.com/pl-pl/resources/what-is-the-cloud
3. https://devopsiarz.pl/kurs-ansible/  <- strongly additional. Ansible is software for automating certain tasks, so you don't have to click manually.
4. https://devopsiarz.pl/devops/kto-to-jest-devops-engineer/
5. https://en.wikipedia.org/wiki/Infrastructure_as_code
6. https://12factor.net/

## Docker

What is this whole Docker thing? They write about it everywhere.

Well, docker is a tool for building and running containers, containerization. Like a virtual machine simulating a computer in a computer. The main difference lies however in that containers are muuuch more efficient when it comes to resources.

VMs set up the entire system and emulate everything from scratch. Docker uses ready components of your system which makes it much less resource-hungry.

Thanks to containers we can download ready 'images' that contain everything the application needs to run as well as the application itself.

Imagine that you have to manually install all dependencies, packages etc.

Now imagine the same on 50 servers, because you need to scale the application. Docker makes this easier for us. Once built complete image only requires running.

Currently it's standard that applications are containerized.

Containerizing applications with Docker has many advantages:

1. Reliability: Docker containers allow running applications independently of the environment, which means that the application works the same on different operating systems and infrastructures.
2. Flexibility: Docker containers are easy to move between different environments, which means you can easily extend the application to new platforms or move it to the cloud.
3. Resource savings: Docker containers are lighter than traditional virtual machines, which means you can run more applications on the same hardware.
4. Speed: Docker containers are faster than virtual machines because they don't require installing the operating system and all needed libraries.
5. Ease of use: Docker provides a tool for creating, sharing and running containers, which makes it easier to manage applications and their dependencies.

Generally speaking, containerizing applications with Docker helps increase reliability, flexibility, efficiency and ease of managing applications, which is particularly useful in a cloud environment.

For reading:

1. https://www.czarnaowca.it/2022/01/docker-tutorial-1-co-to-jest-docker-i-do-czego-jest-nam-potrzeby/
2. https://sii.pl/blog/docker-dla-programistow-co-to-jest/

## Docker-compose

In telegraphic shortcut Docker Compose is like scripts on steroids that allow us to more easily manage several containers. Imagine that we have a database, broker and worker in docker in one application. Potentially a million Dockerfile files, lots of commands to type etc. Mess overall.

Here comes to help the docker-compose file and tool of the same name. It allows for easy management of all application containers as one complete system, instead of managing each container separately. Docker Compose also enables easy resolution of dependencies between containers, such as network connections and required data files.

## Docker Hub

Docker Hub is a public platform for storing and sharing Docker images. It allows for easy sharing of images with other people and using ready-to-run images. Docker Hub is also integrated with the Docker Compose tool, which enables easy running of multiple containers simultaneously.

\pagebreak