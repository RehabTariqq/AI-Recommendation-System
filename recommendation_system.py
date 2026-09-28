import pandas as pd


# -----------------------------------------
# 1. MOVIE DATASET
# -----------------------------------------

movies = {
    "title": [
        "Inception",
        "Interstellar",
        "The Martian",
        "3 Idiots",
        "500 Days of Summer",
        "The Notebook",
        "La La Land",
        "Avengers: Endgame",
        "The Pursuit of Happyness",
        "Inside Out",
        "Taare Zameen Par",
        "Fight Club"
    ],

    "genre": [
        "Sci-Fi",
        "Sci-Fi",
        "Sci-Fi",
        "Comedy",
        "Romance",
        "Romance",
        "Romance",
        "Action",
        "Drama",
        "Animation",
        "Drama",
        "Thriller"
    ],

    "mood": [
        "Thriller",
        "Emotional",
        "Inspirational",
        "Inspirational",
        "Emotional",
        "Emotional",
        "Emotional",
        "Exciting",
        "Inspirational",
        "Emotional",
        "Inspirational",
        "Thriller"
    ],

    "language": [
        "English",
        "English",
        "English",
        "Hindi",
        "English",
        "English",
        "English",
        "English",
        "English",
        "English",
        "Hindi",
        "English"
    ]
}


# Convert the movie data into a DataFrame
movie_data = pd.DataFrame(movies)


# -----------------------------------------
# 2. WELCOME MESSAGE
# -----------------------------------------

print("=" * 55)
print("        AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 55)

print("\nChoose your preferences from the following options.")

print("\nGenres:")
print("Sci-Fi")
print("Comedy")
print("Romance")
print("Action")
print("Drama")
print("Animation")
print("Thriller")

print("\nMoods:")
print("Thriller")
print("Emotional")
print("Inspirational")
print("Exciting")

print("\nLanguages:")
print("English")
print("Hindi")


# -----------------------------------------
# 3. GET USER PREFERENCES
# -----------------------------------------

user_genre = input("\nEnter your preferred genre: ").strip()

user_mood = input("Enter your preferred mood: ").strip()

user_language = input("Enter your preferred language: ").strip()


# -----------------------------------------
# 4. CALCULATE SIMILARITY SCORE
# -----------------------------------------

def calculate_similarity(movie):

    score = 0

    # Compare genre
    if movie["genre"].lower() == user_genre.lower():
        score += 1

    # Compare mood
    if movie["mood"].lower() == user_mood.lower():
        score += 1

    # Compare language
    if movie["language"].lower() == user_language.lower():
        score += 1

    return score


# Calculate score for every movie
movie_data["similarity_score"] = movie_data.apply(
    calculate_similarity,
    axis=1
)


# -----------------------------------------
# 5. SORT MOVIES BY SCORE
# -----------------------------------------

recommendations = movie_data.sort_values(
    by="similarity_score",
    ascending=False
)


# -----------------------------------------
# 6. DISPLAY RECOMMENDATIONS
# -----------------------------------------

print("\n" + "=" * 55)
print("              YOUR RECOMMENDATIONS")
print("=" * 55)

found_recommendation = False

for _, movie in recommendations.iterrows():

    if movie["similarity_score"] > 0:

        found_recommendation = True

        print(f"\n🎬 {movie['title']}")
        print(f"Genre: {movie['genre']}")
        print(f"Mood: {movie['mood']}")
        print(f"Language: {movie['language']}")
        print(
            f"Match Score: "
            f"{movie['similarity_score']}/3"
        )


# -----------------------------------------
# 7. IF NOTHING MATCHES
# -----------------------------------------

if not found_recommendation:

    print("\nNo matching movies were found.")

    print(
        "Please try using one of the "
        "available preferences."
    )


# -----------------------------------------
# 8. USER RATING
# -----------------------------------------

if found_recommendation:

    print("\n" + "=" * 55)

    rating = input(
        "How would you rate these recommendations "
        "(1-5)? "
    ).strip()

    if rating.isdigit():

        rating_number = int(rating)

        if 1 <= rating_number <= 5:

            print(
                f"\nThank you! You rated the "
                f"recommendations {rating_number}/5."
            )

        else:

            print(
                "\nPlease enter a rating between 1 and 5."
            )

    else:

        print(
            "\nPlease enter a number between 1 and 5."
        )


print("\nThank you for using the AI Movie Recommendation System!")