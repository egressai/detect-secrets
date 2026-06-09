"""
This plugin searches for Azure storage connection strings.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class AzureConnectionStringDetector(RegexBasedDetector):
    """Scans for Azure connection strings that contain account keys."""
    secret_type = 'Azure Connection String'

    denylist = (
        re.compile(
            r'DefaultEndpointsProtocol=https?;'
            r'AccountName=[^;\s\'"]+;'
            r'AccountKey=[^;\s\'"]+;'
            r'EndpointSuffix=[^;\s\'"]+',
            flags=re.IGNORECASE,
        ),
    )
