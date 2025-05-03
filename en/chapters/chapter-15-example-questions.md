\pagebreak

# Example Questions and Tasks

The questions you'll encounter depend strictly on what you include in your CV. Here I'll provide a list of questions I've encountered during recruitment interviews. I'll also add some of my own. I'll discuss all of them, at least briefly.

## Django

1. Distinct in Django model

1. Django middleware - what is it, where is it used?
   Answer: It's a piece of code that processes our request on input and output in some way. At this level we handle things like authentication.

1. Django request path
   Answer: Middleware -> router -> views -> models/code/whatever/ -> middleware again (optionally) -> client

1. Django select_related

1. How do migrations work in Django

1. Does makemigrations need a database connection?\
    Answer: No, it doesn't. Django compares models with the last saved state (using hashes, I think) and if it detects changes, it gets to work.

1. Does migrate need a database connection?\
    Answer: Yes - it makes changes to the database, so absolutely.

1. Is it possible to implement login/authentication without sessions?\
    Answer: Absolutely. JWT or Cookies for example.

1. Difference between Flask and Django\
    Answer: Google it, or better yet try it yourself and compare, because it's basic stuff.

1. Difference between Django and FastAPI

  Answer: Same as above.

1. Setting unique_together on a model attribute that has `null=True`. Does Django allow this? What's the risk?
   Answer: In the database null == null is False, so (null, 1) and (null, 1) will be unique for the database. Same for Python.

## Python

1. 3 favorite Python 3 features compared to Python 2
     Answer: Here the answers are obviously very individual, so I won't provide a template, but I, if I remember correctly, mentioned: f-strings, unicode as default encoding, assignment operator in expressions (walrus).

1. What would you change in Python - provide an example of a new PEP
     Answer: Very individual matter. I mentioned something about removing GIL. And speaking of GIL, time for the classic question in every Python dev recruitment.

1. What is GIL?
     Answer: Global Interpreter Lock, and what it is, I've already described, so you should know. In short, it causes a kind of lock that makes only one thread execute at a time in a given interpreter instance.

1. List types of comprehensions in Python.
     Answer: Like List Comprehensions, Set Comprehensions, Dict Comprehensions

1. Provide examples of the above, one for each type.
     Answer: Examples could be...

     ```python
     list_comprehension = [x for x in range(10)]
     dict_comprehension = {x: x**2 for x in range(10)}
     set_comprehension = {x for x in range(10)}
     set_comprehension_variation = set(x for x in range 10)
     tuple_comprehension = tuple(x for x in range(10) if x % 2)
     ```

1. What are the differences between a tuple and a list?
     Answer: The main difference is that one can be mutated, the other cannot - a list can be changed after creation, a tuple cannot - after initialization you can't change it. Besides that, there's a big difference in performance and implementation 'under the hood'. Because a tuple is immutable, the interpreter at initialization time knows exactly how much space it will take, so it allocates only as much memory as it needs, not a gram more. A list, on the other hand, during initialization, is created in such a way that it always allocates more memory than needed for the actual data in the user's list, so that later operations of adding something to the list work faster. If you create a list of, say, 50 elements, it turns out that your list has allocated space not for 50 elements, but for, say, 90. You can find out the exact numbers yourself.

1. What are generators and how do they differ from lists? 
       Answer: Generators are something that makes it easier for us to work with large amounts of data, because they are a kind of 'functions' that instead of loading some entire data set into memory, process values one by one and yield subsequent values. They differ from a list in that a list loads everything into memory, a generator doesn't, greatly simplifying things.

1. Can you program functionally in Python?
     Answer: Yes. It's possible - Python is a language that enables programming in many paradigms such as functional, object-oriented, imperative, procedural. One could argue whether this programming would be 'pure' (probably not) functional and so on, but it's possible in itself. Not a very popular option and not very promoted. Generally some people look askance at this combination.

1. Encapsulation in Python - is it possible?
     Answer: Yes and no. On one hand, Python lacks access modifiers like private or public, but we have conventional designations that cause, for example, variables or functions starting with underscore '_' to be rather private and shouldn't be used outside a given class. However, this is only a convention, not a language element, nothing will prevent you from using a method with an underscore everywhere.

1. How to solve the GIL problem?\
       Answer: Stackless Python or other implementations or using processes instead of threads in our concurrency model.

1. What's under the hood of a dict, what theoretical data structure?
      Answer: Hash map. 

1. How does access to dict elements proceed? 
      Answer: Based on the key, a hash is calculated using a specific algorithm. From this hash, an offset pointer to the reference is obtained.

1. Behavior of order of items added to dictionary in Python, how?
      Answer: In Python < 3.7: OrderedDict() from collections. In >= 3.7 dict() by default preserves order.

1. Differences between list and set.
      Answer: In a list elements can repeat. In a set they cannot. On sets we can perform certain operations that we can't on lists - similar to normal sets in mathematics - sum, intersection, difference. In the simplest case, you can think of a set as a list without repetitions. It's also worth remembering that data in a set is unordered by definition, so a set is completely unsuitable for ordering elements.

1. What type of objects do the functions dict.keys(), dict.values(), dict.items() return?
      Answer: Dict.items() - obvious. List of tuples. But not quite. Because if you look closer, it's a dict_items class, which isn't quite a list - it's a bit of an extended class, because it enables us to perform operations on it like on sets. Similarly with keys() and values(). So on objects returned by these functions you can perform operations like sum, difference or intersection from sets. Tldr - these functions return an iterable set-like object.

1. Bitwise operators in Python. Which do you know, what are they for?
      Answer: << and >>, bitwise shift left and right
      & - bitwise conjunction, i.e. 'and'
      | - bitwise alternative, i.e. or
      ~ - bitwise negation, i.e. ~x = -x – 1
      ^ - bitwise exclusive alternative

1. When to use list comprehension, and when a normal for loop?
      Answer: Where we can, we should use list comprehensions, because they are more readable and more efficient in terms of execution time, because they are optimized by the interpreter and run at a speed somewhat close to C speed, while normal for loops are executed normally by the interpreter at normal Python code speed. However, if we want to do something that has side effects or complex logic, sometimes it's worth sticking to normal loops.

1. What are the differences between for and while loops in Python?
      Answer: Mainly syntactic and performance-related. A while loop will always be executed by the Python interpreter, while a for loop used in list comprehension, for example, can be optimized and run much faster.

1. What is an iterator and an iterable? Difference between iterator and iterable.

1. `float("NaN") == float("NaN")` what's the result?

1. `True is True` and here?

1. `1 is 1` and here?

1. Write a program that checks if a string provided by the user is a palindrome (a sequence that reads the same forwards and backwards).

1. Write a program that counts how many times a given digit appears in a sequence of digits provided by the user.

1. Write a function that takes a list of numbers and returns their sum and arithmetic mean.

1. Write a program that creates a dictionary containing statistics about letters (how many times each letter appears in the text).

1. Write a program that reads a CSV file and displays its contents in table form.

1. Write a program that implements the merge sort algorithm.

1. Write a program that implements the quicksort algorithm.

1. Write a program that implements Dijkstra's algorithm for finding shortest paths in a graph.

## Git
1. What's the difference between merge and rebase?
Answer: Merge creates a 'merge commit', while 'rebase' kind of pastes commits from the merged branch. Besides that, using rebase, you can really mess up git logs. Which is better? Depends who you ask, there are different schools.
1. Differences between Git and GitHub.
Answer: Git is a tool - version control system, while GitHub is a service where we can host our Git repositories and generally collaborate with others.
1. What does git stash do? And git stash pop?

## Http/Rest
1. What is REST?
   Answer: google it
1. What determines what type of content can be sent to/from the server?
   Answer: Headers, specifically content-type.
1. Where do parameters go in a request?
   Answer: In the URL. ? and &.
1. 403 vs 401
   Answer: Forbidden vs unauthorized. Difference between when user is not logged in (no access) vs is logged in but doesn't have permission.
1. HTTP response codes 1xx 2xx 3xx 4xx 5xx
   Answer: Check wiki.
1. What is JWT?
   Answer: JWT is simply an authentication method where we have a specific three-part token generated using some secret key/certificate, which contains a specific payload. 
1. Is it possible to have authentication at the load balancer level so that the application doesn't have to do it additionally later?
   Answer: Absolutely. JWT ftw.
1. Ways to authenticate a request: basic auth and tokens - describe and characterize how they differ.
   Answer: Google it
1. Where does the server get username and password in basic auth?
   Answer: Header. Which one?
1. How does the browser know that a given response should be displayed as json and not as plaintext?
   Answer: Again - CONTENT-TYPE
1. Difference between PUT and PATCH.
    Answer: One requires providing all serializer fields, the other doesn't. Why? Which method requires all fields, which doesn't?
1. Available HTTP methods/verbs.
    Answer: Google it.

## Databases
1. What is a join in SQL, how does it work, example
1. Database normalization - what is it, what's it about.
1. Types of databases. Relational and non-relational, a bit about them.

## General Programming Concepts
1. What is OOP.
1. What is SOLID - name at least one
1. Let's say I type something in the browser window and click enter to go to a given page. What happens under the hood then?

## Data Structures
1. What is a tree?
1. Balanced binary tree?
1. How does a hashmap/dictionary work?
1. And a set?

## Rock Paper Scissors

1. Write a rock_paper_scissors() function that simulates a random game of rock paper scissors and then displays which player, p1 or p2, won the round. Does someone always win? Can there be a tie? Try to make your solution as short as possible. Try not to use ifs at all. Yes, it can be done without them.
   I managed to write the function simulating a single random game in 5 lines of code total, without an if.

2. Now add code that will call such a simulation 10 times and print its result to output.

Example of my solution:

```python
import random as ra
```

```python
def rock_paper_scissors():
    gestures = ['rock', 'paper', 'scissors'] # order here is important
    p1, p2 = ra.randint(0, 2), ra.randint(0, 2)
    return "P1: {0}, x P2: {1}, Result: {2}".format(
        gestures[p1], 
        gestures[p2],
        {0: 'tie', 1: 'p1', 2: 'p2'}[(p1-p2)%3]
    )
```

```python
for i in range(10):
    print(rock_paper_scissors())
```

## Number Operations

Here are two exercises to do.

1. How can you implement multiplication by 2 in Python without using the multiplication operator, exponentiation, pow function, sqrt?
2. What about division by two considering similar restrictions as above?
3. Write an is_prime(number) function that checks if a given number is prime.
4. Same as above, but in one line of code.

## Statistics from Logs
Here we'll go in English. The task description and potential solution below. The whole thing can be further simplified and refactored, but I'm providing here a solution that I quickly scribbled during a live recruitment. 30 minutes. 

1. You are given a large log file which stores user interactions with an application. The entries in the log file follow the following schema: `{userId, timestamp, actionType}`. Calculate the average session time across all users. Assume that data yet get is valid and not sorted in any way. Assume that number of records that are `opens` will be equal to `closes`.
2. What if we want to modify the code to also calculate average session time per user?

```python
from collections import defaultdict
from enum import Enum


# User level 1 -> 1512, 2-> 17
events = [
    [1, 1435459573, "Close"], [1, 1435456566, "Open"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [2, 1435462567, "Open"], [2, 1435462584, "Close"]
]


class ActionTypeEnum(Enum):
    OPEN = "Open"
    CLOSE = "Close"

    @classmethod
    def opposite(cls, action_type: str) -> str:
        if action_type == cls.OPEN.value:
            return cls.CLOSE.value
        return cls.OPEN.value

class Event:
    def __init__(self, user_id, timestamp, action_type):
        self.user_id = user_id
        self.timestamp = timestamp
        self.action_type = action_type

    def calculate_difference(self, second_event):
        if self.action_type == ActionTypeEnum.CLOSE.value:
            return self.timestamp - second_event.timestamp
        return second_event.timestamp - self.timestamp


def calculate_avg_session_time(events: list) -> tuple:
    time_sum, number_of_sessions = 0, 0
    user_level_sum = defaultdict(int)
    user_level_matches = defaultdict(int)

    user_time_mapping: dict = defaultdict(lambda: defaultdict(list))
    for event in events:
        wrapped_event: Event = Event(*event)
        opposite_action = ActionTypeEnum.opposite(wrapped_event.action_type)
        user_id: int = wrapped_event.user_id
        if first_user_record := user_time_mapping[user_id][opposite_action]:
            first_event = first_user_record.pop()
            user_session_time = wrapped_event.calculate_difference(first_event)
            time_sum += user_session_time
            user_level_sum[user_id] += user_session_time
            user_level_matches[user_id] += 1
            number_of_sessions += 1
            continue
        user_time_mapping[user_id][wrapped_event.action_type].append(wrapped_event)
    user_level_average = {
        user_id: user_level_sum[user_id] / user_level_matches[user_id] 
        for user_id in user_level_sum.keys()
    }
    return time_sum / number_of_sessions, user_level_average
print(calculate_avg_session_time(events=events))
# (1213.0, {1: 1512.0, 2: 17.0})
```

Task shamelessly borrowed from a recruitment process.

## Query Statistics

Create a class that will store the total execution time of a given query. As input data, you will receive records containing the query id and duration. Records can be partial, meaning one id can have multiple records. Such values should be summed together.

Additionally, implement a method `get_top_k_records` in this class that will return the specified number of queries with the longest execution time.

```python
from collections import defaultdict
from typing import Iterable

events = [
  {"id": 2, "partial_execution_time": 10},
  {"id": 1, "partial_execution_time": 15},
  {"id": 1, "partial_execution_time": 12},
  {"id": 3, "partial_execution_time": 25},
  {"id": 3, "partial_execution_time": 10},
  {"id": 4, "partial_execution_time": 15},
]

class QueryStats:
  def __init__(self):
    self.query_execution_times: dict = defaultdict(int)
  
  def add(self, event: dict) -> dict:
    self.query_execution_times[event["id"]] += event["partial_execution_time"]
    return event
  
  def get_top_k_records(self, k: int) -> Iterable:
    return sorted(self.query_execution_times.items(), key=lambda record: record[1], reverse=True)


query_stats = QueryStats()
for event in events:
  query_stats.add(event)

print(query_stats.get_top_k_records(5))
```

Task shamelessly borrowed from a recruitment process.

## Order Book

Implement an Order Book that handles regular orders with Price Limit (Limit Order).

Then add support for Iceberg Orders. What this is and how it works you can read in technical documentation of exchanges. For example: SETSmm and Iceberg Orders, SERVICE &TECHNICAL DESCRIPTION from London Stock Exchange. Or just google it.

We read data from standard input as subsequent orders and update the book in real time. If a transaction occurs, we print it to standard output. After adding each order, we print the updated book to standard output.

### Input Data Format

JSON. Each order has a "type" and "order" field. Type contains the order type - Iceberg or Limit. Order contains the order data.

- "direction" order type ("Buy" or "Sell"), 
- "id" unique order identifier (positive integer),
- "price" price (positive integer)
- "quantity" order size (positive integer).

Iceberg orders have an additional field - `peak`, which denotes the peak of this order.

We assume that the input data is correct.

```json
{"type": "Limit", "order": 
{"direction": "Buy", "id": 1, "price": 14, "quantity": 20}}
{"type": "Iceberg", "order": 
{"direction": "Buy", "id": 2, "price": 15, "quantity": 50, "peak": 20}}
{"type": "Limit", "order": 
 {"direction": "Sell", "id": 3, "price": 16, "quantity": 15}}
{"type": "Limit", "order": 
 {"direction": "Sell", "id": 4, "price": 13, "quantity": 60}}
```

### Output Data Format

When we read information about a new order and want to print the updated state of the order book, the JSON object we should print should have the following properties/attributes: `buyOrders` and `sellOrders`. Each order should contain "id", "price" and "quantity" fields. Sorted by price. Buy orders non-increasing. Sell orders non-decreasing. If the price is the same, priority goes to the time the order was added. Example:

```json
{"buyOrders": [{"id": 2, "price": 15, "quantity": 20}, 
               {"id": 1, "price": 14, "quantity": 20}],
"sellOrders": [{"id": 3, "price": 16, "quantity": 15}]}
```

Example session (sorry for ugly formatting, copy and fix it yourself):

```json
{"type": "Limit", "order": 
 {"direction": "Buy", "id": 1, "price": 14, "quantity": 20}} 
{"buyOrders": [
    {"id": 1, "price": 14, "quantity": 20}], "sellOrders": []
}
{"type": "Iceberg", 
 "order": {
     "direction": "Buy", "id": 2, "price": 15,
     "quantity": 50, "peak": 20
 }}
{"buyOrders": [
    {"id": 2, "price": 15, "quantity": 20},
    {"id": 1, "price": 14, "quantity": 20}
], 
 "sellOrders": []}
{"type": "Limit", 
 "order": {"direction": "Sell", "id": 3, "price": 16, "quantity": 15}}
{"buyOrders": [
    {"id": 2, "price": 15, "quantity": 20}, 
    {"id": 1, "price": 14, "quantity": 20}
],
"sellOrders": [
    {"id": 3, "price": 16, "quantity": 15}]
} 
{"type": "Limit", "order": 
 {"direction": "Sell", "id": 4, "price": 13, "quantity": 60}}
{"buyOrders": [{"id": 1, "price": 14, "quantity": 10}],
 "sellOrders": [{"id": 3, "price": 16,"quantity": 15}]} 
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 20} 
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 20} 
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 10} 
{"buyOrderId": 1, "sellOrderId": 4, "price": 14, "quantity": 10}
```

Another example:
```json
{"type": "Iceberg", "order": 
 {"direction": "Sell", "id": 1, "price": 100, "quantity": 200,
"peak": 100}}
{"type": "Iceberg", "order":
{"direction": "Sell", "id": 2, "price": 100, "quantity": 300,
"peak": 100}}
{"type": "Iceberg", "order": 
{"direction": "Sell", "id": 3, "price": 100, "quantity": 200,
"peak": 100}}
{"type": "Iceberg", "order": 
{"direction": "Buy", "id": 4, "price": 100, "quantity": 500,
"peak": 100}}
gives us
{"sellOrders": [{"id": 3, "price": 100, quantity: 100}, 
                {"id": 2, "price": 100, quantity:
100}], "buyOrders": []}
```

Example solution on my github - [github.com/grski](https://github.com/grski)

Task shamelessly borrowed from a recruitment process.

I'm not including the solution here as it's too long.

## URL Shortener

In this task, please create a URL shortening service. Use Python and any framework. For example, django or fastapi.

So a service that shortens URLs, e.g., from https://codesubmit.io/library/react to http://short.est/GeAi9

Similarly, the reverse operation also works.

- Language: **Python**
- Framework: **any**
- Endpoints:
  - /encode - encodes full URL to shortened
  - /decode - decodes shortened to full URL.

-   Both return JSON
-   How the encoding will be done is an implementation detail. Choose as you see fit. As long as it can be encoded and then decoded. You don't need to attach a database - we can keep it in memory.

-   Create documentation on how to run and use.
-   Write tests.
-   Use GIT and show your reasoning through commit history
-   Write code as if it were going to production. Clean, elegant, beautiful.

Example solution on my github - [github.com/grski](https://github.com/grski)

Task shamelessly borrowed from a recruitment process.

I'm not including the solution here as it's too long.

## Static Site Generator

What does this mean? Check Google under `SSG` or `static site generator`. Generally, it's a piece of code, a program that generates static pages based on some foundation, something opposite to the current approach, i.e., creating SPAs. In my case, I decided to create a very simple system for my own blog. Here I leave the implementation details to you. Let this be part of the task - write down requirements, list functionalities, etc. Let your imagination run wild. The minimum I expect is delivering functionalities sufficient for running a blog - index with a list of posts and single posts.

\pagebreak

```python
def find_all_posts(directory: str = "posts") -> Iterable[str]:
    """ All the md posts - both extensions .markdown and .md"""
    return find_all_markdown_and_md_files(directory=directory)


def find_all_pages(directory: str = "pages") -> Iterable[str]:
    """ Similar to the one above, but searches for 
    posts - another directory. Both .md and .markdown """
    return find_all_markdown_and_md_files(directory=directory)


def find_all_markdown_and_md_files(directory: str) -> Iterable[str]:
    """ Base method that finds both .md and .markdown recursively
    in a given directory and it's children. """
    md_files: Generator = iglob(
        os.path.join(directory, "**", "*.md"), recursive=True
    )
    markdown_files: Generator = iglob(
        os.path.join(directory, "**", "*.markdown")
    )
    return chain(md_files, markdown_files)
```

There are comments in the code, so I won't describe it additionally. Next piece of code:

```python
md: Markdown = Markdown(
    extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"]
)

def render_markdown_to_html(md: Markdown, filename: str) -> str:
    """ Markdown to html. Important here is to keep the reset() method. """
    return md.reset().convert(open(filename).read())

def render_jinja_template(template: Template, context: dict) -> str:
    """ Rendering jinja template with a context and global config. """
    context_with_globals = {**context, **CONFIG}
    return template.render(context_with_globals)

def build_meta_context(md: Markdown) -> Dict[str, str]:
    """
    This builds context that we get from Meta items from markdown like
    post/page Title, Description and so on.
    """
    return {key: "\n".join(value) for key, value in md.Meta.items()}
```

Next fragment:

\pagebreak

```python
def build_article_context(article_html: str, md: Markdown) -> Dict[str, str]:
    """ Contant that'll be used to render template with jinja. """
    return {"content": article_html, **build_meta_context(md=md)}


def add_url_to_context(jinja_context: dict, new_filename: str) -> dict:
    """ Builds and adds url for a given page/post 
    to jinja context. """
    jinja_context["url"] = f"{BASE_URL}{new_filename.replace(f'{DIST_DIR}/', '')}"
    return jinja_context

def save_output(original_file_name: str, output: str) -> str:
    """ Saves a given output based on the original 
    filename in the dist folder"""
    new_location: str = os.path.splitext(
        os.path.join(DIST_DIR, original_file_name)
    )[0] + ".html"
    new_directory, _ = os.path.split(new_location)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    output_file: TextIO = open(new_location, "w")
    output_file.write(output)
    return new_location

def gather_statics() -> None:
    template_statics = os.path.join(TEMPLATE_DIR, "static")
    if os.path.exists(template_statics):
        shutil.copytree(
            template_statics, os.path.join(DIST_DIR, "static"),
            dirs_exist_ok=True
        )
```

Putting it all together:

\pagebreak

```python
def render_blog() -> None:
    """ Renders both pages and posts for the blog 
    and moves them to dist folder."""
    posts: Iterable[dict] = reversed(
        sorted(render_posts(), key=lambda x: x["date"])
    )
    render_all_pages()
    render_index(posts=posts)
    gather_statics()


def render_all_pages() -> None:
    """ Rendering of all the pages for the blog.
    markdown -> html with jinja -> html"""
    template: Template = jinja_environment.get_template("index.html")
    for filename in find_all_pages():
        render_page(filename=filename, md=md, template=template)


def render_page(
    filename: str, 
    md: Markdown, 
    template: Template, 
    additional_context: dict = None
):
    additional_context = additional_context if additional_context else {}
    page_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = {
        "page": {"content": page_html}, **additional_context
    }
    output: str = render_jinja_template(
        template=template, context=jinja_context
    )
    save_output(
        original_file_name=jinja_context.get("slug", filename), output=output
    )


def render_posts() -> Iterable[dict]:
    template: Template = jinja_environment.get_template("detail.html",)
    return [
        render_and_save_post(md=md, filename=filename, template=template)
        for filename in find_all_posts()
    ]


def render_and_save_post(md, filename, template) -> dict:
    """ Renders blog posts and saves the output as 
    html. md -> html with jinja -> html"""
    article_html: str = render_markdown_to_html(md=md, filename=filename)
    jinja_context: dict = build_article_context(article_html=article_html, md=md)
    output: str = render_jinja_template(template=template, context=jinja_context)
    new_filename: str = save_output(
        original_file_name=jinja_context.get("slug", filename), output=output
    )
    return add_url_to_context(
        jinja_context=jinja_context, new_filename=new_filename
    )


def render_markdown_to_html(md: Markdown, filename: str) -> str:
    """ Markdown to html. Important here is to keep the reset() method. """
    return md.reset().convert(open(filename).read())


def render_index(posts: Iterable[dict]) -> None:
    md: Markdown = Markdown(
        extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"]
    )
    template: Template = jinja_environment.get_template("index.html")
    filename = "index.md"
    additonal_context: dict = {"articles": posts}
    render_page(
        filename=filename,
        md=md, 
        template=template,
        additional_context=additonal_context
    )
```

This is described in more detail in [my blog post](https://grski.pl/braindead.html), and the full source code is on github - [braindead](https://github.com/grski/braindead). There you'll also find commit history, description, etc. Take a look.

## One-liner

Write a one-line Python generator or iterator expression that returns the sequence of integers generated by repeatedly adding the ascii values of each letter in the word "Close" to itself. The first 10 integers in this sequence are: 67, 175, 286, 401, 502, 569, 677, 788, 903, 1004. Assume any needed Python standard library modules are already imported.

Answer:

```python
islice(accumulate(cycle("Close"), func=lambda x, y: x + ord(y), initial=0), 1, None)
```

Such a puzzle.

\pagebreak
