import pytest

from detect_secrets.plugins.google_api_key import GoogleApiKeyDetector


class TestGoogleApiKeyDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            ('AIzaSyD9W7gK0QaBCDEFGHIJKLMNOpqrstuv12345', True),
            ('GOOGLE_API_KEY=AIzaSyD9W7gK0QaBCDEFGHIJKLMNOpqrstuv12345', True),
            ('AIzaSyD9W7gK0QaBCDEFGHIJ', False),
            ('AIza invalid google key', False),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = GoogleApiKeyDetector()
        output = logic.analyze_line(filename='mock_filename', line=payload)

        assert len(output) == int(should_flag)
