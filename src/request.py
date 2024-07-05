from dataclasses import dataclass
from sanic import Sanic, Request
from types import SimpleNamespace

@dataclass
class CustomContext:
    user_id: str = None

class CustomRequest(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx.user_id = self.headers.get("X-User-ID")

    @staticmethod
    def make_context() -> CustomContext:
        return CustomContext()

