#Code Warriors - https://www.codewars.com

#Green Glass Door
def step_through_with(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True

    return False

print(step_through_with('moon')) #True
print(step_through_with('sun')) #False
print(step_through_with('test')) #False