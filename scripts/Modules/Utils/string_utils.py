def shout(text: str) -> str:
    """Convert the input text to uppercase and add an exclamation mark."""
    return text.upper() + "!"

def whisper(text: str) -> str:
    return text.lower() + "_"

__all__ = ["shout"]