# Two Tables Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

```
```
Nouns:
user account, email address, username
post, title, content, views 
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| user acccount         | email address, username
| post                  | title, content, views, account id

1. Name of the first table: `accounts` 
    Column names: `id`, `username`, `email_address`

2. Name of the second table : `posts` 
    Column names: `title`, `content`, `views`, `account_id`

## 3. Decide the column types

_Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`_

```

Table: accounts
id: SERIAL (PRIMARY KEY)
username: VARCHAR(255)
email_address: VARCHAR(255)

Table: posts
id: SERIAL
title: VARCHAR(255)
content: TEXT
views: INTEGER
account_id: INTEGER FK

```

## 4. Decide on The Tables Relationship

Since one user account can have many posts, the FOREIGN KEY is in the `posts` table 

## 5. Write the SQL

```sql
-- file: seeds/social_network.sql

CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  email_address VARCHAR(255)
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  content TEXT,
  views INTEGER,
  account_id INT,
  CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 blog < social_network.sql
```