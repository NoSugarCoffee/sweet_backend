from datetime import datetime, timezone, timedelta


def get_current_timestamp_CST():
    return datetime.now(tz=timezone(timedelta(hours=8)))