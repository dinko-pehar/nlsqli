<p align="center">
  Small SQL Injection CLI written in Python <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python" width="16" height="16">
</p>

## Features

## Installation

## Usage



##Other

###Research:

Union-based SQL Injection:

> Union-based SQL Injection represents the most popular type of SQL injection and uses the UNION statement. The UNION statement represents the combination of two select statements to retrieve data from the database.

Error-Based SQL Injection:

> Error with response

Blind SQL Injections:

- Boolean-based SQL Injection
- Time-based

We need to make a list of all input fields which contain values that could be used to generate an SQL query and test them separately, trying to interfere with the query and to produce an error.

Figure out what kind of DB is running in background for more precise exploits

HTTP Header Pollution

Alter, delete and access data

Content-based Blind SQL Injection attacks

Time-based Blind SQL Injection -> Delayed response or heavy operation

###TODO:


- [ ] Add flake8 and black configs
- [x] Create CLI
- [x] Modularize it
- [ ] Research SQL injection payloads
- [ ] Add CI/CD integration (GitHub Actions)
- [ ] **Document code**
- [ ] **Create docker build**
- [ ] ~~Accept from a file multiple URLs~~
- [ ] ~~Unit test argparser~~
- [x] Create rich interface
- [ ] Move payloads to where they belong inside packages in linux
- [ ] Add types
- [ ] Create installer by `setup.py`
- [ ] ~~Add export to JSON or CSV~~
