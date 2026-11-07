DEFAULT_STALE_AFTER_SECONDS = 2.0


def is_stale(
    updated_at: float,
    now: float,
    stale_after: float = DEFAULT_STALE_AFTER_SECONDS,
) -> bool:
    if stale_after < 0:
        raise ValueError("Stale threshold must not be negative")
    return now - updated_at > stale_after
