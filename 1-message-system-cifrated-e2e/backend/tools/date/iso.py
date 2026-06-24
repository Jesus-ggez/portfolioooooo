from datetime import datetime


def get_now() -> str:
    return datetime.now().isoformat()
