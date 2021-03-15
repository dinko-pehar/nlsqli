import argparse
from http.cookies import SimpleCookie

from constants import EPILOG

parser = argparse.ArgumentParser(description="Detect and exploit SQL injection flaws",
                                 epilog=EPILOG,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

# At least one parameter is required.
target_args = parser.add_mutually_exclusive_group(required=True)
target_args.add_argument('-u','--url',
                         help='Target URL (e.g. "http://www.site.com/vuln.php?id=1")'
                         )
target_args.add_argument('-m','--multi',
                         help='File for multi values'
                         )

# Optional groups.

# Request group.
request_args = parser.add_argument_group(title="Request",
                                         description="Additional arguments when sending request.")
# TODO: Add and modify this.
request_args.add_argument('-H', '--header',
                          nargs="*", action="append",
                          help='Extra headers (e.g. "X-API-KEY: XXX")')
request_args.add_argument('--method',
                          type=str, default="GET", choices=["GET", "POST", "PUT", "DELETE", "PATCH"],
                          help='Use different HTTP method (e.g. POST)')
request_args.add_argument('--cookies',
                          type=SimpleCookie,
                          help='HTTP Cookies header value (e.g. "PHPSESSID=a8d127e;sec=low")')
request_args.add_argument('--timeout',
                          type=str, default=30,
                          help='Seconds to wait before timeout connection (default 30)')
# TODO: Include this.
request_args.add_argument('-f', '--form',
                          action="store_true", default=False,
                          help='Submit a form with data')
request_args.add_argument('-a', '--auth',
                          type=str,
                          help='Pass a username:password pair for Basic Auth.')
# TODO: Include this.
request_args.add_argument('--data',
                          type=str,
                          help='POST data (e.g. "query=test")')
# Style group.
# TODO
request_args = parser.add_argument_group(title="Style",
                                         description="Style output ...")
