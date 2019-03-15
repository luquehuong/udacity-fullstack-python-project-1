# Udacity Fullstack Python Project 1

#### Project Description
> In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

#### Prerequired
A Vagrant box (Ubuntu OS) up and running within Postgresql installed

#### Setup database
1. Redirect to root project directory
2. Run `vagrant ssh`
3. Import data to `news` database `psql -d news -f newsdata.sql`
4. Create a new Postgresql account within username equals `vagrant` and password `vagrant`
5. Set permission for user `vagrant` to `news` database

#### Run script
Redirect to root project and run `python reporting_tool.py`
