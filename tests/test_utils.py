from datetime import datetime, timedelta, timezone

from atoma.utils import try_parse_date


def test_try_parse_date():
    expected = datetime(
        2018, 11, 30, 17, 0, tzinfo=timezone(timedelta(seconds=32400))
    )
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 +0900') == expected

    assert try_parse_date('Fri, 30 Nov 2018 17:00:00:00 +0900') is None

    expected = datetime(2018, 11, 30, 17, 0, tzinfo=timezone.utc)
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00 PST') == expected
    assert try_parse_date('Fri, 30 Nov 2018 17:00:00') == expected

    expected = datetime(2018, 10, 10, 18, 0, tzinfo=timezone.utc)
    assert try_parse_date('Web, 10 Oct 2018 18:00:00 +0000') == expected
