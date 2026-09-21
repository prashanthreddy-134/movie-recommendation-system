import streamlit as st
from urllib.parse import quote_plus
from recommender import MovieRecommender


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Indian Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        opacity: 0.75;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 27px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .movie-card {
        padding: 22px;
        border-radius: 18px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 20px;
        background: rgba(128, 128, 128, 0.05);
    }

    .movie-title {
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .movie-meta {
        font-size: 15px;
        opacity: 0.80;
        margin-bottom: 15px;
    }

    .info-box {
        padding: 20px;
        border-radius: 16px;
        background: rgba(128, 128, 128, 0.08);
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .feature-box {
        padding: 15px;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.20);
        background: rgba(128, 128, 128, 0.04);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD RECOMMENDER MODEL
# =========================================================

@st.cache_resource
def load_recommender():
    return MovieRecommender()


recommender = load_recommender()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">'
    '🎬 Indian Movie Recommendation System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover Telugu and Kannada movies using '
    'Machine Learning and Content-Based Recommendation.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎛️ Movie Filters")

st.sidebar.markdown(
    "Use the filters below to discover movies."
)


# ---------------------------------------------------------
# LANGUAGE
# ---------------------------------------------------------

languages = ["All"] + recommender.get_languages()

language = st.sidebar.selectbox(
    "🌐 Language",
    languages
)


# ---------------------------------------------------------
# GENRE
# ---------------------------------------------------------

genres = ["All"] + recommender.get_genres()

genre = st.sidebar.selectbox(
    "🎭 Genre",
    genres
)


# ---------------------------------------------------------
# RATING
# ---------------------------------------------------------

min_rating = st.sidebar.slider(
    "⭐ Minimum Rating",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)


# ---------------------------------------------------------
# YEAR
# ---------------------------------------------------------

all_movies = recommender.movies

min_dataset_year = int(
    all_movies["year"].min()
)

max_dataset_year = int(
    all_movies["year"].max()
)


year_range = st.sidebar.slider(
    "📅 Release Year",
    min_value=min_dataset_year,
    max_value=max_dataset_year,
    value=(
        min_dataset_year,
        max_dataset_year
    )
)


# ---------------------------------------------------------
# NUMBER OF RECOMMENDATIONS
# ---------------------------------------------------------

number_of_movies = st.sidebar.slider(
    "🔢 Number of Recommendations",
    min_value=3,
    max_value=10,
    value=5
)


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_movies = recommender.filter_movies(
    language=language,
    genre=genre,
    min_rating=min_rating,
    min_year=year_range[0],
    max_year=year_range[1]
)


# =========================================================
# NO MOVIES FOUND
# =========================================================

if filtered_movies.empty:

    st.warning(
        "⚠️ No movies match your selected filters. "
        "Try changing the language, genre, rating or year."
    )

    st.stop()


# =========================================================
# MOVIE SELECTION
# =========================================================

movie_titles = filtered_movies["title"].tolist()


selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movie_titles
)


movie = recommender.get_movie(
    selected_movie
)


if movie is None:

    st.error(
        "❌ Movie information could not be loaded."
    )

    st.stop()


# =========================================================
# SELECTED MOVIE SECTION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🎥 Selected Movie'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# MOVIE METRICS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🌐 Language",
        movie["language"]
    )


with col2:

    st.metric(
        "📅 Year",
        int(movie["year"])
    )


with col3:

    st.metric(
        "⭐ Rating",
        f'{float(movie["rating"]):.1f}/10'
    )


with col4:

    primary_genre = str(
        movie["genres"]
    ).split("|")[0]

    st.metric(
        "🎭 Genre",
        primary_genre
    )


# =========================================================
# MOVIE DETAILS
# =========================================================

st.markdown(
    f"""
    <div class="info-box">

    <h3>🎬 {movie["title"]}</h3>

    <p>
    <b>🎬 Director:</b>
    {movie["director"]}
    </p>

    <p>
    <b>👥 Cast:</b>
    {str(movie["cast"]).replace("|", ", ")}
    </p>

    <p>
    <b>🎭 Genres:</b>
    {str(movie["genres"]).replace("|", ", ")}
    </p>

    <p>
    <b>📖 Story:</b>
    {movie["description"]}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# WATCH MOVIE + TRAILER
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🍿 Watch Movie'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# JUSTWATCH SEARCH
# ---------------------------------------------------------

encoded_movie = quote_plus(
    f'{movie["title"]} {movie["language"]}'
)


watch_url = (
    "https://www.justwatch.com/in/search?q="
    + encoded_movie
)


# ---------------------------------------------------------
# YOUTUBE TRAILER SEARCH
# ---------------------------------------------------------

trailer_query = quote_plus(
    f'{movie["title"]} '
    f'{movie["language"]} '
    f'official trailer'
)


trailer_url = (
    "https://www.youtube.com/results?search_query="
    + trailer_query
)


# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------

watch_col, trailer_col = st.columns(2)


with watch_col:

    st.link_button(
        "▶️ Watch Movie",
        watch_url,
        use_container_width=True
    )


with trailer_col:

    st.link_button(
        "🎞️ Watch Trailer",
        trailer_url,
        use_container_width=True
    )


st.caption(
    "Watch Movie opens the movie's legal streaming availability "
    "in India. Availability depends on platform, region and subscription."
)


# =========================================================
# RECOMMENDATION SECTION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🤖 AI Movie Recommendations'
    '</div>',
    unsafe_allow_html=True
)


st.write(
    "Find movies similar to your selected movie "
    "using TF-IDF and Cosine Similarity."
)


# =========================================================
# GENERATE RECOMMENDATIONS
# =========================================================

generate_button = st.button(
    "🚀 Generate Recommendations",
    type="primary",
    use_container_width=True
)


if generate_button:

    recommendations = recommender.recommend(
        title=selected_movie,
        n=number_of_movies,
        language=language,
        genre=genre,
        min_rating=min_rating,
        min_year=year_range[0],
        max_year=year_range[1]
    )


    # =====================================================
    # NO RECOMMENDATIONS
    # =====================================================

    if recommendations.empty:

        st.warning(
            "⚠️ No recommendations found with the current "
            "filters. Try relaxing some filters."
        )


    else:

        # =================================================
        # RECOMMENDATION SUMMARY
        # =================================================

        st.success(
            f"✅ Found {len(recommendations)} "
            f"recommended movies for {selected_movie}."
        )


        # =================================================
        # SORTING
        # =================================================

        sort_option = st.selectbox(
            "🔃 Sort Recommendations By",
            [
                "Similarity",
                "Rating",
                "Year"
            ]
        )


        if sort_option == "Similarity":

            recommendations = recommendations.sort_values(
                "Similarity",
                ascending=False
            )


        elif sort_option == "Rating":

            recommendations = recommendations.sort_values(
                "Rating",
                ascending=False
            )


        elif sort_option == "Year":

            recommendations = recommendations.sort_values(
                "Year",
                ascending=False
            )


        # =================================================
        # RECOMMENDATION CARDS
        # =================================================

        for index, rec in recommendations.iterrows():

            rec_title = str(
                rec["Movie"]
            )


            rec_language = str(
                rec["Language"]
            )


            rec_year = int(
                rec["Year"]
            )


            rec_rating = float(
                rec["Rating"]
            )


            rec_similarity = float(
                rec["Similarity"]
            )


            rec_genre = str(
                rec["Genre"]
            )


            rec_director = str(
                rec["Director"]
            )


            rec_cast = str(
                rec["Cast"]
            )


            rec_description = str(
                rec["Description"]
            )


            # =================================================
            # WATCH URL
            # =================================================

            rec_encoded_movie = quote_plus(
                f'{rec_title} {rec_language}'
            )


            rec_watch_url = (
                "https://www.justwatch.com/in/search?q="
                + rec_encoded_movie
            )


            # =================================================
            # TRAILER URL
            # =================================================

            rec_trailer_query = quote_plus(
                f'{rec_title} '
                f'{rec_language} '
                f'official trailer'
            )


            rec_trailer_url = (
                "https://www.youtube.com/results?search_query="
                + rec_trailer_query
            )


            # =================================================
            # MOVIE CARD
            # =================================================

            st.markdown(
                '<div class="movie-card">',
                unsafe_allow_html=True
            )


            # -------------------------------------------------
            # TITLE
            # -------------------------------------------------

            st.markdown(
                f'<div class="movie-title">'
                f'🎬 {rec_title}'
                f'</div>',
                unsafe_allow_html=True
            )


            # -------------------------------------------------
            # META INFORMATION
            # -------------------------------------------------

            st.markdown(
                f"""
                <div class="movie-meta">

                🌐 {rec_language}
                &nbsp; | &nbsp;
                📅 {rec_year}
                &nbsp; | &nbsp;
                ⭐ {rec_rating:.1f}/10

                </div>
                """,
                unsafe_allow_html=True
            )


            # -------------------------------------------------
            # DETAILS COLUMNS
            # -------------------------------------------------

            info_col1, info_col2 = st.columns(2)


            with info_col1:

                st.write(
                    f"🎭 **Genres:** "
                    f"{rec_genre.replace('|', ', ')}"
                )

                st.write(
                    f"🎬 **Director:** "
                    f"{rec_director}"
                )


            with info_col2:

                st.write(
                    f"👥 **Cast:** "
                    f"{rec_cast.replace('|', ', ')}"
                )

                st.write(
                    f"📅 **Release Year:** "
                    f"{rec_year}"
                )


            # -------------------------------------------------
            # STORY
            # -------------------------------------------------

            st.write(
                f"📖 **Story:** {rec_description}"
            )


            # =================================================
            # SIMILARITY SCORE
            # =================================================

            st.write(
                f"🤖 **Similarity Score: "
                f"{rec_similarity:.1f}%**"
            )


            # -------------------------------------------------
            # PROGRESS BAR
            # -------------------------------------------------

            progress_value = min(
                max(rec_similarity / 100, 0.0),
                1.0
            )


            st.progress(
                progress_value
            )


            # =================================================
            # WATCH + TRAILER
            # =================================================

            rec_col1, rec_col2 = st.columns(2)


            with rec_col1:

                st.link_button(
                    "▶️ Watch Movie",
                    rec_watch_url,
                    use_container_width=True
                )


            with rec_col2:

                st.link_button(
                    "🎞️ Watch Trailer",
                    rec_trailer_url,
                    use_container_width=True
                )


            # =================================================
            # END CARD
            # =================================================

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        # =================================================
        # CSV EXPORT
        # =================================================

        st.markdown(
            "### 📥 Export Recommendations"
        )


        csv_data = recommendations.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            "⬇️ Download Recommendations CSV",
            data=csv_data,
            file_name="movie_recommendations.csv",
            mime="text/csv",
            use_container_width=True
        )


# =========================================================
# PROJECT FEATURES
# =========================================================

st.markdown(
    '<div class="section-title">'
    '✨ Project Features'
    '</div>',
    unsafe_allow_html=True
)


feature_col1, feature_col2, feature_col3 = st.columns(3)


with feature_col1:

    st.markdown(
        """
        <div class="feature-box">

        ### 🤖 Machine Learning

        • TF-IDF Vectorization  
        • Cosine Similarity  
        • Content-Based Filtering  

        </div>
        """,
        unsafe_allow_html=True
    )


with feature_col2:

    st.markdown(
        """
        <div class="feature-box">

        ### 🎛️ Smart Filters

        • Telugu / Kannada  
        • Genre  
        • Rating  
        • Release Year  

        </div>
        """,
        unsafe_allow_html=True
    )


with feature_col3:

    st.markdown(
        """
        <div class="feature-box">

        ### 🍿 Movie Discovery

        • Movie Details  
        • Watch Movie  
        • Watch Trailer  
        • Similarity Score  

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ML EXPLANATION
# =========================================================

with st.expander(
    "🧠 How does the Recommendation System work?"
):

    st.markdown(
        """
        ### 1️⃣ Movie Features

        The system uses multiple movie attributes:

        - Language
        - Genres
        - Director
        - Cast
        - Keywords
        - Movie description


        ### 2️⃣ Text Processing

        These movie attributes are combined into a
        single content representation.


        ### 3️⃣ TF-IDF

        TF-IDF converts the movie text into numerical
        feature vectors.

        This allows the machine learning model to
        understand important words and terms.


        ### 4️⃣ Cosine Similarity

        Cosine Similarity calculates how similar
        movies are to each other.

        A higher similarity score means that the
        movies have more similar content.


        ### 5️⃣ Content-Based Recommendation

        When you select a movie, the system finds
        other movies with similar characteristics.


        ### 6️⃣ Filtering

        Recommendations can be filtered by:

        - Language
        - Genre
        - Minimum rating
        - Release year


        ### 7️⃣ Ranking

        Results can be sorted by:

        - Similarity
        - Rating
        - Release year
        """
    )


# =========================================================
# TECHNOLOGIES
# =========================================================

with st.expander(
    "🛠️ Technologies Used"
):

    st.write(
        """
        **Programming Language:** Python

        **Frontend/UI:** Streamlit

        **Data Processing:** Pandas

        **Machine Learning:** Scikit-learn

        **NLP:** TF-IDF Vectorization

        **Similarity Algorithm:** Cosine Similarity

        **Dataset:** Telugu and Kannada Movies
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()


st.caption(
    "🎬 Indian Movie Recommendation System | "
    "Python • Streamlit • Pandas • Scikit-learn • "
    "TF-IDF • Cosine Similarity"
)