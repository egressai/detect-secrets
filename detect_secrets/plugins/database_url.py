"""
This plugin searches for database URLs containing inline credentials.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class DatabaseUrlDetector(RegexBasedDetector):
    """Scans for credential-bearing database connection URLs."""
    secret_type = 'Database URL'

    denylist = (
        re.compile(
            r'\b(?:postgres(?:ql)?|mysql2?|mariadb|mongodb(?:\+srv)?|redis|rediss|mssql|'
            r'sqlserver|oracle)://[^\s\'"]*:[^\s\'"]+@[^\s\'"]+',
            flags=re.IGNORECASE,
        ),
    )
