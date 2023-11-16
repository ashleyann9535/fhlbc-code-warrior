#Write a function called intersection. This function should accept two lists and return a list with the values that are in both input lists.
# flesh out intersection pleaseeeee
def intersection(first, second):
    intersect = [value for value in first if value in second]
    return intersect


print(intersection([1,2,3], [2,3,4]))    #[2,3]
print(intersection(['a','b','z'], ['x','y','z']))   # ['z']