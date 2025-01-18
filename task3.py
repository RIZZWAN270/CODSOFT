print("It's a simple Movie Recommendation System!\n ")
print ("It's a collection of some movie with genre (theme) ,so you can ask want genre you want and we will recommend the movie based upon your theme or your request.\n")
print("If you want to know what genres we have, just type: 'What genres do you have?'\n")

collection = {
    "love": ["Raja Rani", "Joe", "Shajahan", "96"],
    "horror": ["Pisaasu", "Arundhati", "Kanchana", "Aval"],
    "comedy": ["Mark Antony", "Kalakalappu", "Tamizh Padam", "DD Returns"],
    "crime": ["Viduthalai", "Maharaja", "Jai Bhim", "Vanangaan"]
}
list_of_movies = list(collection.keys())

value = input("Enter your request (genres or ask about available genres): ").strip().lower()

def fun_movies(user_genres):
    display = []

    for genre in user_genres:
        genre = genre.strip()
        if genre in collection:
            display.extend(collection[genre])
        else:
            print(f"Genre '{genre}' not found in our database.")

    return display

if value == "what genres do you have?":
    print("\nWe have the following genres:")
    for genre in list_of_movies:
        print(f"- {genre}")
else:
    user_genres = value.split(",")
    display = fun_movies(user_genres)
    if display:
        print("\nHere are some movie recommendations for you based on your preference:")
        for movie in display:
            print(f"- {movie}")
    else:
        print("Sorry, we couldn't find any recommendations for your preference or suggestions.")