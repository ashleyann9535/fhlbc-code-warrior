#Code Warriors - https://www.codewars.com

#Green Glass Door
def step_through_with(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True

    return False

# print(step_through_with('moon')) #True
# print(step_through_with('sun')) #False
# print(step_through_with('test')) #False

#How Green Is My Valley?
def make_valley(arr):
    right = []
    left = []

    arr_sort = sorted(arr, reverse=True)

    for index, val in enumerate(arr_sort):
        if index % 2 != 0:
            left.append(val)
        else:
            right.insert(0,val)

    left.extend(right)

    return left

print(make_valley([79, 35, 54, 19, 35, 25])) #[79, 35, 25, *19*, 35, 54]
print(make_valley([67, 93, 100, -16, 65, 97, 92])) #[100, 93, 67, *-16*, 65, 92, 97]
