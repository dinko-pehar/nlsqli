import argparse

import requests
from bs4 import BeautifulSoup

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
request_args.add_argument('-H', '--header',
                          nargs="*",
                          help='Extra headers (e.g. "X-API-KEY: XYZ")')
request_args.add_argument('--method',
                          type=str, default="GET",
                          help='Use different HTTP method (e.g. PUT)')
request_args.add_argument('--cookie',
                          type=str,
                          help='HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")')
request_args.add_argument('--timeout',
                          type=str, default=30,
                          help='Seconds to wait before timeout connection (default 30)')
# Auth dodat


parser.add_argument('-V', '--verbose',
                    choices=[1,2,3], default=1, type=int,
                    help='Verbosity level: 1-3 (default 1)')

if __name__ == '__main__':
    args = vars(parser.parse_args())
    print(args)
