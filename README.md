## AI Movie Recommendation System

A simple movie recommendation system that recommends movies based on user preferences using similarity scoring.

##  Project Overview
The system takes three user preferences:

* Genre
* Mood
* Language

It compares these preferences with information about a collection of movies and calculates a similarity score for each movie.

Movies with higher similarity scores are displayed as stronger recommendations.

##  Objective

The objective of this project is to demonstrate a basic recommendation system using:

* User preferences
* Dataset handling
* Similarity logic
* Preference matching
* Recommendation ranking

##  How It Works

The system follows these steps:

1. Stores movie information in a dataset.
2. Asks the user for their preferred genre.
3. Asks the user for their preferred mood.
4. Asks the user for their preferred language.
5. Compares the user's preferences with every movie.
6. Calculates a similarity score.
7. Sorts movies according to their scores.
8. Displays matching movie recommendations.
9. Allows the user to rate the recommendations.

##  Similarity Scoring

Each matching preference gives the movie **1 point**.

| Preference       | Score |
| ---------------- | ----: |
| Genre matches    |    +1 |
| Mood matches     |    +1 |
| Language matches |    +1 |

The maximum possible score is:

**3/3**

For example, if the user chooses:

```text
Genre: Sci-Fi
Mood: Emotional
Language: English
```

A movie matching all three preferences receives:

```text
3/3
```

##  Movie Dataset

The system currently contains 12 movies:

1. Inception
2. Interstellar
3. The Martian
4. 3 Idiots
5. 500 Days of Summer
6. The Notebook
7. La La Land
8. Avengers: Endgame
9. The Pursuit of Happyness
10. Inside Out
11. Taare Zameen Par
12. Fight Club

Each movie contains:

* Title
* Genre
* Mood
* Language

##  Technologies Used

* Python
* Pandas
* Git
* GitHub

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/RehabTariqq/AI-Recommendation-System.git
```

### 2. Open the project folder

```bash
cd AI-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the required library

```bash
pip install pandas
```

### 6. Run the program

```bash
python recommendation_system.py
```

##  Example

The user enters:

```text
Genre: Romance
Mood: Emotional
Language: English
```

The system compares these preferences with the movie dataset and calculates a similarity score for each movie.

Movies with matching preferences receive higher scores and are displayed as recommendations.

##  Concepts Demonstrated

This project demonstrates basic concepts including:

* Python programming
* Dictionaries
* Functions
* Conditional statements
* Loops
* User input
* Pandas DataFrames
* Dataset handling
* Similarity scoring
* Sorting
* Recommendation logic

##  Future Improvements

Possible improvements include:

* Adding more movies
* Adding ratings for individual movies
* Using multiple genres
* Using weighted preferences
* Building a graphical user interface
* Using machine learning for recommendations
* Adding content-based filtering
* Connecting the system to a movie database API


*Developed as part of my Artificial Intelligence internship at DecodeLabs*.
