import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie data
data = {
    'movie': [
        'Avatar', 'Titanic', 'Avengers', 'Batman',
        'Spider-Man', 'Iron Man', 'Joker', 'Frozen',
        'Inception', 'Interstellar', 'The Dark Knight',
        'Doctor Strange', 'Thor', 'Black Panther',
        'Finding Nemo', 'Toy Story', 'Cars',
        'Harry Potter', 'Lord of the Rings',
        'The Conjuring', 'Annabelle', 'It',
        'Fast and Furious', 'John Wick',
        'Deadpool', 'Venom', 'Shrek',
        'Kung Fu Panda', 'Minions', 'Moana'
    ],

    'genre': [
        'sci-fi action adventure',
        'romance drama',
        'action superhero',
        'dark action hero',
        'action superhero adventure',
        'technology action superhero',
        'psychological crime drama',
        'animation fantasy family',
        'mind-bending sci-fi thriller',
        'space sci-fi drama',
        'crime dark action',
        'magic superhero fantasy',
        'mythology action fantasy',
        'africa superhero action',
        'animation family adventure',
        'animation comedy family',
        'animation racing comedy',
        'magic fantasy adventure',
        'fantasy war adventure',
        'horror supernatural',
        'horror doll supernatural',
        'horror thriller clown',
        'racing action crime',
        'action assassin thriller',
        'comedy action superhero',
        'dark superhero sci-fi',
        'animation comedy fantasy',
        'animation martial-arts comedy',
        'animation comedy family',
        'animation ocean adventure'
    ]
}
movies = pd.DataFrame(data)

# Convert genre text to numbers
tfidf = TfidfVectorizer()
vectors = tfidf.fit_transform(movies['genre'])

# Similarity
similarity = cosine_similarity(vectors)

# User input
genre = input("Enter genre: ")

# Convert input
user_vector = tfidf.transform([genre])

# Compare with movies
scores = cosine_similarity(user_vector, vectors)

# Best movie
best_index = scores.argmax()

print("Recommended Movie:", movies.iloc[best_index]['movie'])

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie data
data = {
    'movie': [
        'Avatar', 'Titanic', 'Avengers', 'Batman',
        'Spider-Man', 'Iron Man', 'Joker', 'Frozen',
        'Inception', 'Interstellar', 'The Dark Knight',
        'Doctor Strange', 'Thor', 'Black Panther',
        'Finding Nemo', 'Toy Story', 'Cars',
        'Harry Potter', 'Lord of the Rings',
        'The Conjuring', 'Annabelle', 'It',
        'Fast and Furious', 'John Wick',
        'Deadpool', 'Venom', 'Shrek',
        'Kung Fu Panda', 'Minions', 'Moana'
    ],

    'genre': [
        'sci-fi action adventure',
        'romance drama',
        'action superhero',
        'dark action hero',
        'action superhero adventure',
        'technology action superhero',
        'psychological crime drama',
        'animation fantasy family',
        'mind-bending sci-fi thriller',
        'space sci-fi drama',
        'crime dark action',
        'magic superhero fantasy',
        'mythology action fantasy',
        'africa superhero action',
        'animation family adventure',
        'animation comedy family',
        'animation racing comedy',
        'magic fantasy adventure',
        'fantasy war adventure',
        'horror supernatural',
        'horror doll supernatural',
        'horror thriller clown',
        'racing action crime',
        'action assassin thriller',
        'comedy action superhero',
        'dark superhero sci-fi',
        'animation comedy fantasy',
        'animation martial-arts comedy',
        'animation comedy family',
        'animation ocean adventure'
    ]
}
movies = pd.DataFrame(data)

# Convert genre text to numbers
tfidf = TfidfVectorizer()
vectors = tfidf.fit_transform(movies['genre'])

# Similarity
similarity = cosine_similarity(vectors)

print("Choose a genre number:")
print("1. action superhero")
print("2. sci-fi adventure")
print("3. horror supernatural")
print("4. animation comedy")
print("5. magic fantasy")
print("6. romance drama")
print("7. action thriller")

# User choice
choice = input("\nEnter number: ")

# Convert number to genre
genre_dict = {
    "1": "action superhero",
    "2": "sci-fi adventure",
    "3": "horror supernatural",
    "4": "animation comedy",
    "5": "magic fantasy",
    "6": "romance drama",
    "7": "action thriller"
}

genre = genre_dict.get(choice, "")

# Check valid input
if genre == "":
    print("Invalid choice")
else:
    # Convert input
    user_vector = tfidf.transform([genre])

    # Compare with movies
    scores = cosine_similarity(user_vector, vectors)

    # Best movie
    best_index = scores.argmax()

    print("Recommended Movie:", movies.iloc[best_index]['movie'])
# Convert input
user_vector = tfidf.transform([genre])

# Compare with movies
scores = cosine_similarity(user_vector, vectors)

# Best movie
best_index = scores.argmax()

print("Recommended Movie:", movies.iloc[best_index]['movie'])
