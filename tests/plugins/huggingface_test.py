import pytest

from detect_secrets.plugins.huggingface import HuggingFaceTokenDetector


VALID_HUGGING_FACE_TOKEN = 'hf_' + 'a' * 34


class TestHuggingFaceTokenDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            (VALID_HUGGING_FACE_TOKEN, True),
            ('HUGGINGFACE_TOKEN={}'.format(VALID_HUGGING_FACE_TOKEN), True),
            ('hf_short', False),
            ('ghp_abcdefghijklmnopqrstuvwxyzABCDEFGH', False),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = HuggingFaceTokenDetector()
        output = logic.analyze_line(filename='mock_filename', line=payload)

        assert len(output) == int(should_flag)
