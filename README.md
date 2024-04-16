# University Collaboration Recommendation System

## Project Overview
The University Collaboration Recommendation System is designed to foster academic collaborations by accurately matching students and professors based on shared research interests and academic fields. Leveraging advanced Natural Language Processing (NLP) and Machine Learning techniques, this system parses and analyzes detailed research profiles to suggest optimal academic pairings.

## Key Features
- **Robust Text Processing**: Implements advanced NLP techniques to process and normalize research interest data.
- **Semantic Matching**: Uses embeddings to capture the deeper meaning of texts, improving the accuracy of matches.
- **Visualization**: Integrates WordClouds to visually represent common research themes among students and professors.
- **Scalable Matching Engine**: Employs cosine similarity for scalable and efficient similarity computations.
- **Interactive Analysis**: Provides tools for visual analysis of data distribution and similarity results.

## Technologies Used
- **Python**: The core programming language used.
- **Pandas & NumPy**: For data manipulation and numerical operations.
- **NLTK & SpaCy**: For natural language processing.
- **Scikit-Learn**: For machine learning operations and cosine similarity calculations.
- **WordCloud & Seaborn**: For data visualization.

## Prerequisites
To run this project, you will need Python 3.6+ and the following Python libraries installed:
- pandas
- numpy
- nltk
- spacy
- sklearn
- wordcloud
- seaborn

You can install all required packages with the following command:
```bash
pip install pandas numpy nltk spacy scikit-learn wordcloud seaborn
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
git clone https://github.com/anush97/Professor_Student_RecommendationSystem.git
cd Professor_Student_RecommendationSystem
```

## Usage
To run the system, navigate to the project directory and execute:
```bash
python recommendation_system.py
```

## System Architecture
- **Data Preprocessing**: Cleans and normalizes text inputs, preparing them for analysis.
- **Feature Engineering**: Converts research interests into vectorized form using TF-IDF and embeds them with SpaCy.
- **Similarity Calculation**: Computes similarity scores using a cosine similarity matrix to identify matches.
- **Recommendation Engine**: Generates and outputs top matches based on similarity scores, tailored to individual profiles.


