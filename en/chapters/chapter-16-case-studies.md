\pagebreak

# Case Studies of Various Applications

Here we'll discuss and analyze various cases of specific implementations, talk about decisions and System Design, why something is this way and not another, etc.

## Link Shortener

The task was to design a system for shortening links, assuming we'll handle quite a lot of traffic. I won't write it step by step, instead, I'm putting here notes from the conversation, a short description, and questions I asked.

1. Do we include authentication, or will it be handled outside the service? What is the business need?
   `What do you think?`
   For GETs decoding the shortened URL, auth isn't needed. For creation, it might be useful to be able to assign a user to the link they shortened. This will allow for future editing or management of shortened URLs.
   `So we include it`
   In this case, I would use JWT auth, simply due to preferences plus the possibility of later pushing auth to the Load Balancer level when we scale.
2. What will be the ratio of writes to reads? That is, how many GETs per each created URL.
   `Let's assume many, many reads per one write.`
   Then a regular database like Postgres. If needed, we can add batch creation of reads with intermediate cache storage and scale the database first vertically, then create a cluster with a write-only master and several read-only replicas/slaves. 