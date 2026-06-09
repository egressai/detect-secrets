import pytest

from detect_secrets.plugins.azure_connection_string import AzureConnectionStringDetector


class TestAzureConnectionStringDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            (
                'DefaultEndpointsProtocol=https;AccountName=acct;'
                'AccountKey=abcdefghijklmnopqrstuvwxyz0123456789+/==;'
                'EndpointSuffix=core.windows.net',
                True,
            ),
            (
                'AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;'
                'AccountName=acct;AccountKey=abcdefghijklmnopqrstuvwxyz0123456789+/==;'
                'EndpointSuffix=core.windows.net"',
                True,
            ),
            ('DefaultEndpointsProtocol=https;AccountName=acct;EndpointSuffix=core.windows.net', False),
            ('AccountKey=abcdefghijklmnopqrstuvwxyz0123456789+/==', False),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = AzureConnectionStringDetector()
        output = logic.analyze_line(filename='mock_filename', line=payload)

        assert len(output) == int(should_flag)
