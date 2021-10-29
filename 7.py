def has_duplicates(s):
    if len(set(s)) < len(s):
        return True
    return False


print(has_duplicates([1,2,3,4,5,1]))#True
print(has_duplicates([1,2,3,4,5,6]))#False
print(has_duplicates('absnjeogpb'))#True
