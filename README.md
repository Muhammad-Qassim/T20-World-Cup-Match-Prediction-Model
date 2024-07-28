# T20 World Cup Match Prediction Model

This project aims to predict the outcome of cricket matches based on various features such as team rankings, recent form, venue, toss decision, and head-to-head statistics. The project utilizes machine learning techniques to train a model on historical match data and evaluate its performance.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Usage](#usage)
- [Feature Engineering](#feature-engineering)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results and Analysis](#results-and-analysis)
- [Contributing](#contributing)
- [License](#license)

## Project Overview


1. **Data Loading**: The cricket match data is loaded from a CSV file named `t20_wc24_match_data.csv`.
2. **Data Preprocessing**: Missing values are handled, and categorical features are encoded. The data is split into training and testing sets.
3. **Feature Engineering**: Additional features are derived from the existing data, such as recent team performance, head-to-head win rates, and date components.
4. **Model Training**: A machine learning model (Gradient Boosting Classifier) is trained using the preprocessed data.
5. **Model Evaluation**: The trained model's performance is evaluated using metrics like accuracy, precision, recall, and F1-score.
6. **Feature Importance Analysis**: The relative importance of each feature in the model's predictions is analyzed and visualized.

## Dataset

The project uses the `t20_wc24_match_data.csv` dataset, which contains historical cricket match data. The dataset should be placed in the `data` directory before running the script.

The CSV file was created using JSON files for matches from CricSheet. I developed a custom script to convert these JSON files into a CSV format, extracting the necessary information for my model.


## Feature Engineering

The project implements several feature engineering techniques to derive additional features from the existing data. These include:

- Calculating recent team performance (win rate, runs scored, wickets lost)
- Encoding categorical features (venue, team names)
- Extracting date components (year, month, day)
- Calculating head-to-head win rates between teams

## Model Training and Evaluation

The project uses a Gradient Boosting Classifier model from the scikit-learn library. The model is trained on the preprocessed data, and its performance is evaluated using metrics such as accuracy, precision, recall, and F1-score. Additionally, the project analyzes the relative importance of each feature in the model's predictions.

## Results and Analysis

The initial model achieved an accuracy of 64.00% when including venue features. However, subsequent analysis revealed that venue features dominated the model's decision-making process, potentially leading to overfitting.

To mitigate this issue, the venue features were removed, and the model was retrained. Remarkably, the model's accuracy remained at 64.00%, suggesting that while venue features carried substantial weight, their exclusion did not significantly impact overall performance.

Further analysis of feature importances highlighted that recent team performance and home advantage were the most influential factors in the model's predictions. In contrast, features like head-to-head win rates contributed minimally.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
