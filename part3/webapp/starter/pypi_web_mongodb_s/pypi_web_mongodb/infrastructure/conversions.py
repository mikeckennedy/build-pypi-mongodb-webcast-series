from typing import Optional


def try_int(text: str, default: Optional[int] = None) -> Optional[int]:
    try:
        return int(text)
    except:
        return default
