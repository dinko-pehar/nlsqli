import copy
import sys

import requests
from rich.progress import track

from constants import PAYLOADS_PATH
from utils import retrieve_payloads, console, parse_headers


def analyze_output(req):
    # TODO: Figure out how to analyze output?
    if "MariaDB" in req.text:
        return True


def send(session, query_string, payload, *,
         method='', url='', timeout=0, data=None):
    # Copy by value (don't modify original query string).
    params = copy.deepcopy(query_string)

    for key, val in params.items():
        params[key] = payload  # Change query argument to injection.

        req = session.request(method=method,
                              url=url,
                              timeout=timeout,
                              params=params,
                              data={})

        if analyze_output(req):
            console.log(f"Parameter {key} seems to be SQLi vulnerable.")

        params[key] = val  # Retain original value.


def main(args):
    console.rule("Running...", characters="=")

    url, query_string = args.get("url")
    method = args.get('method')
    timeout = args.get('timeout')
    headers = parse_headers(args.get('header'))
    data = args.get('data')
    cookies = args.get('cookies')
    auth = args.get('auth')

    if data is None and len(query_string) == 0:
        console.print(f"Found [bold red]{len(query_string)}[/bold red] query string"
                      f" arguments and form data is set to: {data}\nExiting...")
        sys.exit(1)

    console.print(f"Received URL: {args.get('url')}")
    console.print(f"Found [bold red]{len(query_string)}[/bold red] query string arguments.")
    console.print(f"Request [u cyan]Timeout[/u cyan] set to: {timeout}")
    console.print(f"Request [u cyan]Headers[/u cyan] set to: {headers}")
    console.print(f"Request [u cyan]Method[/u cyan] set to: {method}")
    console.print(f"Request [u cyan]Cookies[/u cyan] set to: {cookies}")
    console.print(f"Request [u cyan]Auth[/u cyan] set to Basic: {auth}")

    with requests.Session() as session:

        if cookies:  # Update cookies if provided.
            session.cookies.update(cookies)

        if auth:  # Should be basic auth e.g. username:password.
            session.auth = tuple(auth.split(':'))

        if headers:
            session.headers.update(headers)

        console.rule("Injecting ...")

        for payload_path in PAYLOADS_PATH.rglob('*.txt'):
            payloads = retrieve_payloads(payload_path)

            for payload in track(payloads, description=f"Injecting from {payload_path} payloads..."):
                send(session, query_string, payload,
                     method=method, url=url, timeout=timeout)
