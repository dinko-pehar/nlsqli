from urllib.parse import urlparse, parse_qs
from collections.abc import Iterator

from rich.console import Console

console = Console()


class URLParserType:
    """Type handler to split URL and query strings."""

    def __init__(self, url: str):
        self.url = self.qs = url

    @property
    def url(self) -> str:
        """Retrieve URL stripped from Query arguments.

        Returns:
            str: URL without query arguments or fragments.
        """
        return self._url

    @url.setter
    def url(self, val: str):
        # Although _replace private method is called, it's recommended for changing
        # ParseResult class by documentation:
        # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
        self._url = urlparse(val, allow_fragments=False)._replace(query=None).geturl()

    @property
    def qs(self) -> dict:
        """Retrieve Query arguments.

        Returns:
            dict: Mappings of query argument name and their values.
        """
        return self._qs

    @qs.setter
    def qs(self, val: str):
        _query = parse_qs(urlparse(val).query, keep_blank_values=False)
        self._qs = {k: v.pop() for k, v in _query.items()}

    def __iter__(self) -> Iterator[str, dict]:
        return iter([self.url, self.qs])

    def __str__(self) -> str:
        return f"URLParser with URL: {self.url} and query string: {self.qs}"

    def __repr__(self) -> str:
        return f"URLParser: <URL -> {self.url} , Query -> {self.qs}>"


def retrieve_payloads(payload_path):

    with open(payload_path, mode="r", encoding="utf-8") as fp:
        return fp.readlines()


def parse_headers(headers) -> dict:
    """Convert headers argument to dictionary."""

    _headers = dict()

    if headers:
        for header in headers:
            # Header should be string as "X-API-Key:3"
            # NOTE: Not going to test input, assume it for now.
            key, val = header.pop().replace(' ', '').split(':')
            _headers[key] = val

    return _headers
