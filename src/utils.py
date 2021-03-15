from urllib.parse import urlparse, parse_qs

from rich.console import Console

console = Console()


class URLParser:

    def __init__(self, url):

        self.url = self.qs = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, val):
        # Although _replace method is called, it's recommended for changing
        # ParseResult class by documentation:
        # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
        self._url = urlparse(val, allow_fragments=False)._replace(query=None).geturl()
        console.print()

    @property
    def qs(self):
        return self._qs

    @qs.setter
    def qs(self, val):
        _query = parse_qs(urlparse(val).query, keep_blank_values=False)
        self._qs = {k: v.pop() for k, v in _query.items()}

    def __iter__(self):
        return iter([self.url, self.qs])

    def __str__(self) -> str:
        return f"URLParser with URL: {self.url} and query string: {self.qs}"

    def __repr__(self) -> str:
        return f"URLParser: <URL -> {self.url} , Query -> {self.qs}>"


def retrieve_payloads(payload_path):

    with open(payload_path, mode="r", encoding="utf-8") as fp:
        return fp.readlines()
