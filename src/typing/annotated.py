from typing import Annotated


def greet(name: Annotated[str, "The name to greet"]) -> str:
    return f"Hello, {name}!"
