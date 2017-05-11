def selfPowers():
    total = 0
    for i in range(1, 1000):
        total += i ** i
    
    return total

print(str(selfPowers())[-10:])