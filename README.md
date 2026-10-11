# Movie Recommender System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-154F5B?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![TMDB](https://img.shields.io/badge/TMDB_API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)

A content-based movie recommender built with Streamlit. Pick a movie and get five similar ones with their posters.

**Live demo:** https://movie-recoms.streamlit.app

## Key skills

- **Text preprocessing:** lowercasing, tokenization, Porter stemming (NLTK) and stop word removal
- **Feature engineering:** overview, genres, keywords, top 3 cast and director merged into one tag per movie
- **Vectorisation:** bag-of-words with `CountVectorizer` (5000 features)
- **Similarity:** cosine similarity for content-based filtering
- **Optimisation:** precomputed top-5 neighbours (88 KB) instead of the 176 MB similarity matrix
- **Integration and deployment:** TMDB API for posters, deployed on Streamlit Community Cloud

Data: [TMDB 5000 Movies dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). The full pipeline is in `main.ipynb`.

## Run locally

```bash
git clone https://github.com/imsoumya18/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
```

Add a free [TMDB API key](https://www.themoviedb.org/settings/api) to `.streamlit/secrets.toml` (or set `TMDB_API_KEY` as an environment variable):

```toml
TMDB_API_KEY = "your_key"
```

```bash
streamlit run app.py
```
