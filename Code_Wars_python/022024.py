#Friend or Foe
def friend(x):
    friends = filter(lambda name: len(name) == 4, x )
    return list(friends)

def friend_two(x):
    friends_two = [name for name in x if len(name) == 4]
    return friends_two


print(friend(["Ryan", "Kieran", "Mark"])) #["Ryan", "Mark"]
print(friend_two(["Ryan", "Kieran", "Mark"])) #["Ryan", "Mark"]