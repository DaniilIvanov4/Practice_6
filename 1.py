def nested_sum(t):
    s = 0
    for row in t:
        s += sum(row)
    return s

print(nested_sum(([2,3,4,2,1],[5,4,5,3,2])))