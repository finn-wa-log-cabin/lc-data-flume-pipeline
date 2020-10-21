from datetime import datetime, timedelta

import DataPipelineFunctions.Common.time_utils as time_utils
from dateutil.tz.tz import tzoffset
from dateutil import tz


def test_timestamp_nzdt():
    nzdt = tzoffset("NZDT", timedelta(hours=13).seconds)
    dt = datetime(2009, 2, 14, 12, 31, 31, 11000, tzinfo=nzdt)
    assert time_utils.timestamp(dt) == 1234567891011


def test_timestamp_utc():
    dt = datetime(2009, 2, 13, 23, 31, 31, 11000, tzinfo=tz.UTC)
    assert time_utils.timestamp(dt) == 1234567891011


def test_start_of_day_nzdt():
    nzdt = tzoffset("NZDT", timedelta(hours=13).seconds)
    dt = datetime(2009, 2, 13, 1, 1, 1, 11000, tzinfo=nzdt)
    assert time_utils.start_of_day(dt) == datetime(2009, 2, 13, tzinfo=nzdt)


def test_start_of_day_no_tz():
    dt = datetime(2009, 2, 13, 1, 1, 31, 11000)
    assert time_utils.start_of_day(dt) == datetime(2009, 2, 13)
