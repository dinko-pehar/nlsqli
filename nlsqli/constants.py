from pathlib import Path

EPILOG="""
------------------

Example usage:
                                
...
"""

PAYLOADS_PATH = Path('/tmp/data/payloads')

# Standard error codes defined by databases.
# This could be expanded, but time is money...
DBMS_ERRORS = {
    "MariaDB": ["MariaDB", "error in your SQL syntax.*MariaDB"],
    "MySQL": [r"SQL Syntax.*MySQL", r"valid MySQL result"],
    "PostgreSQL": ["PostgreSQL"]
}
