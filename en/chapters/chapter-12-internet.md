\pagebreak

# Internet

Here we'll touch on various issues related to networks, the Internet, and everything else. Even though as a junior-python wannabe we're most concerned with Python itself and programming, remember that the code we write and then run doesn't operate in some vacuum.

All our web apps, programs, etc. are run in some specific environment. This environment affects the execution of our programs and how they work. Additionally, we often have to interact with it in some way, often bidirectionally. What does this mean? Well, in addition to Python itself, you should also know the whole ecosystem where things run, because otherwise you can sometimes shoot yourself in the foot. Knowledge about the environment and related things, which we directly or indirectly use, often without realizing it - i.e., other components of the `System` we're designing, creating, or maintaining - are an integral part of it and something that affects our work and our code.

By System, I mean some arrangement, set of elements. In IT, this is usually, for example, our web app, servers where it runs, client, etc.

So let's talk about this whole system and environment.

## The Request Journey

Most web applications work on the client-server model. The client makes requests to the server, the server returns a response.

But how does it happen that we're able to send this request? What happens when you type `example.com` in your browser's address bar and then see a website?

Well, here's how it works.

Assuming you're connected to the Internet, your request will be processed by your ISP (Internet Service Provider), which will reach out to something called DNS. DNS is a Domain Name Server, like a phone book that contains mappings of domains/addresses like example.com to locations (IPs) on the network.

What does this mean? Every server has its more or less unique IP. The so-called IP address. It's like a home address.

An IP looks like this: **172.16.254.1**. It's a 32-bit number, at least in the case of the IPv4 standard. That's hard to remember, right? It is for me. But `example.com` is not. That's why this mapping and domains came about. Domains make it easier to remember and make life easier for users.

I'll also throw in a fun fact. If IPv4 defines an IP address as a 32-bit number, then a question for you: what problem might arise here in today's world? Well, a 32-bit number is small by today's standards. Think about how many devices are connected to the Internet, most of them have unique public addresses. Good grief. Generally, we're approaching a point where there won't be free unique IP addresses. Unfortunate.

So IPv6 was created, which solves this problem. IPv6 example: **2001:0db8:85a3:0000:0000:8a2e:0370:7334**. Here the size is already 128 bits. 2 to the power of 128 gives us a ton of options, this address space will last us for a while.

Alright, let's get back to the request.

We currently have: your browser (client) -> ISP -> DNS -> Server.

Next, servers often have Load Balancers/Proxies, which are pieces of software that appropriately direct requests/queries arriving at them to matching local resources/services/APIs, etc.

From the LB/Proxy, the request goes to the target service. Then we receive a response and we're done.

There may be many other services in between like cache, CDN, etc., but I've presented a shortened version here. And speaking of CDN...

## CDN

What is a CDN and why is it important? It's basically thanks to them that we can use mobile networks without problems, pay less for Internet, thanks to CDNs your funny cat video doesn't stutter, and your provider can serve the current number of customers instead of, say, half. I know, I'm exaggerating a bit, but only a little. So what is it?

### Introduction

But first, a handful of information to gain some perspective. We live in times where existence without the Internet is practically impossible, and certainly very inconvenient. Most of today's luxuries somehow rely on/use this invention. However, we often don't realize how huge the Internet is and how fast it's developing, let me explain.

In 2018 we crossed another barrier - that's when Earth broke a new record for Internet users - 4 billion people using the Internet, which is as much as 53% of the population. This is incredible growth, considering that just 4 years earlier there were about 2.4 billion Internet users.

In 2016, 44 billion GB of data flew through the Internet daily. Given that there were significantly fewer users then, accounting for users in 2018, that gives us about 51 billion GB daily. Of course, this is a highly underestimated result, because not only are there more users, but they also consume more and more data, but for the purposes of this article it's enough, as it gives us some picture. Now in 2022 we have about 5 billion. 62.5% of the population.

The average smartphone user uses 2.9 GB of mobile data per month (January 2018 data). That's 50% more than the year before. The network is developing at an alarming rate. Why alarming? Well, when it comes to wired connections, it's not that tragic, because you can add a cable or two, although that's also all complicated and expensive, the real problem arises with mobile data networks, as they are severely limited by physics, and considering the continuous growth... Well, we have something to worry about or our network will get a bit congested.

### And Then CDN Enters, All in White

Yes. The whole situation is mitigated by CDN. What is it? These are servers that cache the most popular content on the Internet to generally relieve the network, shorten loading times, and prevent certain problems, improve security. These servers are scattered around the Earth in geographically strategic locations for the network.

On the network, we have content providers. This content varies - text, images, videos, multimedia. Content providers place them on their pages, servers, and it's fine. When you want to read or watch something on the Internet, your device connects through the Internet to the content provider's server and transmits specific content to you. All good, right? Not really.

The problem arises when this data and users increase worldwide. The problem stems from the Internet's architecture. When you watch an episode of your favorite series, your computer doesn't connect directly to the provider's server, no. Before that happens, it has to go through dozens of other devices that will direct it to the right place, the same goes for the response from that server.

Imagine you're at a government office and to handle a specific matter you need signatures from ten different officials and finally a signature from the supervisor in America, to whom there's a long queue. It takes a lot of time, energy, and so on, right? Yes. Complicated matter overall. The CDN's role is to shorten this list of required signatures to one official who happens to be at the local office.

Just like with servers - your request, instead of trudging to a server in Asia or America and bothering one server, will first ask the local guy who's in the next city. In 99% of cases, he's enough. In the remaining 1%, you'll have to trek to America, but once there we'll handle things quickly, because thanks to help with handling clients locally, Uncle Sam has fewer to serve, so the queue is much smaller.

### Details

From the Content Provider's server to CDNs, certain data is transmitted and cached - what kind? The ones that are most popular - it's very important to keep mainly the data that is most popular on CDNs, because this way CDNs take over most of the traffic, reducing network load and achieving a high hit rate.

This is a complex process because, after all, different content is popular in different regions, and predicting how they'll change is not trivial.

The algorithms used here to predict what will be popular where are really interesting and important - CDN space and resources are limited, so choosing this content is difficult. An amazing example of such optimization and predicting what will be popular can be observed with Netflix and how they solve this.

### What is Hit Rate, Lifetime?

I used the term hit rate earlier. It's a term that describes what percentage of user requests can be processed by CDN and only CDN, and what percentage needs help from the Content Provider's server. Currently, some can optimize their servers so that the cache hit rate is even around 99%. Amazing results.

There's also the determination of how long once uploaded content should be available - lifetime - after it expires, the cache is 'deleted' from the server and new (or still the same, if they're still popular)/updated data takes its place. It's completely different depending on the data, region, the service provider itself.

### Is CDN One Huge Server?

No, it's often entire clusters of geographically distributed servers. Hundreds of thousands of machines that have a certain hierarchy and act according to it. How? Roughly like this. The content provider's server is CP.

Then we have CD & LCF - you could say it's like a headquarters.

Then there's CCF and under it CDPF. CCF is the local office, and CDPF is the official.

By default, when you make a request for certain content, it lands in the CCF, CCF checks whether what you need is somewhere in its resources, i.e., on the CDPF servers where cached content is kept. In short, it checks if what you're asking for is 'copied' somewhere on the local server.

If it's not on one, it goes to the next CDPF under its control. What if it doesn't find it on any of its CDPFs? Then it reports this to CD & LCF, which asks the remaining CCFs one by one.

If every CCF determines that this content is not on the CDPFs under their control? Then CD & LCF makes a request to the content creator's server, downloads the data from there and saves it locally. So the original server is bothered in a very small number of cases, making the server itself and its surrounding network significantly relieved, traffic is spread across local and distributed CCFs instead of being concentrated in one location.

It's partly thanks to such solutions (or similar) that GitHub, with the help of Akamai, was able to cope with the recent record DDOS attack directed against this popular platform, which at its peak reached 1.35 Tbps - almost one and a half Tb per second. Amazing. That's why services can handle the load. Thanks to this, Netflix doesn't clog the entire Internet.

### Summary

There are many things that make our days easier, and we don't even know it. CDNs were probably something like that for most of you. Of course, there are many simplifications in the text, so bear with it.

## Cache

What is cache? Cache is like a database, but with a somewhat different purpose. By design, cache stores data for a specified amount of time, usually quite short, relative to databases, which sometimes store data permanently.

Cache is therefore like a database with a short expiration date, in which we store memorized results of computations, typically those that are expensive and only those that concern reading rather than writing to the database, for example.

So if we have some view/function, whatever, that takes an argument - in our case it will be some request - then for similar or identical ones, cache will return the result 'from memory' instead of calculating/fetching again.

Further reading:

1. https://www.techtarget.com/searchstorage/definition/cache
2. https://realpython.com/lru-cache-python/
3. https://realpython.com/python-memcache-efficient-caching/



## Cloud

AWS, Azure, GCP are cloud service providers. What does this mean? What is the cloud? The cloud is simply like a server room, but at someone else's place. Someone else worries about certain things.

For an appropriate fee, cloud providers handle certain things for us, provide additional services, take care of most things.

It's often conveniences where, in exchange for a certain cost and the fact that cloud providers sometimes make decisions for us on certain matters, we shift the burden of care for some things to an external company. In short.

AWS is Amazon's cloud, Azure is Microsoft's, and GCP is Google's.

Which one is better? The one your target employer uses. At the core, they're quite similar to each other, only the names of some services change. Additionally, one cloud will have a better toolset for specific tasks, another for others.

In my opinion, if we're talking about enterprise, it's probably mostly Azure/AWS.

Startups are mainly AWS.

GCP is a mix.

Source: pulled from thin air.

I personally encountered AWS most often, but that's just me. I recommend getting familiar with and playing around with setting up various services in the cloud yourself. Each of them offers programs where by registering you'll receive a certain amount of credits to spend on your experiments. Take advantage of it, because it's worth it. It will add independence and +10 to your reputation if you learn the basics of DevOps. And what is this whole DevOps thing? Link number 4. In short, it's a person responsible for infrastructure and managing servers, i.e., the place where our applications are run.

Anyway.

Further reading:

1. https://aws.amazon.com/what-is-cloud-computing/
2. https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-the-cloud/
3. https://www.ansible.com/ <- very optional. Ansible is software for automating certain tasks, so you don't have to click manually.
4. https://www.atlassian.com/devops/what-is-devops
5. https://en.wikipedia.org/wiki/Infrastructure_as_code
6. https://12factor.net/

## Docker

So what is this Docker thing? Everyone writes about it.

Well, Docker is a tool for building and running containers, containerization. It's like a virtual machine simulating a computer inside a computer. The main difference, however, is that containers are much more efficient in terms of resources.

VMs set up an entire system and emulate everything from scratch. Docker uses existing components of your system, making it much less resource-hungry.

Thanks to containers, we can download ready-made 'images' that contain everything the application needs to run as well as the application itself.

Imagine having to manually install all dependencies, packages, etc.

Now imagine the same on 50 servers, because you happen to need to scale the application. Docker makes this easier. An image built once just needs to be run.

Currently, it's standard to containerize applications.

Containerizing applications with Docker has many advantages:

1. Reliability: Docker containers allow applications to run independently of the environment, meaning the application works the same on different operating systems and infrastructures.
2. Flexibility: Docker containers are easy to move between different environments, meaning you can easily expand your application to new platforms or move it to the cloud.
3. Resource savings: Docker containers are lighter than traditional virtual machines, meaning you can run more applications on the same hardware.
4. Speed: Docker containers are faster than virtual machines because they don't require installing an operating system and all necessary libraries.
5. Ease of use: Docker provides tools for creating, sharing, and running containers, making it easier to manage applications and their dependencies.

Generally speaking, containerizing applications with Docker helps increase reliability, flexibility, performance, and ease of managing applications, which is especially useful in a cloud environment.

Further reading:

1. https://docs.docker.com/get-started/overview/
2. https://www.docker.com/resources/what-container/

## Docker Compose

In short, Docker Compose is like scripts on steroids that allow us to more easily manage multiple containers. Imagine we have a database, broker, and worker in Docker in one application. Potentially a million Dockerfile files, lots of commands to type, etc. A mess overall.

This is where the docker-compose file and the tool of the same name come to help. It allows easy management of all application containers as one complete system, instead of managing each container separately. Docker Compose also makes it easy to resolve dependencies between containers, such as network connections and required data files.

## Docker Hub

Docker Hub is a public platform for storing and sharing Docker images. It allows easy sharing of images with others and using ready-made images ready to run. Docker Hub is also integrated with Docker Compose, enabling easy running of multiple containers simultaneously.

\pagebreak
