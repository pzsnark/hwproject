def some(*ars):
    result = 0
    for a in ars:
        result += a
    return result


print(some(1, 4, 6))
