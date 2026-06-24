from datetime import datetime


def get_now() -> int:
    return int( datetime.now().timestamp() )
