"""
Module for extending arguments provided from CLI.
"""
import argparse
from http.cookies import SimpleCookie

from nlsqli.utils import URLParserType, parse_data
from nlsqli.constants import EPILOG

parser = argparse.ArgumentParser(description="Detect and exploit SQL injection flaws",
                                 epilog=EPILOG,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

# Required arguments.
required_args = parser.add_argument_group(title="Required arguments")
required_args.add_argument('-u','--url',
                           type=URLParserType, required=True,
                           help='Target URL (e.g. "http://www.site.com/vuln.php?id=1")'
                           )

# Optional groups.

# Request group.
request_args = parser.add_argument_group(title="Request arguments",
                                         description="Additional arguments when sending request.")
request_args.add_argument('--method',
                          type=str, default="GET", choices=["GET", "POST", "PUT", "DELETE", "PATCH"],
                          help='Use different HTTP method (e.g. POST)')
request_args.add_argument('--timeout',
                          type=int, default=30,
                          help='Seconds to wait before timeout connection (default 30s)')
# TODO: Not working as expected, list in list ?
request_args.add_argument('-H', '--header',
                          type=str,
                          nargs="*", action="append",
                          help='Extra headers (e.g. -H "Connection: Keep-Alive"'
                               '-H "ETag: 737060cd8c284d8af7ad3082f209582d"')
request_args.add_argument('--cookies',
                          type=SimpleCookie,
                          help='HTTP Cookies header value (e.g. --cookies "PHPSESSID=a8d127e;sec=low")')
request_args.add_argument('-a', '--auth',
                          type=str,
                          help='Pass a username:password pair for Basic Auth.')
request_args.add_argument('--data',
                          type=parse_data,
                          help='Form data (e.g. "id=4&Submit=Submit")')
