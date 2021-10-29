def is_sorted(t):
    if t == sorted(t):
        return True
    else:
        return False
print(is_sorted([1,3,5,6,8,3]))