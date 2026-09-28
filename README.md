**AI Movie Recommendation System**

A simple movie recommendation system that recommends movies based on user preferences using similarity scoring.

**Project Overview**

This project was developed as part of my Artificial Intelligence internship at DecodeLabs.

The system takes three user preferences:

Genre
Mood
Language

It compares these preferences with information about a collection of movies and calculates a similarity score for each movie.

Movies with higher similarity scores are displayed as stronger recommendations.

**Objective**

The objective of this project is to demonstrate a basic recommendation system using:

User preferences
Dataset handling
Similarity logic
Preference matching
Recommendation ranking

**How It Works**

The system follows these steps:

Stores movie information in a dataset.
Asks the user for their preferred genre.
Asks the user for their preferred mood.
Asks the user for their preferred language.
Compares the user's preferences with every movie.
Calculates a similarity score.
Sorts movies according to their scores.
Displays matching movie recommendations.
Allows the user to rate the recommendations.

**Similarity Scoring**

Each matching preference gives the movie 1 point.

Preference	Score
Genre matches	+1
Mood matches	+1
Language matches	+1

The maximum possible score is:

3/3

For example, if the user chooses:

Genre: Sci-Fi
Mood: Emotional
Language: English

A movie matching all three preferences receives:

3/3
**🎬 Movie Dataset**

The system currently contains 12 movies:

Inception
Interstellar
The Martian
3 Idiots
500 Days of Summer
The Notebook
La La Land
Avengers: Endgame
The Pursuit of Happyness
Inside Out
Taare Zameen Par
Fight Club

Each movie contains:

Title
Genre
Mood
Language
**Technologies Used**
Python
Pandas
Git
GitHub
**▶ How to Run**
1. Clone the repository
git clone https://github.com/RehabTariqq/AI-Recommendation-System.git
2. Open the project folder
cd AI-Recommendation-System
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install the required library
pip install pandas
6. Run the program
python recommendation_system.py
 Example

The user enters:

Genre: Romance
Mood: Emotional
Language: English

The system compares these preferences with the movie dataset and calculates a similarity score for each movie.

Movies with matching preferences receive higher scores and are displayed as recommendations.

**Concepts Demonstrated**

This project demonstrates basic concepts including:

Python programming
Dictionaries
Functions
Conditional statements
Loops
User input
Pandas DataFrames
Dataset handling
Similarity scoring
Sorting
Recommendation logic
 Future Improvements

**Possible improvements include:**

Adding more movies
Adding ratings for individual movies
Using multiple genres
Using weighted preferences
Building a graphical user interface
Using machine learning for recommendations
Adding content-based filtering
Connecting the system to a movie database API

*Built as part of my Artificial Intelligence Internship at DecodeLabs.*
