\pagebreak

# Databases

A bit about what's worth reading and what databases are all about.

So what are databases anyway? They're simply places where we want to store data in a relatively persistent way.

Databases come in all shapes and sizes, divided into various categories. We'll talk about Relational databases and the query language that has dominated database systems for decades - SQL. There are databases that don't use it, but that's outside the scope of this book.

Right off the bat, I'll note that because different types of databases exist, flame wars sometimes break out. Which one is better, etc. It's like Linux vs Windows, which Linux distro is best, Apples vs Oranges, etc.

The truth is that it's foolish to praise only one solution in every situation. Each database has its own use cases and niches where it fits best. Well, maybe except for OracleDB, which should have died long ago and stopped tormenting people with its existence. Anyway.

## SQL

SQL is simply a database language that allows you to make queries on data. That's all you need to know. In addition, read about simple queries: SELECT, UPDATE, INSERT, WHERE clause, and others.

Examples to analyze if you don't feel like googling yourself:

```sql
SELECT column1, column2, ... FROM table_name;
SELECT * FROM table_name;
SELECT DISTINCT column1, column2, ... FROM table_name;
DELETE FROM table_name WHERE condition;
DELETE FROM table_name WHERE condition;
SELECT column1, column2, ... FROM table_name WHERE condition;
SELECT column1, column2, ... FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

## Relational Databases

These are basically databases where we have some formal structure, let's say through defined tables (most commonly) and where we can define relationships between tables. To make things easier, I'll add a small general summary:

SQL (Structured Query Language) is a language designed for communicating with relational databases. It allows you to perform operations such as creating, modifying, and querying data stored in a database.

The advantages of SQL are:

1. Simplicity and ease of use - SQL is simple and intuitive, and its syntax is easy to understand.
2. Versatility - SQL can be used with many different types of databases, such as MySQL, Oracle, Microsoft SQL Server, and many others.
3. Performance - SQL is optimized for fast queries on large datasets.
4. Standardization - SQL is quite standardized, meaning different databases will have similar syntax and feature sets.

SQL is often used in web applications to manage data stored in databases, such as user registration, storing products in an online store, and creating reports.

### Tables

Tables are simply where we store data. Tables have columns and records/rows.

A table is a data structure in a database that stores data in the form of rows and columns. Each row in a table represents a single data record, and the columns define the different fields that make up that record.

For example, if we're creating an employee database, we could create a table containing information about employees, such as their first name, last name, position, salary, and hire date. The table might look something like this:

| First Name | Last Name | Position  | Salary | Hire Date  |
| ---------- | --------- | --------- | ------ | ---------- |
| John       | Smith     | Director  | 10000  | 2020-01-01 |
| Anna       | Johnson   | Manager   | 8000   | 2020-03-01 |
| Mark       | Williams  | Engineer  | 6000   | 2020-05-01 |
| Sarah      | Davis     | Assistant | 4000   | 2020-07-01 |

A table can contain any number of records and fields, and the data stored in it can be of various types, such as numbers, text, dates, etc. So, unlike Python, in SQL we define data types and it's mandatory.

The table is the basic data structure in a database and is used to store and provide data in applications.

Further reading:

1. https://www.w3schools.com/sql/sql_intro.asp

### Indexes

What are indexes? Indexes are special lookup tables that help us speed up data retrieval. They're like pointers showing what is where, thanks to which SQL knows where to jump and from where to read a given value. Like a table of contents in a book.

Thanks to them, SELECTs and WHERE clauses are much faster. However, operations for adding and updating data will be slower - when adding data, in addition to the table itself, the index must also be updated, which causes additional overhead.

Indexes can be created on one or more columns and can be combined.

When should you think twice before creating an index?

- For small tables
- For very frequently updated tables where data changes often
- When you have many NULLs in a column

### Relationships

Relationships describe the connections between a pair of tables. They exist when two tables are connected by a primary or foreign key.

Each relationship is described by a specific type of relationship, the bond between those two tables. The first example will be **one to many** (foreign key). An example of this could be the buyer <-> invoice relationship. An invoice has only one buyer by definition, while one buyer can have many invoices.

Another example is **many to many**. Here, let's use the fan-artist relationship as an example. One artist can have many fans. One fan can like many artists.

Further reading:

1. https://www.w3schools.com/sql/sql_foreignkey.asp
2. https://www.sqlshack.com/learn-sql-types-of-relations/

### Normalization

Normalization is a process in which we eliminate redundant data and establish relationships between tables.

This helps avoid data duplication and mess in the data.

Data normalization is a process of optimizing database structure by splitting data into smaller, more specialized tables, each containing only the necessary data. The goal of normalization is to ensure that data is stored in the best possible way, i.e., to avoid redundancy and ensure data integrity.

Data normalization is performed in several steps called normalization levels: 1NF, 2NF, 3NF.

Data normalization has several benefits, such as:

1. Easier data management - with fewer tables and no redundancy, data is easier to manage, less mess.
2. Performance improvement - smaller tables are easier to search and query, leading to better performance.

But more on the details later.

### Transactions and Concurrency

The deal with transactions is that sometimes we want to group certain operations and execute them together. For example, imagine a bank transfer scenario.

What if during an operation that can be broken down into the following steps:

1. Withdraw funds from Account A and update Account A balance.
2. Add the withdrawn funds to Account B and update Account B balance.

...there's a power outage, disk error, whatever? Well, exactly, Customer B wouldn't get the money and Customer A would lose it. Not cool. This is where transactions come in, all in white, allowing us to persist and, before completing a given group of operations, save them. All or nothing.

If something fails along the way, the transaction is rolled back as if it never happened and everyone's happy.

Here it's also worth reading about SELECT FOR UPDATE and Race Conditions. Important for concurrency.

Further reading: https://www.postgresql.org/docs/current/tutorial-transactions.html

### Subscriptions/Notifications

Sometimes we want to inform interested parties about our changes, e.g., adding a record to the database. Imagine that, for example, we have notifications in our application and we inform users about promotions, application updates, or something similar.

There are advanced solutions, you can simply poll the API, but that's a mediocre solution.

There are appropriate protocols and 3rd party services that nicely solve this problem.

However, the simplest is probably... LISTEN and NOTIFY from Postgres. Many people don't realize that Postgres has built-in notification support. But there it is. This Postgres is a nice multitool, handles everything. Anyway.

For review: https://www.cybertec-postgresql.com/en/listen-notify-automatic-client-notification-in-postgresql/

### Permissions and Security

Databases sometimes provide something called column/row-level security. What does this mean? Well, thanks to this, we can determine which user can see which columns or which records in which table in which database/schema.

Some DBs require us to install additional packages to achieve this, others have it by default, and still others don't provide such granular control at all. Postgres, for example, does. Cool stuff.

To configure, for example, row-level security, you need to add access rules to the table that specify which rows are visible to individual users or groups of users. For example, you can create a rule that allows a user named "john" to see only those rows where the "department" field has the value "marketing".

Row-level security is a useful tool for restricting access to data in a database and can be used in conjunction with other security mechanisms, such as user permissions and roles.

### Profiling

We can profile queries similarly to Python code. There are special tools for this. There's something called `EXPLAIN` and `ANALYZE`, there are statistics, there are profilers.

EXPLAIN allows us to examine in advance what a given database plans to do to execute a query. This is the so-called 'query plan'. It's worth remembering these two terms. In the case of Postgres, `EXPLAIN` generates the plan. `EXPLAIN ANALYZE` additionally executes it, providing actual data and statistics.

More reading: https://www.cybertec-postgresql.com/en/3-ways-to-detect-slow-queries-in-postgresql/

### Column Order

Even the order of columns, e.g., in Postgres, matters and affects how fast our query executes. A huge impact even.

I'll summarize here the conclusions I would expect from a junior. I wouldn't require the exact mechanism, but it would be nice to know that the number of columns in a table affects performance, which column we're processing also has an impact, a huge one. So it's worth remembering that creating huge tables with hundreds of columns is not desirable. Sometimes you need to split them and find a compromise between convenience and performance.

Further reading: https://www.cybertec-postgresql.com/en/column-order-in-postgresql-does-matter/

### Summary

Databases are an essential element of almost every system. It's worth knowing a little bit about them. SQL is the dominant language in the database world. Knowing the basics of it probably won't hurt us and might help.

## Tenants and What They Are

A bit about the tenant pattern in Django implemented using django-tenants and Postgres.

(Note: this piece was written a few years ago by me and Dominik Szady, who was my junior at the time <3)

### The Young One's Perspective
Hello! My name is Dominik, I'm a junior developer at thirty3.

An environment that will be demanding, but is probably the best for a beginner like me. A place where there's a mentor who will help me in difficult moments, answer all my questions and point the way, tell me about the mistakes I'm making.

Does this make learning programming easier than before? Absolutely! Does it make it easy? No!

Today I'd like to write a few words about my experience so far, new tasks, mentoring, and so on, in a joint article with my mentor - Olaf, and most importantly - about the tenancy pattern in software architecture.

I would say that the learning process can be divided into two parts:

understanding a new topic (technology, tool, etc.), which ends with having a general idea of how things are done, which allows you to build things based on an example, make small modifications to existing things, and so on;

an endless process of improvement that leads to being able to create complex things from scratch;

For me, being a junior developer means that I will often face problems that will require me to do the first part - learning something new to solve them. This is exactly how I could describe my first month at thirty3 - being outside my programming comfort zone and doing things I've never done before. Which is AWESOME.

#### First Days

The first days at a new job are always difficult and I swear that when I was setting up my work environment at previous companies, something always went wrong - I was missing some tools, packages, I was getting weird errors. Fortunately, running the project at thirty3 for the first time was completely the opposite.

In this case, the difference-maker was the combination of Docker and Makefile. All I had to do was download Docker (and docker-compose) on my computer and follow the damn README.md to have everything ready and working. The application works. Documentation, practices are defined, code is clear and easy to understand, tests are there. It was a breeze.

At least until a certain point. It wasn't long before I was hit by multi-tenant architecture. What is it? Imagine you have an application used by multiple companies (tenants). You'd like to make sure there's no accidental data leak between companies, while also ensuring the architecture is scalable and efficient.

#### Tenants to the Rescue

At thirty3 we used django-tenants to solve this problem, at least in a few cases. There's one database instance for storing data for the application, but multiple schemas - one for each tenant (company). This creates a logical separation between data. Before I jump to examples of how I tried to understand this concept and the beginnings, so hopefully you'll immediately notice my mistakes and understand how it works. Let's assume we have a very simple Django project that allows companies to create projects they will work on.

We need two Django apps:

```
companies
projects
```
And models declared in the respective models.py files:

```python
# `companies/models.py`
class Company(TenantMixin):
    name = models.CharField(max_length=255)
```

```python
# `projects/models.py`
class Project:
    name = models.CharField(max_length=255)
    is_paid = models.BooleanField()
```
The behavior we'd like to have is that each Company has its Projects, which are not accessible to other companies.

As I mentioned earlier, each tenant has its schema in the database - like a database within a database. It's created along with the creation of the model that inherits from TenantMixin (Company). What allows us to distinguish tenants is the unique schema_name attribute (TenantMixin attribute), which we must provide when creating each Company object. (Olaf's note: it doesn't have to be the schema name - it can be an ID or almost anything really, as long as it's unique. Generally, schema_name is just metadata that lets us know where to look in the db).

Besides that, we need to create a specific schema called "public", whose purpose (O: Actually it's there in Postgres by default, we just create a model in our tenants table and set up public as the shared schema) is to store global data not specific to a given tenant/company and all tenant schema_names.

#### Tenants in Django
The question we should now ask ourselves is: how does Django know which data should be stored in the "public" schema and which in schemas for specific tenants? This is managed in the settings file by setting the SHARED_APPS and TENANT_APPS variables. These are lists of Django applications (similar to INSTALLED_APPS). Placing an application in e.g., TENANT_APPS will mean that tables for Models from this application will be created in each tenant's schema. On the other hand, if we add our application to the SHARED_APPS list, then as with other applications where tenants don't occur, tables will be created in the "public" schema.

```
SHARED_APPS = ["companies", ...]
TENANT_APPS = ["projects", ...]
```
Another question is how Django knows which tenant schema to perform actions on? Tenants are identified by URL, e.g., the URL request "tenant.something.com" will cause the hostname to be looked up in the appropriate table in the "public" schema. If a match is found, the schema context is updated, meaning queries will be executed in the matched tenant's schema. Django-tenants provides several tools for setting schemas from the code perspective.

```python
with schema_context(schema_name):
    # queries will be performed against the schema "schema_name"
```
or

```python
with tenant_context(tenant_object):
    # queries will pe performed against the schema of tenant_object.
```
Knowing all this, let's look at the following code snippets to identify some mistakes I made during the thought process.

```python
class TenantsTestCase(BaseTenantTestCase):
    def test_tenants_example(self):
        companies = Company.objects.all()
        ...
```

The expected behavior for me would be to get all companies, yet the result was an empty QuerySet. Ok, maybe I need to create a tenant before displaying, logical, let's try.

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        companies = Company.objects.all()
```

This time I got an error

`Cannot get tenant list while in tenant context, enter public schema.`

I asked myself "What's going on?", but I managed to find somewhere the use of schema_context. So I tried:

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        with schema_context("public"):
            companies = Company.objects.all()
```

Great, no error this time. Anyway, the companies variable is still an empty QuerySet. Last try:

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        with schema_context("public"):
            Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        with schema_context("public"):
            companies = Company.objects.all()
```

Finally, this time I got a QuerySet with two Company objects. But wait, I only created one. Time to put it all together.

It turns out that when we run tests with Django-tenants, a new tenant is created, with schema_name "test" and all queries are executed against that schema, unless we switch it. (O: At least in our case, since we use the FastTenant case -> otherwise tenants are created e.g., per TestCase, which takes time because migrations are applied per tenant etc.)

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        # schema_context = "test"
        with schema_context("public"):
            # schema_context = "public"
            Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        # schema_context = "test"
        with schema_context("public"):
            # schema_context = "public"
            companies = Company.objects.all()
        # schema_context = "test"
```

Now let's remember that Company, which is our tenant object, is stored in the "public" schema, so the empty QuerySets we got earlier were correct because we were trying to look for the Company object in schemas that don't contain them. Going further, creating a Project object must happen in the context of a specific tenant schema, because that's where its tables are stored.

```python
class TenantsTestCase(BaseTenantTestCase):
    def test_tenants_example(self):
       # Here we can create project, as we are in context of "test"
       # tenant
       Project.objects.create(name="Test project", is_paid=True)
       with schema_context("public"):
            # Here we can not create Project, we are in "public"
            # context,no tables for Project here
            companies = Company.objects.all()
```

For me, working with tenants revolves around tracking how the context changes, so you always know what queries you can execute and what effects to expect.

### The Old Timer's Perspective
Ok. Enough from Dominik's perspective. Now it's my turn. I'll give you a broader view. What you've read so far is Dominik's understanding of the tenant concept and how we used it at thirty3. It's more or less correct, some things are too simplified, but the general idea is somewhere there as it should be. I'm a bit proud of him, it took me much longer to understand certain things. Enough back-patting. Now I'll try to give you more information about the decision process we had when we started using tenants, why we use them, and why you might want to too.

Let's start.

#### What Are Tenants?
First thing - tenants. What is it? It's a concept, most commonly used in e.g., SaaS products, that simplifying a bit, they are like your customers. I at least like to think of it that way. It's like when instead of creating a bespoke solution for a given Company, which only that company uses, you create a general solution where the company is just like a user.

Some things are defined globally in the DB and shared between users/companies, other things are defined and should only be accessible to that specific Company, and so on. In a normal case, when only that company will use the application, you don't have to think about it much. The problem arises when you want to globalize that application and have multiple companies. All of them have some private data, some public. This data should be separated and inaccessible to other companies using the SaaS. You need another layer of abstraction that logically binds or encapsulates this company data. Aw shiet, here come tenants. What are the other benefits?

#### Scaling SaaS
As time passes and our applications grow, when you start acquiring customers who aren't your immediate family or investors, things start to get complicated. Privacy suddenly becomes important. Data breaches/leaks are costly. Then the product starts gaining traction, your user base grows, optimization becomes an issue. This happens in almost every successful product.

It's good to think about these problems and prepare for them, but only as much as necessary so as not to over-engineer. In our case, in most cases, we decided to use the Tenant pattern for this purpose, using DB schemas to implement the plan. This makes it harder for all customers' data to leak or for one customer to gain access to another customer's sensitive data, easier to scale our applications, without overly burdening our work time.

#### Database Scaling Methods
What is the factor that limits us most often, at least in most applications? DB. What are the ways to scale a DB? Horizontal and vertical. Vertical means you have one DB that you just throw more resources at - better hardware. Such scaling has its limits. When you hit them, no matter how much money you have - that's the end. Can you do something about it?

This is where horizontal scaling comes to the rescue, i.e., using more machines/DBs instead of one. However, this is quite tricky - just setting up a second database next to it won't help. Things like master-slave patterns, data consistency, node networks, and so on suddenly come into play. Quite a complex topic in my opinion.

Of course, this method also has limitations, but they are often much larger than the limitations of a vertically scaled system. So yes - managing tenants in a SaaS-like product can be done in many different ways. The first is DB per client. Here we would probably have one larger DB with things shared globally in the application, and then smaller (or larger) DBs with data unique to the client.

The second is Schema per client, i.e., one database with sort of 'mini databases' inside.

The third is custom permissions and relationships in tables, for example with all clients' data placed in one schema, one db.

The first is expensive and troublesome to manage on a smaller scale.

The third often ends up with messy DB tables, privacy concerns, and a permission nightmare.

The second however... Well, it imposes almost no costs on the situation where you would have a regular single schema/DB architecture - it's not a SaaS architecture, but it makes it easier to scale and separate customer data through DB abstraction - instead of having many DBs that are troublesome to manage, it uses one DB as if there were "many", at least in a sense.

That's why we chose this solution. And honestly, we're quite happy with the results.

A big advantage of tenants is also the fact that queries still remain simple. Querying for invoices only from a given company? Just set the appropriate tenant context and that's it.

#### Different Tenant Management Methods
The so-called search path that we set for Postgres queries using our db router can be set in many ways. The traditional tenant pattern uses subdomains as a way to identify the tenant - e.g., x.myproduct.com will look up tenant x. That's one way. Remember to prohibit users from registering tenants with names of commonly used subdomains e.g., `ftp, mail, static` and so on, otherwise an unpleasant surprise may await us. Also remember to have certificates that have a wildcard for subdomains - otherwise you'll be without SSL for your tenants' subdomains, which is quite bad.

Another solution is, for example, putting it as part of the url, but not a subdomain. For example: `api.example.com/v1/tenant/someendpoint`. We used the latter.

#### What Tenants Gave Us
We achieved:

1. zero additional infrastructure management costs
2. zero additional infrastructure
3. ease of scaling -> change the way the search path is set for the db router and done, horizontal scaling in three minutes
4. customer data is logically separated from each other
5. queries still remain simple, as do permissions and tables

Anyway. Plus minus that's how tenants look and work.

PS: cons of having me as a mentor - you'll probably start writing.

## ORM

What is ORM? A few words about this very useful tool.

### What is ORM?

ORM, or Object-Relational Mapping. A tool that, using appropriate 'classes' or 'mappings', "converts" values from SQL into Python objects, which are actually easier to handle. It's a collection of useful methods, conveniences, and abstractions.

### ORM vs Pure SQL

The difference between ORM and the traditional approach, where we write pure SQL ourselves, is dramatic.

#### More Abstraction

The first difference is that ORM hides many things from us, providing a layer of abstraction over SQL itself. It does this at the cost of performance and at the cost of assuming that the programmer knows how ORM works, as their creators make certain decisions for us. These decisions affect how ORM works and how it creates queries. Sometimes not knowing them can cause us to shoot ourselves in the face, unknowingly. Ignorance can sometimes hurt. Plus the performance.

#### Lower Performance

It's not a huge overhead, but for complex queries you'll probably need to resort to writing pure SQL. It may also turn out that something that takes a minute in pure SQL, in ORM, due to e.g., the uncommon nature of the issue, may take hours. And vice versa. That happens too.

#### Still Worth It

Nevertheless, for most, the vast majority, which includes you, because otherwise you wouldn't be reading this book, ORM will be a significant convenience. However, as I always like to point out, it's worth knowing at least the basics of SQL and knowing how ORM works under the hood, even if very superficially.

#### Debugging/Profiling ORM

ORM is additionally harder to debug and profile - queries are generated by the engine, often they can be not very friendly in terms of readability for humans plus somewhat suboptimal in terms of performance. Again, for 99% of cases it won't matter, because a query returning a list of users will be equally simple here and there.

#### Serialization to/from Python Objects

ORM also provides us with a certain layer of abstraction in the form of mapping data from the database to Python objects. Data serialization and validation too. In the case of writing SQL queries manually, it often becomes your responsibility to check if the data is correct, its interpretation or conversion. When it comes to ORM, it either provides a range of tools that help us with this or even takes care of it for us. Pretty cool.

### Summary

ORM is simply a form of abstraction and simplification of database interaction from the level of a given language. It has its pros and cons, you need to know them to make an informed choice. In 95% of cases it will make your life easier, while the remaining 5% is probably outside the scope of this book intended for junior wannabes.

\pagebreak

