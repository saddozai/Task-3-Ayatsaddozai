
# PROJECT 3 - Ai recommendation system
# DecodeLabs Internship

#dataset

movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr Bean", "The Mask", "Home Alone"],
    "horror": ["Conjuring", "Annabelle", "Insidious"],
    "sci-fi": ["Interstellar", "Avatar", "Inception"]
}

#header

print("Welcome to Decodelabs ")
print(" AI Movie Recommendation System ")
print("=================================")


print("\nAvailable Categories:")
for category in movies:
    print("-", category.title())

user_choice = input("\nEnter your favorite category: ").lower()
if user_choice in movies:

    print("\nRecommended Movies:")
    for movie in movies[user_choice]:
        print("-", movie)

else:
    print("\nSorry! Category not found.")
print("\nThank You For Using The System!")