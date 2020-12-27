from main.common.domain.tables.device_telemetry import *
from main.common.domain.messages.raw_telemetry import RawTelemetryMsg
from datetime import datetime

from azure.functions import EventGridEvent
from main.common.utils.time import timestamp

RAW_TELEMETRY = SummaryPeriod("Raw", 0)


def main(event: EventGridEvent) -> str:
    """Receives telemetry from a device, and creates a table row for it.

    Args:
    - event: The event containing the device telemetry.

    Returns: The serialised row to be inserted into the DeviceTelemetry table.
    """
    message: RawTelemetryMsg = RawTelemetryMsg.Schema().loads(event.get_json())

    event_time = event.event_time()
    if event_time is None:
        event_time = datetime.utcnow()

    row = DeviceTelemetry.new(
        timestamp(event_time),
        customerID=message.customerID,
        deviceID=message.deviceID,
        depth=message.depth,
        numReadings=1,
        period=RAW_TELEMETRY,
    )

    return DeviceTelemetry.Schema().dumps(row)