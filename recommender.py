from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# DATA PATH
# ============================================================

DATA_PATH = Path(__file__).parent / "data" / "movies.csv"


# ============================================================
# MOVIE RECOMMENDER
# ============================================================

class MovieRecommender:

    def __init__(self, csv_path=DATA_PATH):

        self.movies = pd.read_csv(csv_path)

        # ----------------------------------------------------
        # Clean missing values
        # ----------------------------------------------------

        text_columns = [
            "language",
            "genres",
            "director",
            "cast",
            "keywords",
            "description"
        ]

        for column in text_columns:
            self.movies[column] = (
                self.movies[column]
                .fillna("")
                .astype(str)
            )

        self.movies["year"] = (
            pd.to_numeric(
                self.movies["year"],
                errors="coerce"
            )
            .fillna(0)
            .astype(int)
        )

        self.movies["rating"] = (
            pd.to_numeric(
                self.movies["rating"],
                errors="coerce"
            )
            .fillna(0)
        )

        # ----------------------------------------------------
        # Create ML content
        # ----------------------------------------------------

        self.movies["content"] = (
            self.movies["language"] + " "
            + self.movies["genres"].str.replace(
                "|", " ", regex=False
            ) + " "
            + self.movies["director"] + " "
            + self.movies["cast"].str.replace(
                "|", " ", regex=False
            ) + " "
            + self.movies["keywords"] + " "
            + self.movies["description"]
        )

        # ----------------------------------------------------
        # TF-IDF
        # ----------------------------------------------------

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        self.tfidf_matrix = (
            self.vectorizer.fit_transform(
                self.movies["content"]
            )
        )

        # ----------------------------------------------------
        # Cosine Similarity
        # ----------------------------------------------------

        self.similarity_matrix = cosine_similarity(
            self.tfidf_matrix
        )

    # ========================================================
    # GET LANGUAGES
    # ========================================================

    def get_languages(self):

        return sorted(
            self.movies["language"]
            .dropna()
            .unique()
            .tolist()
        )

    # ========================================================
    # GET GENRES
    # ========================================================

    def get_genres(self):

        genres = set()

        for genre_list in self.movies["genres"]:

            for genre in genre_list.split("|"):

                genre = genre.strip()

                if genre:
                    genres.add(genre)

        return sorted(genres)

    # ========================================================
    # FILTER MOVIES
    # ========================================================

    def filter_movies(
        self,
        language="All",
        genre="All",
        min_rating=0.0,
        min_year=0,
        max_year=9999
    ):

        filtered = self.movies.copy()

        # Language filter
        if language != "All":

            filtered = filtered[
                filtered["language"].str.lower()
                == language.lower()
            ]

        # Genre filter
        if genre != "All":

            filtered = filtered[
                filtered["genres"]
                .str.contains(
                    genre,
                    case=False,
                    regex=False
                )
            ]

        # Rating filter
        filtered = filtered[
            filtered["rating"] >= min_rating
        ]

        # Year filter
        filtered = filtered[
            (filtered["year"] >= min_year)
            & (filtered["year"] <= max_year)
        ]

        return filtered

    # ========================================================
    # GET MOVIE DETAILS
    # ========================================================

    def get_movie(self, title):

        matches = self.movies[
            self.movies["title"].str.lower()
            == title.lower()
        ]

        if matches.empty:
            return None

        return matches.iloc[0]

    # ========================================================
    # RECOMMEND MOVIES
    # ========================================================

    def recommend(
        self,
        title,
        n=5,
        language="All",
        genre="All",
        min_rating=0.0,
        min_year=0,
        max_year=9999
    ):

        # ----------------------------------------------------
        # Find selected movie
        # ----------------------------------------------------

        matches = self.movies[
            self.movies["title"].str.lower()
            == title.lower()
        ]

        if matches.empty:

            matches = self.movies[
                self.movies["title"]
                .str.lower()
                .str.contains(
                    title.lower(),
                    regex=False
                )
            ]

        if matches.empty:

            raise ValueError(
                f"Movie '{title}' was not found."
            )

        movie_index = matches.index[0]

        # ----------------------------------------------------
        # Similarity scores
        # ----------------------------------------------------

        scores = list(
            enumerate(
                self.similarity_matrix[
                    movie_index
                ]
            )
        )

        scores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        # ----------------------------------------------------
        # Apply filters
        # ----------------------------------------------------

        for index, similarity_score in scores:

            # Never recommend selected movie
            if index == movie_index:
                continue

            movie = self.movies.iloc[index]

            # Language
            if language != "All":

                if (
                    movie["language"].lower()
                    != language.lower()
                ):
                    continue

            # Genre
            if genre != "All":

                if genre.lower() not in (
                    movie["genres"].lower()
                ):
                    continue

            # Rating
            if movie["rating"] < min_rating:
                continue

            # Year
            if movie["year"] < min_year:
                continue

            if movie["year"] > max_year:
                continue

            # ------------------------------------------------
            # Add recommendation
            # ------------------------------------------------

            recommendations.append(
                {
                    "Movie": movie["title"],
                    "Language": movie["language"],
                    "Year": movie["year"],
                    "Genre": movie["genres"],
                    "Rating": movie["rating"],
                    "Director": movie["director"],
                    "Cast": movie["cast"],
                    "Description": movie["description"],
                    "Similarity": round(
                        float(similarity_score) * 100,
                        2
                    )
                }
            )

            if len(recommendations) >= n:
                break

        return pd.DataFrame(
            recommendations
        )