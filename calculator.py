def average(lst):
    """Calculate the average of a list of numbers."""
    if not lst:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(lst) / len(lst)
