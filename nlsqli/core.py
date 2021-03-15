"""
Core module; everything in here defines whole project workflow.
"""
import copy
import re
import sys
import time

import requests

from nlsqli.constants import PAYLOADS_PATH, DBMS_ERRORS
from nlsqli.utils import retrieve_payloads, console


def analyze_output(req, query_id):
    """Search response for successful injection."""

    # Search for standard errors defined by databases.
    for db_name in DBMS_ERRORS.keys():

        for error_regex in DBMS_ERRORS.get(db_name):

            # Case insensitive search on response.
            if re.search(error_regex, req.text, re.I):
                time.sleep(.01)
                console.print(f" [bold red](WARNING)[/bold red] parameter"
                              f" [u cyan]{query_id}[/u cyan]"
                              f" appears to be error SQLi vulnerable ({db_name})")
                return True

    return False

def send(session: requests.Session, query_string: dict, payload: str, *,
         method: str = '', url: str = '', timeout: int = 0):
    """Send prepared request with malicious payload."""

    # Copy by value (don't modify original query string).
    params = copy.deepcopy(query_string)

    for key, val in params.items():
        params[key] = payload  # Change query argument to injection.

        req = session.request(method=method,
                              url=url,
                              timeout=timeout,
                              params=params,
                              data={})

        if analyze_output(req, key):
            console.print(f" ---> Payload: {payload}")
        params[key] = val  # Retain original value.


def inject(args):
    """Execute all sorts of injections."""
    console.rule("Running...", characters="=")

    url, query_string = args.get("url")
    method = args.get('method')
    timeout = args.get('timeout')
    headers = args.get('header')
    data = args.get('data')
    cookies = args.get('cookies')
    auth = args.get('auth')

    if data is None and len(query_string) == 0:
        console.print(f"Found [bold red]{len(query_string)}[/bold red] query string"
                      f" arguments and form data is set to: {data}\nExiting...")
        sys.exit(1)

    console.print(f"Received: {args.get('url')}")
    console.print(f"Found [bold red]{len(query_string)}[/bold red] query string arguments.")
    console.print(f"Request [u cyan]Method[/u cyan] set to: {method}")
    console.print(f"Request [u cyan]Timeout[/u cyan] set to: {timeout}")
    console.print(f"Request [u cyan]Headers[/u cyan] set to: {headers}")
    console.print(f"Request [u cyan]Data[/u cyan] set to: {headers}")
    console.print(f"Request [u cyan]Cookies[/u cyan] set to: {cookies}")
    console.print(f"Request [u cyan]Auth[/u cyan] set to Basic: {auth}")

    time.sleep(1)

    with requests.Session() as session:

        if cookies:  # Update cookies if provided.
            session.cookies.update(cookies)

        if auth:  # Should be basic auth e.g. username:password.
            session.auth = tuple(auth.split(':'))

        # TODO: Fix headers casting to dictionary.
        # if headers:
        #     session.headers.update(headers)

        console.rule("Injecting ...")

        # Load payloads and replace them with values from provided query string.
        for payload_path in PAYLOADS_PATH.rglob('*.txt'):
            payloads = retrieve_payloads(payload_path)

            for payload in payloads:

                # TODO: Add headers and data.
                send(session, query_string, payload,
                     method=method, url=url, timeout=timeout)
