def is_number_in_bounds(n: str, left: int, right: int):
    try:
        n = int(n)
        return left <= n <= right
    except Exception:
        return False