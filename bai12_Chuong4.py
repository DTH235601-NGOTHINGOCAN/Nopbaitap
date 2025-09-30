
def oscillate(start, count):
    x = abs(start)
    sign = -1 if start < 0 else 1
    for _ in range(count * 1):
        yield sign * x
        sign *= -1
        if sign > 0:
            x += 1

# Chạy thử
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
