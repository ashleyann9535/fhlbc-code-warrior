#Exercise 26 Dictionary Creation Exercise
#Create a dictionary called user_info  and add at least 3 key value pairs to it 
user_info = {
    'username': 'applejack',
    'email': 'apple@testmail.com',
    'password': '****'
}

#Exercise 27 Access Data in a Dictionary Exercise
#Using given dictionary, Declare a variable called full_name  that is equal to artist's first  
# and last  names with a space between. You must reference the values associated with those keys 
# in the artist dictionary.
artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)