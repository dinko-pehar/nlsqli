<p align="center">
  Small SQL Injection CLI written in Python <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python" width="16" height="16">
</p>

---

[![asciicast](https://asciinema.org/a/rBGyb07vchT86Leo4skGhMJ8A.svg)](https://asciinema.org/a/rBGyb07vchT86Leo4skGhMJ8A)

## Installation

### Docker

Easiest way to run this project is to build docker image in root of a project:

```shell
docker build -t nlsqli .
```

Than, you can run image as:

```shell
docker run --rm -it nlsqli --help
```

where *nlsqli* is example SQLi tool.

### Manual

Depending on platform, you can create virtualenv for Python:

```shell
python3 -m venv venv
```

and activate it:

```shell
source venv/bin/activate
```

Then, run:

```shell
pip install .
```

Last step is to copy `data` folder to `/tmp`:

```shell
cp -r data /tmp
```

Run:

```shell
nlsqli --help
```

to check if it's installed successfully.

## Usage

To use this tool, only required parameter is *URL*:

```shell
nlsqli -u 'http://example.com/path/to?q=3&s=4'
# OR
nlsqli --url 'http://example.com/path/to?q=3&s=4'
```

It will inject payloads at query arguments (*q and s in case above*)

You can authenticate (*if needed*) using [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) as:

```shell
nlsqli -u 'http://example.com/path/to?q=3' --auth 'username:password'  
```

or use Session Cookies (*Open Developer tools and in console run `document.cookie` to retrieve it*):

```shell
nlsqli --url 'http://example.com/path/to?q=3' --cookie 'PHPSESSID=rj77s7nkq8plslmkg8l8e73d94; security=low'  
```

By default, HTTP Request method is `GET` which you can also change:


```shell
nlsqli -u 'http://example.com/path/to?q=3' --auth 'username:password' --method 'DELETE'
```

## Results

You should see output of payloads which are injected and if any SQLi flaws are triggered as:

```text
================================== Running... ==================================
Received: http://localhost/vulnerabilities/sqli/ and query string: {'id': '1', 
'Submit': 'Submit'}
Found 2 query string arguments.
Request Method set to: GET
Request Timeout set to: 30
Request Headers set to: None
Request Data set to: None
Request Cookies set to: Set-Cookie: PHPSESSID=rj77s7nkq8plslmkg8l8e73d94
Set-Cookie: security=low
Request Auth set to Basic: None
───────────────────────────────── Injecting ... ────────────────────────────
 (INFO) Injecting: ' into id
 (WARNING) parameter id appears to be error SQLi vulnerable (MariaDB)
 (INFO) Injecting: ' into Submit
 (INFO) Injecting: '' into id
 (INFO) Injecting: '' into Submit
 (INFO) Injecting: ` into id
 (INFO) Injecting: ` into Submit
 (INFO) Injecting: `` into id
 (INFO) Injecting: ' or " into id
 (WARNING) parameter id appears to be error SQLi vulnerable (MariaDB)
 ...

```

## Other

Only tested on `dvwa`.

Run in a detached mode and same network:

```shell
docker run -d -p 80:80 --name dvwa --net test_network vulnerables/web-dvwa
```

set database and security to low and pass URL along with a cookie to check the output:

```shell
nlsqli --url 'http://dvwa/vulnerabilities/sqli/?id=2&Submit=Submit' --cookie 'PHPSESSID=rj77s7nkq8plslmkg8l8e73d94; security=low'
```

### Research:

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

### TODO:


- [ ] Add flake8 and black configs
- [x] Create CLI
- [x] Modularize it
- [x] Research SQL injection payloads
- [ ] Add CI/CD integration (GitHub Actions)
- [x] **Document code**
- [x] **Create docker build**
- [ ] ~~Accept from a file multiple URLs~~
- [x] ~~Unit test argparser~~ (Partial)
- [x] Create rich interface
- [x] Move payloads to where they belong inside packages in Unix
- [x] Add types (PARTIAL)
- [x] Create `setup.py` for installer
- [ ] ~~Add export to JSON or CSV~~
- [ ] Support `asyncio` model
- [ ] Along with query string and form data, add HTTP parameter pollution
- [ ] Count errors
- [ ] Add `Makefile`
