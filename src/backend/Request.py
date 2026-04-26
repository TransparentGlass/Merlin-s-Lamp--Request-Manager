from dataclasses import dataclass

@dataclass
class Request:
    title: str
    request_type: str
    content: str
    date: str
    author: str
    requestID: int = None