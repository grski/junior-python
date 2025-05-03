\pagebreak

# Databases

A bit about what databases are and what's worth reading about them.

What are databases anyway? Simply put, they are places where we want to store data in a relatively permanent way.

Databases come in various forms and are divided into different categories. We'll focus on Relational databases and the query language that has dominated database systems for decades - SQL. There are databases that don't use SQL, but that's beyond the scope of this book.

Let me point out right away that because there are different types of databases, sometimes there are heated debates about which one is better, etc. Something like Linux vs Windows, which Linux distro is best, Apples or Plums, etc.

The truth is that it's foolish to praise only one solution in every situation. Each database has its own applications and certain niches where it works best. Well, maybe except for OracleDB, which should have died long ago and stopped torturing people with its existence. Anyway.

## SQL

SQL is simply a database language that allows you to query data. That's all you need to know. Additionally, read about simple queries: SELECT, UPDATE, INSERT, WHERE clause, and others.

Examples to analyze if you don't feel like Googling yourself:

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

These are generally databases where we have some formal structure, say, through defined tables (most commonly) and where we can define relationships between tables. To make things easier, I'll add a small general summary:

SQL (Structured Query Language) is a language designed for communicating with relational databases. It allows operations such as creating, modifying, and querying data stored in the database.

The advantages of SQL are:

1. Simplicity and ease of use - SQL is simple and intuitive, and its syntax is easy to understand.
2. Versatility - SQL can be used with many different types of databases, such as MySQL, Oracle, Microsoft SQL Server, and many others.
3. Performance - SQL is optimized for performing fast queries on large datasets.
4. Standardization - SQL is fairly standardized, meaning different databases will have similar syntax and set of functions.

SQL is often used in web applications to manage data stored in databases, such as user registration, storing products in an online store, and creating reports.

### Tables

Tables are simply where we store data. Tables have columns and records/rows.

A table is a data structure in a database that stores data in the form of rows and columns. Each row in a table represents a single data record, and the table's columns define different fields that make up that record.

For example, if we're creating an employee database, we could create a table containing information about employees, such as their first name, last name, position, salary, and hire date. The table might look something like this:

| First Name | Last Name   | Position  | Salary | Hire Date     |
| ---------- | ----------- | --------- | ------ | ------------- |
| John       | Smith       | Director  | 10000  | 2020-01-01    |
| Anna       | Johnson     | Manager   | 8000   | 2020-03-01    |
| Mark       | Williams    | Engineer  | 6000   | 2020-05-01    |
| Agatha    | Brown       | Assistant | 4000   | 2020-07-01    |

A table can contain any number of records and fields, and the data stored in it can be of various types, such as numbers, text, dates, etc. Unlike in Python, in SQL we define data types and this is mandatory.

A table is the basic data structure in a database and is used to store and provide access to data in applications.

For reading:
1. https://www.plukasiewicz.net/SQL/Introduction (a bit formal, but might be helpful)

### Indexes

What are indexes? Indexes are special lookup tables that allow us to speed up data retrieval. They're like pointers that tell SQL where to jump and from where to read a given value. Like a table of contents in a book.

Thanks to them, SELECTs and WHERE clauses are much faster. However, operations for adding and updating data will be slower - when adding data, besides the table itself, the index also needs to be updated, which causes additional overhead.

Indexes can be created on one or more columns, and they can be combined.

When should you think twice before creating an index?

- In the case of small tables
- In very frequently updated tables where data changes often
- When we have a lot of NULLs in some column

### Relationships

Relationships describe connections between pairs of tables. They exist when two tables are connected by a primary or foreign key.

Each relationship is described by a specific type of relationship, the constraints between these two tables. The first example will be **one-to-many** (one to many/foreign key). An example of this could be the relationship buyer <-> invoice. An invoice has only one buyer by definition, while one buyer can have many invoices.

Another example is **many-to-many**. Here, let's use the example of a fan of an artist. One artist can have many fans. One fan can like many artists.

For reading:
1. https://developeronthego.pl/sql-schemat-bazy-danych/
2. https://analityk.edu.pl/relacyjna-baza-danych-o-co-chodzi-z-tymi-relacjami-sql/

### Normalization

Normalization is the process where we get rid of unnecessary data and establish relationships between tables.

This helps avoid data duplication and mess in the data.

Data normalization is the process of optimizing the database structure by separating data into smaller, more specialized tables, each containing only necessary data. The goal of normalization is to ensure that data is stored in the best possible way, i.e., to avoid redundancy and ensure data integrity.

Data normalization is performed in several steps, called normalization degrees. 1NF, 2NF, 3NF.

Data normalization has several benefits, such as:

1. Easier data management - with fewer tables and no redundancy, data is easier to manage, less mess.
2. Improved performance - smaller tables are easier to search and query, leading to better performance.

But more details later.

### Transactions and Concurrency

With transactions, it's about sometimes wanting to group certain operations and perform them together. For example, imagine the example from the link below - a bank transfer.

What if during the execution of an operation that can be divided into the following steps:

1. Withdraw funds from account A and update account A's balance.
2. Add the withdrawn funds to account B and update account B's balance.

...there's a power outage, disk error, whatever? Well, client B wouldn't get the money and client A would lose it. Not cool. This is where transactions come in, allowing us to permanently record a group of operations before completing them. All or nothing.

If something fails along the way, the transaction is rolled back as if it never happened and everyone's happy.

Here it's also worth reading about SELECT FOR UPDATE and Race Condition. Important for concurrency.

For reading: https://mst.mimuw.edu.pl/lecture.php?lecture=bad&part=Ch7

### Subscriptions/Notifications

Sometimes we want to inform interested parties about our changes, e.g., adding a record to the database. Imagine that we have notifications in our application and we inform users about promotions, app updates, or something similar.

There are advanced solutions, you can simply poll the API, but that's a mediocre solution.

There are appropriate protocols and 3rd party services that nicely solve this problem.

But the simplest is probably... LISTEN and NOTIFY from Postgres. Many people don't realize that Postgres has built-in notification support. But here it is. Postgres is a nice all-in-one solution. Anyway.

To check out: https://www.cybertec-postgresql.com/en/listen-notify-automatic-client-notification-in-postgresql/

### Permissions and Security

Databases sometimes provide something like column/row-level security. What does this mean? Well, thanks to this we can determine which user can see which columns or even which records in which table in which database/schema.

Some DBs require us to install additional packages to achieve this, others have it by default, and some don't provide such granular control at all. Postgres, for example, does. Nice stuff.

To configure row-level security, you need to add access rules to the table that determine which rows are visible to specific users or groups of users. For example, you can create a rule that allows a user named "john" to see only those rows where the "department" field has the value "marketing".

Row-level security is a useful tool for limiting access to data in a database and can be used in combination with other security mechanisms, such as user permissions and roles.

### Profiling

We can profile queries similarly to Python code. There are special tools for this. There's something called `EXPLAIN` and `ANALYZE`, there are statistics, there are profilers.

EXPLAIN allows us to examine in advance what a given database plans to do to execute a query. This is the so-called 'query plan'. It's worth remembering these two terms. In the case of Postgres, `EXPLAIN` generates a plan. `EXPLAIN ANALYZE` additionally executes it, providing actual data and statistics.

More to read: https://www.cybertec-postgresql.com/en/3-ways-to-detect-slow-queries-in-postgresql/

### Column Order

Even the order of columns in, for example, Postgres matters and affects how quickly our query will execute. Huge impact even.

I'll summarize here the conclusions I would expect from a junior. I wouldn't require knowledge of the exact mechanism, but it would be nice to know that the number of columns in a table affects performance, which column we're processing also has an impact, a huge one. It's worth remembering that creating huge tables with hundreds of columns is not desirable. Sometimes you need to split them and find a compromise between convenience and performance.

To read: https://www.cybertec-postgresql.com/en/column-order-in-postgresql-does-matter/

### Summary

Databases are an essential element of almost every system. It's worth knowing a bit about them. The dominant language in the database world is SQL. Knowledge of its basics probably won't hurt us and might help.

## Tenants and What They Are

A bit about the tenant pattern in Django implemented using django-tenants and Postgres.

(Note: this piece was written several years ago by me and Dominik Szadego, who was my junior at the time <3)

### Junior's Perspective
Hi! My name is Dominik, I'm a junior developer at thirty3.

The environment that will be demanding, but is probably the best for a beginner like me. A place where there is a mentor who will help me in difficult times, answer all my questions and show the way, tell me about the mistakes I make.

Does this make learning programming easier than before? Absolutely! Does it make it easy? No!

Today I would like to write a few words about my experience so far, new tasks, mentoring and so on, in a joint article with my mentor - Olaf, and most importantly - about the tenancy pattern in software architecture.

I would say that the learning process can be divided into two parts:

understanding a new topic (technology, tool, etc.), which ends with having a general idea of how things are done, which allows building things based on example, making small modifications to existing things and so on;

an endless process of improvement that leads to being able to create complex things from scratch;

For me, being a junior programmer means that I will often face problems that will require me to perform the first part - learning something new to solve them. This is exactly how I could describe my first month at thirty3 - being outside my programming comfort zone and doing things I had never done before. Which is AWESOME.

#### First Days

The first days in a new job are always difficult and I swear that when I was setting up my work environment in previous companies, something always went wrong - I was missing some tools, packages, getting strange errors. Fortunately, running the project at thirty3 for the first time was completely the opposite.

In this case, the difference-maker was the combination of Docker and Makefile. All I had to do was download docker (and docker-compose) on my computer and follow the damn README.md to have everything ready and working. The application works. Documentation, practices are defined, code is clear and easy to understand, tests are there. It was a breeze.

At least until a certain point. It didn't take long before I was hit by the multi-tenant architecture. What is this. Imagine that you have an application used by many companies (tenants). You would like to be sure that there is no accidental data leakage between companies, while at the same time ensuring that the architecture is scalable and efficient.

#### Tenants to the Rescue

At thirty3 we used django-tenants to solve this problem, at least in several cases. There is one database instance to store data for the application, but many schemas - one for each tenant (company). This creates a logical separation between data. Before I jump to examples, let me try to understand this concept and the beginnings, so, hopefully, you will immediately notice my mistakes and understand how it works. Let's assume that we have a very simple Django project that allows companies to create projects they will work on.

We need two Django apps:

```
companies
projects
```
And models declared in appropriate models.py files:

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
The behavior we would like to have is that each Company has its own Projects, which are not available to other companies.

As I mentioned earlier, each tenant has its own schema in the database - like a database within a database. It is created along with the creation of a model that inherits from TenantMixin (Company). The thing that allows us to distinguish tenants is a unique schema_name attribute (TenantMixin attribute), which we must provide when creating each Company object. (Olaf's note: this doesn't have to be the schema name - it can be an ID or almost anything really, as long as it's unique. Generally schema_name is just metadata that allows us to know where to look in the db).

In addition, we need to create a specific schema called "public", whose purpose (O: Actually it's there in postgres by default, we just create a model in our tenants table and set up public as a shared schema) is to store global data not specific to a given tenant/company and all tenant schema_names.

#### Tenants in Django
The question we should ask ourselves now is: how does Django know which data should be stored in the "public" schema and which in the schemas for specific tenants? This is handled in the settings file by setting the SHARED_APPS and TENANT_APPS variables. These are lists of Django apps (similar to INSTALLED_APPS). Placing an app in e.g. TENANT_APPS will mean that tables for Models from this app will be created in each tenant's schema. On the other hand, if we add our app to the SHARED_APPS list, then as in the case of other apps where there are no tenants, tables will be created in the "public" schema.

``` 
SHARED_APPS = ["companies", …]
TENANT_APPS = ["projects", …]
```
Another question is, how does Django know on which tenant's schema to perform actions? Tenants are identified by URL, e.g. a request to URL "tenant.something.com" will cause the hostname to be looked up in the appropriate table in the "public" schema. If a match is found, the schema context is updated, which means that queries will be performed in the matched tenant's schema. Django-tenants provides several tools for setting schemas from the code perspective.

```python
with schema_context(schema_name):
    # queries will be performed against the schema "schema_name"
```
or

```python
with tenant_context(tenant_object):
    # queries will pe performed against the schema of tenant_object.
```
Knowing all this, let's look at the following code fragments to identify some mistakes I made during the thought process.

```python
class TenantsTestCase(BaseTenantTestCase):
    def test_tenants_example(self):
        companies = Company.objects.all()
        ...
```

The expected behavior for me would be to get all companies, and yet the result was an empty QuerySet. Ok, maybe I need to create some tenant before displaying, logical, let's try.

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        companies = Company.objects.all()
```

This time I got an error

`Cannot get list of tenants while in tenant context, enter public schema.`

I asked myself "What's happening?", but I managed to find somewhere the use of schema_context. So I tried:

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        with schema_context("public"):
            companies = Company.objects.all()
```

Great, this time there's no error. Anyway, the companies variable is still an empty QuerySet. Last attempt:

```python
class TenantsTestCase(BaseTenantTestCase):
    def setUp(self):
        with schema_context("public"):
            Company.objects.create(name="Test company", schema_name="test_schema")
    def test_tenants_example(self):
        with schema_context("public"):
            companies = Company.objects.all()
```

Finally, this time I got a QuerySet with two Company objects. But wait, I created one. Time to put it all together.

It turns out that when we run tests with Django-tenants, a new tenant is created with schema_name "test" and all queries are performed against this schema unless we switch it. (O: At least in our case, because we use FastTenant case -> otherwise tenants are created e.g. per TestCase, which takes time because migrations are applied per tenant etc.)

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

Now remember that Company, which is our tenant object, is stored in the "public" schema, so the empty QuerySets we got earlier were correct because we were trying to find the Company object in schemas that don't contain them. Going further, creating a Project object must take place in the context of a specific tenant's schema because that's where its tables are stored.

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

For me, working with tenants resolves around tracking how the context changes to always know what queries I can perform and what effects to expect.

### Old-timer's Perspective
Ok. Enough from Dominik's perspective. Now it's my turn. I'll give you a bit of insight from a broader perspective. What you've read so far is Dominik's understanding of the tenant concept and how we used it at thirty3. It's more or less correct, some things are oversimplified, but the general idea is somewhere there. I'm a bit proud of him, it took me much longer to understand certain things. Enough patting on the back. Now I'll try to give you more information about the decision-making process we had when we started using tenants, why we use them and why you might want to do it too.

Let's start.

#### What are tenants?
First thing - tenants. What is this? It's a concept, most often used in e.g. SaaS products, that simplifying a bit, they are like your clients. At least that's how I like to think about it. Something like when instead of creating a custom solution for a given Company, which is used only by that company, you create a general solution where the company is just like a user.

Some things are defined globally in the DB and shared between users/companies, other things are defined and should be available only to that specific Company and so on. In a normal case, when only that company will use the application, you don't have to think about it much. The problem arises when you want to globalize this application and have many companies. All of them have some private data, some public. This data should be separated and unavailable to other companies using the given SaaS. You need another layer of abstraction that logically ties or encapsulates this company data. Aw shiet, here go tenants. What are other benefits?

#### SaaS Scaling
As time passes and our applications develop, when you start getting clients who aren't your closest family or investors, things start to get complicated. Privacy suddenly becomes important. Data breaches/leaks are costly. Then the product starts gaining traction, your user base grows, optimization becomes a problem. This happens in almost every successful product.

It's good to think about these problems and prepare for them, but only as much as needed, so as not to over-engineer. In our case, in most cases, we decided to use the Tenant pattern for this purpose, using DB schemas to implement the plan. Thanks to this, it's harder for all clients' data to leak or for one client to get access to another client's sensitive data, easier to scale our application, without overburdening our working time.

#### Database Scaling Methods
What is the factor that most often limits us, at least in most applications? DB. What are the ways to scale DB? Horizontal and vertical. Vertical means you have one DB, to which you simply throw more resources - better hardware. Such scaling has its limits. When you hit them, no matter how much money you have - that's it. Can you do something about it?

This is where horizontal scaling comes to the rescue, i.e. using more machines/DBs instead of one. However, this is quite tricky - just putting up a second DB next to it won't do anything. Suddenly things like master-slave patterns, data consistency, node networks and so on come into play. Quite a complex topic in my opinion.

Of course, this method also has limitations, but often they are much greater than the limitations of a vertically scaled system. So yes - managing tenants in a SaaS-like product can be done in many different ways. The first is DB per client. Here we would probably have one larger DB with globally shared things in the application, and then smaller (or larger) DBs with data unique to the client.

The second is Schema per client, i.e. one database with like 'mini databases' inside.

The third is custom permissions and relationships in tables, for example with all clients' data placed in one schema, one db.

The first is costly and troublesome to manage on a smaller scale.

The third often ends up with messy DB tables, privacy concerns and permission nightmare.

The second however... Well, it almost doesn't impose costs on the situation where you would have a regular single schema/DB architecture - it's not a SaaS architecture, but it facilitates scaling and separating client data through DB abstraction - instead of having many DBs which are troublesome to manage, it uses one DB as if there were "many", at least in some sense.

That's why we decided on this solution. And honestly, we're quite happy with the results.

A big advantage of tenants is also the fact that queries remain simple. Query for invoices only from a given company? Just set the appropriate tenant context and that's it.

#### Different Tenant Management Methods
The so-called search path, which we set for Postgres queries using our db router, can be set in many ways. The traditional tenant pattern uses subdomains as a way to identify tenant- e.g. x.myproduct.com will look up tenant x. That's one way. Remember to prevent users from registering tenants with names of commonly used subdomains e.g.` ftp, mail, static` and so on, otherwise you might be in for an unpleasant surprise. Also remember to have certificates that have a wildcard for subdomains - otherwise you'll be without SSL for your tenants' subdomains, which is quite bad.

Another solution is for example to put it as part of the url, but not a subdomain. For example:`api.example.com/v1/tenant/someendpoint`. We used the latter.

#### What Tenants Gave Us
We achieved:

1. zero additional costs of managing additional infra
2. zero additional infra
3. ease of scaling -> change the way of setting the search path for db router and done, horizontal scaling in three minutes
4. client data is logically separated from each other
5. queries remain simple, same as permissions and tables

Anyway. Plus minus that's how tenants look and work.

PS: minuses of having me as a mentor - you'll probably start writing.

## ORM

What is ORM? Well, a few words about this useful tool.

### What is ORM?

ORM, or Object-Relational Mapping. Such a tool that converts SQL values into Python objects that are easier to handle, using appropriate 'classes' or 'mappings'. It's a collection of useful methods, conveniences and abstractions.

### ORM vs Pure SQL

The difference between ORM and the traditional approach where we write pure SQL ourselves is diametrical.

#### More Abstraction

The first difference will be the fact that ORM hides many things from us, providing a layer of abstraction above SQL itself. It does this at the cost of performance and at the cost of assuming that the programmer knows how ORM works, as their creators make certain decisions for us. These decisions affect how ORM works and how it creates queries. Sometimes not knowing them can make us shoot ourselves in the foot, unknowingly. Ignorance can sometimes hurt. Plus that performance.

#### Lower Performance

It's not some enormous overhead, but with complex queries you'll probably have to resort to writing pure SQL. It might also turn out that something that takes a minute in pure SQL, in ORM, due to e.g. the unusual nature of the problem, might take hours. And vice versa. It happens.

#### Still Worth It

Nevertheless, for most, the vast majority, which includes you, because otherwise you wouldn't be reading this book, ORM will be a significant convenience. However, as I always do, I must point out that it's worth knowing and knowing at least the basics of SQL and knowing how ORM works under the hood, at least very very superficially.

#### Debugging/Profiling ORM

ORM is additionally harder to debug and profile - queries are generated by the engine, often they can be not very friendly when it comes to readability, for humans plus somewhat non-optimal when it comes to performance. Again, for 99% of cases it won't matter, because a query returning a list of users will be just as simple here and there.

#### Serialization from/to Python Objects

ORM also provides us with a layer of abstraction in the form of mapping data from the database to Python objects. Data serialization and also their validation. In the case of writing SQL queries manually, it often becomes your responsibility to check if the data is correct, their interpretation or conversion. If it's about ORM, it either provides a range of tools that help us with this or even takes care of it for us. Something nice.

### Summary

ORM is simply a form of abstraction and simplification of database interaction from the level of a given language. It has its advantages and disadvantages, you need to know them to make a conscious choice. In 95% of cases it will make your life easier, but the remaining 5% is probably beyond the scope of this book intended for junior wannabes.

\pagebreak 