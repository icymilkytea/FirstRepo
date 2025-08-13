def high_and_low(numbers):
    l = [int(i) for i in numbers.split(" ")]
    high = l[0]
    low = l[0]
    for i in l:
        if i < low:
            low = i
        if i > high:
            high = i


    result = f"{high} {low}"
    return result

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))