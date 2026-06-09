import pytest

from detect_secrets.plugins.anthropic import AnthropicDetector


class TestAnthropicDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            ('sk-ant-api03-abcdefghijklmnopqrstuvwxyzABCDEF1234567890', True),
            ('sk-ant-abcdefghijklmnopqrstuvwxyzABCDEF1234567890', True),
            ('sk-ant-api03-short', False),
            ('sk-proj-abcdefghijklmnopqrstuvwxyzABCDEF1234567890', False),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = AnthropicDetector()
        output = logic.analyze_line(filename='mock_filename', line=payload)

        assert len(output) == int(should_flag)
