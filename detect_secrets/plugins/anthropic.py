"""
This plugin searches for Anthropic API keys.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class AnthropicDetector(RegexBasedDetector):
    """Scans for Anthropic API keys."""
    secret_type = 'Anthropic API Key'

    denylist = (
        re.compile(r'sk-ant-(?:api\d{2}-)?[A-Za-z0-9_-]{32,}'),
    )
