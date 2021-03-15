import copy

import requests
from rich.progress import track

from constants import PAYLOADS_PATH
from utils import URLParser, retrieve_payloads, console


def analyze_output(req):
    # TODO: Figure out how to analyze output?
    if "MariaDB" in req.text:
        return True



def send(session, query_string, payload, *, method='', url='', timeout=0):
    # Copy by value (don't modify original query string).
    params = copy.deepcopy(query_string)

    for key, val in params.items():
        params[key] = payload  # Change query argument to injection.

        req = session.request(method=method,
                              url=url,
                              timeout=timeout,
                              params=params)

        if analyze_output(req):
            console.log(f"Parameter []{key}[] seems to be SQLi vulnerable.")

        params[key] = val  # Retain original value.


def main(args):
    console.rule("Running...", characters="=")
    """

    """

    cookies = args.get('cookies')
    method = args.get('method')
    timeout = args.get('timeout')
    headers = args.get('headers')
    url, query_string = URLParser(args.get("url"))

    console.print(f"Received URL: {args.get('url')}")
    console.print(f"Received URL: {url}")
    console.print(f"Found [bold red]{len(query_string)}[/bold red] query string arguments.")
    console.print(f"Request [u cyan]Timeout[/u cyan] set to: {timeout}")
    console.print(f"Request [u cyan]Headers[/u cyan] set to: {headers}")
    console.print(f"Request [u cyan]Method[/u cyan] set to: {headers}")
    console.print(f"Request [u cyan]Cookies[/u cyan] set to: {cookies}")

    with requests.Session() as session:

        if cookies:  # Update cookies if provided.
            session.cookies.update(cookies)

        console.rule("Injecting ...")

        for payload_path in PAYLOADS_PATH.rglob('*.txt'):
            payloads = retrieve_payloads(payload_path)

            for payload in track(payloads, description=f"Injecting from {payload_path} payloads..."):
                send(session, query_string, payload, method=method, url=url, timeout=timeout)
