# Movie Recommendation System
**This project is a content-based movie recommendation system that suggests top similar movies based on a user's chosen film, enhancing discovery with visual context.**

## Project Highlights:
**1-Intelligent Recommendations:** Engineered a machine learning model in Python that leverages Natural Language Processing (NLP) techniques and vectorization to convert movie features into numerical representations. This enables the system to compute cosine similarity, identifying and recommending the top 10 most similar movies.

**2-End-to-End Development:** Managed the entire project lifecycle, from gathering and preprocessing 5000+ movie records (including cleaning and handling missing values) to deploying a user-friendly web application.

**3-Interactive User Experience:** Built a responsive front-end using Streamlit that allows users to select a movie title from a dropdown. The system then fetches and displays movie posters via the TMDB API, providing rich visual context for recommendations.

**4-Key Technologies:** Python | NumPy | Pandas | Scikit-learn | Natural Language Processing (NLP) techniques | Vectorization | Stemming | Cosine similarity

Gathered and preprocessed movie data from a dataset, including cleaning and handling missing values --> Implemented vectorization techniques to convert movie features into numerical representations suitable for machine learning algorithms --> Utilized cosine similarity to compute the similarity between movies based on their feature vectors --> Designed the recommender system to provide top 10 movie recommendations for a given movie input

## Project flow: 1.Data --> 2.Preprocessing --> 3.Model --> 4.Website --> 5.Deploy.
![WhatsApp Image 2024-04-05 at 9 33 34 PM](https://github.com/prerakpanwar/Recommender-System/assets/40028120/78516baf-f61e-4728-b432-51b6766d363b)

### How It Works
The system operates on a content-based filtering approach. When you select a movie, its unique features (like genres, keywords, cast, and plot overview) are transformed into numerical vectors. Cosine similarity then measures the "angle" between your selected movie's vector and all other movie vectors. A smaller angle (closer to 1) indicates higher similarity. The system then returns the top 10 movies with the highest similarity scores, complete with their posters from the TMDB API.

### Usage
*Clone the repository and ensure you have the necessary libraries installed.

*Get a TMDB API key from "https://www.themoviedb.org/" (you can use the provided key if it's active, otherwise create your own).

*Run the Streamlit application using "streamlit run application.py" in your terminal.

*Open your web browser to the local host address provided by Streamlit.

*Select a movie from the dropdown to instantly get your top recommendations!

### Results
![Screenshot 2025-06-06 144534](https://github.com/user-attachments/assets/43742aba-f686-435d-92f4-49061c6323e0)

### Dataset link:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata


