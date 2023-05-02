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

#Exercise 28 Totaling Donations Exercise
# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!
# Use a loop to add together all the donations and store the resulting number 
# in a variable called total_donations
total_donations = 0
for value in donations.values():
    total_donations += value
print(total_donations)