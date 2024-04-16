# University Collaboration Recommendation System

## Project Overview
The University Collaboration Recommendation System is designed to foster academic collaborations by accurately matching students and professors based on shared research interests and academic fields. Leveraging advanced Natural Language Processing (NLP) and Machine Learning techniques, this system parses and analyzes detailed research profiles to suggest optimal academic pairings.

## Key Features
- **Robust Text Processing**: Implements advanced NLP techniques to process and normalize research interest data.
- **Semantic Matching**: Uses embeddings to capture the deeper meaning of texts, improving the accuracy of matches.
- **Visualization**: Integrates WordClouds to visually represent common research themes among students and professors.
- **Scalable Matching Engine**: Employs cosine similarity for scalable and efficient similarity computations.
- **Interactive Analysis**: Provides tools for visual analysis of data distribution and similarity results.
- **Web API**: A Flask API to query recommendations in real-time.
- **Front-End Interface**: A simple web form to input GUID and retrieve matched profiles.

## Technologies Used
- **Python**: The core programming language used.
- **Flask**: For the web API interface.
- **Pandas & NumPy**: For data manipulation and numerical operations.
- **NLTK & SpaCy**: For natural language processing.
- **Scikit-Learn**: For machine learning operations and cosine similarity calculations.
- **WordCloud & Seaborn**: For data visualization.
- **HTML & JavaScript**: For the front-end interface.

## Prerequisites
To run this project, you will need Python 3.6+ and the following Python libraries installed:
- Flask
- pandas
- numpy
- nltk
- spacy
- sklearn
- wordcloud
- seaborn

You can install all required packages with the following command:
```bash
pip install Flask pandas numpy nltk spacy scikit-learn wordcloud seaborn
```

Ensure you have the necessary NLTK data and SpaCy models downloaded:
```python
import nltk
import spacy
nltk.download('stopwords')
nltk.download('punkt')
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_lg
```

## Installation
To get a local copy up and running, follow these simple steps:
```bash
git clone https://github.com/anush97/University_Collaboration_Recommendation_System.git
cd University_Collaboration_Recommendation_System
```

## Usage
To start the web application and API, navigate to the project directory and execute:
```bash
python app.py
```
This will start the Flask server, and the application can be accessed at `http://127.0.0.1:5000`.

## API Endpoints
The Flask API provides endpoints to get recommendations:
- **POST** `/recommendations` - To receive recommendations based on the user type (student or professor) and GUID.

You can interact with the API directly using tools like `curl` or Postman, or use the web form provided by the index page.

## System Architecture
- **Data Preprocessing**: Cleans and normalizes text inputs, preparing them for analysis.
- **Feature Engineering**: Converts research interests into vectorized form using TF-IDF and embeds them with SpaCy.
- **Similarity Calculation**: Computes similarity scores using a cosine similarity matrix to identify matches.
- **Recommendation Engine**: Generates and outputs top matches based on similarity scores, tailored to individual profiles.
- **Web API**: Hosts the recommendation engine on a Flask server, allowing real-time HTTP requests.
- **Front-End**: A user-friendly interface to request and view recommendations.


## Methodology and Libraries
This section explains the methods and libraries used to implement the recommendation system:
- **Data Preprocessing**: Text data is cleaned and normalized using regular expressions and `NLTK`. This includes removing punctuation, lowercasing, and stemming.
- **NLP Techniques**: `SpaCy` is used to create embeddings for the research interest texts, which are then utilized to understand the context and semantics of words.
- **Vectorization**: Research interests are transformed into numerical data using `TF-IDF` vectorization from `Scikit-Learn`.
- **Similarity Scores**: The `cosine_similarity` function from `Scikit-Learn` is used to calculate the similarity between different profiles.
- **Flask**: A lightweight WSGI web application framework used to create the API and serve the front-end interface.
- **Front-End Development**: Basic HTML and JavaScript are used to create a user-friendly interface to interact with the API.


## Sources and Credits
The development of this project was inspired by a combination of academic literature on recommendation systems, documentation of the various libraries used, and community-driven resources such as Stack Overflow and GitHub repositories.
Some links -
- https://esource.dbs.ie/server/api/core/bitstreams/ea22d96a-262c-42bf-9bf3-8fbb98e3d36a/content
- https://aclanthology.org/R19-2009.pdf
- https://github.com/AmoliR/nlp-for-book-recommendation/tree/76ca80daf9eb733274a3d92887bbfbec7b48704c

## Contact
For any further queries or issues related to the recommendation system, you can open an issue on the GitHub repository or contact the maintainers directly.

