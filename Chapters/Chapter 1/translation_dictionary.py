words = {
    "sahayog":"help",
    "kursi":"chair",
    "billi":"cat"
}
word = input("Enter a word to know the meaning: ")
print(words[word])

# Creating an empty dictionary
favorite_languages = {}

# Manually entering names and their favorite languages
for i in range(5):
    name = input("Enter the name of your friend: ")
    language = input(f"Enter {name}'s favorite programming language: ")
    favorite_languages[name] = language

# Printing the dictionary
print("\nFavorite languages dictionary:")
print(favorite_languages)

# Retrieving a particular person's favorite language
person = input("\nEnter the name of the person whose favorite language you want to retrieve: ")

if person in favorite_languages:
    print(f"{person}'s favorite programming language is: {favorite_languages[person]}")
else:
    print(f"No entry found for {person}.")
