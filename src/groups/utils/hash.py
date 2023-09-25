import hashlib
from typing import Any


def hash_sha256(value: Any) -> str:
    return hashlib.sha256(value.encode()).hexdigest()
