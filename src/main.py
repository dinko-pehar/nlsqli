#!/usr/bin/env python3
"""
The main entry point. Invoke as `nlsqli' or `python3 -m nlsqli'.
"""
import sys

from cli import parser
from core import main


if __name__ == '__main__':
    args = vars(parser.parse_args())
    try:
        main(args)
    except KeyboardInterrupt:
        sys.exit(1)

