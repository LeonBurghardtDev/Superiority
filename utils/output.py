def print_success(text: str) -> None:
    print(f"\033[32m{text}\033[0m")

def print_error(text: str) -> None:
    print(f"\033[31m{text}\033[0m")