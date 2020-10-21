import json
from datetime import datetime

from azure.functions import EventGridEvent
from DataPipelineFunctions.Common.time_utils import timestamp


def main(event: EventGridEvent) -> str:
    """
    Receives telemetry from a device, and inserts the data into a table.
    """
    event_time = event.event_time()
    if event_time is None:
        event_time = datetime.utcnow()

    telemetry = json.loads(event.get_json())
    if telemetry["depth"] is None:
        raise TypeError(f"Received telemetry with null depth: {event}")
    telemetry["PartitionKey"] = f"{telemetry['customerID']}_{telemetry['deviceID']}_Raw"
    telemetry["RowKey"] = str(timestamp(event_time))

    return json.dumps(telemetry)
