def add_one(n):
    """Adds 1 to the given parameter."""
    n += 1
    return n  # Return the new value
num = 9
print("Before calling add_one:", num)

num = add_one(num)
print("After calling add_one:", num)
