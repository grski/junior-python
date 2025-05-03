\pagebreak

# Data Types

In the previous chapter, we talked about variables. While on this topic, it's worth mentioning the types of data that our variables can store in Python. We'll talk about this specific language, but a similar division exists in most languages.

As I wrote in previous chapters, Python doesn't require us to define types for our variables; it doesn't have static typing. Remember what this meant and answer the question - what does the lack of static typing mean? What is dynamic typing? What are its advantages/disadvantages? Look in the book, maybe in the answers to previous chapters. Do this now.

Despite this, it's good to know what types we usually divide our variables into. Why? Because Python also uses them, it just somehow guesses what type we used. Depending on the type, different operations can be performed on the variable. When we think about it, it's logical because even though underneath it's all the same - binary code, on certain fragments that we interpret as X, we want to perform only operations from set Z, and when we interpret G, only from F. To put it simply, if we mark something as text, we'll treat it differently, or apply different modifications, than in a situation where something is a number. On numbers, we can perform arithmetic operations, while in text, we can search for our name, for example. Different operations depending on the type. Logical, right?

So in Python, we distinguish, among others, the following basic data types:

1. Numbers
2. Strings
3. Bytes
4. Boolean/Logical type

Among the more complex ones, we have:

1. Lists 