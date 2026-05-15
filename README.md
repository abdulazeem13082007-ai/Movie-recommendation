[README.md](https://github.com/user-attachments/files/27791003/README.md)
# README - Movie Recommendation System

## Project Overview

This is a simple **Movie Recommendation System** built using Python and Machine Learning concepts.

The program recommends a movie based on the genre selected by the user.

It uses:

- **Pandas** → for handling movie data
- **TF-IDF Vectorizer** → to convert text into numerical form
- **Cosine Similarity** → to find similar genres

---

# Features

- Movie recommendation based on genre
- Simple number-based genre selection
- Uses Machine Learning text similarity
- Beginner-friendly Python project

---

# Technologies Used

- Python
- Pandas
- Scikit-learn

---

# Installation

Install required libraries before running the program.

```bash
pip install pandas scikit-learn
```

---

# How the Program Works

1. Stores movie names and genres
2. Converts genre text into numbers using TF-IDF
3. User selects a genre using a number
4. Program compares selected genre with movie genres
5. Finds the most similar movie
6. Displays recommended movie

---

# Genre Options

| Number | Genre |
|---|---|
| 1 | action superhero |
| 2 | sci-fi adventure |
| 3 | horror supernatural |
| 4 | animation comedy |
| 5 | magic fantasy |
| 6 | romance drama |
| 7 | action thriller |

---

# Example Output

```text
Choose a genre number:
1. action superhero
2. sci-fi adventure
3. horror supernatural
4. animation comedy
5. magic fantasy
6. romance drama
7. action thriller

Enter number: 4

Recommended Movie: Toy Story
```

---

# Machine Learning Concepts Used

## 1. TF-IDF Vectorizer

TF-IDF converts text data into numerical values.

Example:

```text
action superhero
```

becomes numbers that the computer can understand.

---

## 2. Cosine Similarity

Cosine similarity checks how similar two genres are.

Similarity score:
- 0 → completely different
- 1 → exactly same

---

# Project Structure

```text
movie_recommendation/
│
├── movie_recommendation.py
└── README.md
```

---

# Future Improvements

You can improve this project by adding:

- More movies
- Movie posters
- Multiple recommendations
- User ratings
- GUI using Tkinter
- Web app using Flask or Django

---

# Author

Created using Python and Scikit-learn.
