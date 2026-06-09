import pytest

from detect_secrets.plugins.database_url import DatabaseUrlDetector


class TestDatabaseUrlDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            ('postgres://admin:password@prod.internal:5432/app', True),
            ('DATABASE_URL="postgresql://admin:p%40ss@localhost/app"', True),
            ('mongodb+srv://user:password@cluster0.example.mongodb.net/app', True),
            ('redis://:password@localhost:6379/0', True),
            ('postgres://prod.internal:5432/app', False),
            ('https://user:password@example.com', False),
        ],
    )
    def test_analyze(self, payload, should_flag):
        logic = DatabaseUrlDetector()
        output = logic.analyze_line(filename='mock_filename', line=payload)

        assert len(output) == int(should_flag)
