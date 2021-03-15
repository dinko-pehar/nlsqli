#!/usr/bin/env python3
"""
The main entry point. Invoke as `nlsqli' or `python3 -m nlsqli'.
"""
import sys

from nlsqli.cli import parser
from nlsqli.core import inject


def main():
    args = vars(parser.parse_args())
    try:
        inject(args)
    except KeyboardInterrupt:
        # Suppress CTRL + C traceback
        sys.exit(1)


if __name__ == '__main__':
    main()
