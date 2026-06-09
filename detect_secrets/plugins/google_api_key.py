"""
This plugin searches for Google and Gemini API keys.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class GoogleApiKeyDetector(RegexBasedDetector):
    """Scans for Google API keys, including Gemini API keys."""
    secret_type = 'Google API Key'

    denylist = (
        re.compile(r'AIza[0-9A-Za-z_-]{35}'),
    )
