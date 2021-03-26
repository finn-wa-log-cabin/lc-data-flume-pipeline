from datetime import datetime
from typing import Dict, List

from shared.utils.files import *
from shared.utils.time import timestamp

from InsertSummary import insert_summary

SAMPLES_PATH = "test/InsertSummary/samples/"


def test_insert_summary():
    request_str = load_text(SAMPLES_PATH + "request.json")
    data_str = load_text(SAMPLES_PATH + "data.json")
    summaries_str = insert_summary.main(request_str, data_str)
    summaries: List[Dict] = json.loads(summaries_str)
    assert len(summaries) == 3
    assert summaries[0]["RowKey"] == "20200101"
    assert summaries[0]["startTimestamp"] == timestamp(
        datetime(year=2020, month=1, day=1)
    )
    assert summaries[1]["RowKey"] == "20200201"
    assert summaries[1]["startTimestamp"] == timestamp(
        datetime(year=2020, month=2, day=1)
    )
    assert summaries[2]["RowKey"] == "20200301"
    assert summaries[2]["startTimestamp"] == timestamp(
        datetime(year=2020, month=3, day=1)
    )
    for summary in summaries:
        assert summary["customerID"] == "TestCustomer1"
        assert summary["deviceID"] == "TestDevice1"
        assert summary["timespan"] == "MONTHLY"
        assert summary["PartitionKey"] == "TestCustomer1_TestDevice1_MONTHLY"
