"""
Response Class to generate data
"""
from typing import Any

from fastapi import Response


class RT:
    @classmethod
    def error_response(cls, error_message="") -> dict:
        return dict(
            code=500,
            message=error_message
        )

    @classmethod
    def true_response(cls, data: Any = None, message: str = "") -> dict:
        return dict(
            data=data,
            code=200,
            message=message
        )
