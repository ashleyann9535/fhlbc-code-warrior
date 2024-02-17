#Source = www.codewars.com

#Friend or Foe
def friend(x):
    friends = filter(lambda name: len(name) == 4, x )
    return list(friends)

def friend_two(x):
    friends_two = [name for name in x if len(name) == 4]
    return friends_two


#print(friend(["Ryan", "Kieran", "Mark"])) #["Ryan", "Mark"]
#print(friend_two(["Ryan", "Kieran", "Mark"])) #["Ryan", "Mark"]

#I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(num):
    phrases = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']

    location = (num % 6) -1

    return phrases[location]

print(how_much_i_love_you(2)) # 'a little
print(how_much_i_love_you(6)) # 'not at all
print(how_much_i_love_you(11))# madly 