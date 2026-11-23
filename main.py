from pathlib import Path

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")
ENTRY = "Sorry I'm late: I finished on time, then promoted myself to manager and spent the deadline approving my own work."


def validate_entry(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} characters")
    return text


def write_entry(path: Path | None = None) -> Path:
    target = OUTPUT_PATH if path is None else Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(validate_entry(ENTRY).encode("utf-8"))
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
