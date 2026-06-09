"""
This plugin searches for Hugging Face access tokens.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class HuggingFaceTokenDetector(RegexBasedDetector):
    """Scans for Hugging Face access tokens."""
    secret_type = 'Hugging Face Token'

    denylist = (
        re.compile(r'hf_[A-Za-z0-9]{34,}'),
    )
