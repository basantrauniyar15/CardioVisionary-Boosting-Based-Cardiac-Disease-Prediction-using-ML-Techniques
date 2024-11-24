**CardioVisionary: Boosting Based Cardiac Disease Prediction using ML Techniques**

**Project Overview**

This project focuses on predicting the presence of heart disease using machine learning. It utilizes the Heart Disease UCI dataset, which includes various health attributes, such as age, cholesterol levels, and blood pressure, to predict whether an individual is at risk of heart disease. The application leverages several machine learning models, including Logistic Regression, Gradient Boosting, Random Forest, and Support Vector Machine (SVM), with the goal of providing an easy-to-use interface for early diagnosis and preventive healthcare.

**Features**

The heart disease prediction system includes several key features. It allows users to input personal and medical data through a web interface and provides a prediction of heart disease severity on a scale of 0-4. The system also suggests precautionary measures based on the prediction. The application is built using Flask for the backend, with a clean and responsive front-end created using HTML, CSS, and JavaScript. The best-performing machine learning model is Gradient Boosting, which offers an accuracy of 98.37%.

**Dataset**

The dataset used for this project is from the UCI Machine Learning Repository and contains 920 records, each with 16 attributes. These attributes include demographic information (such as age and sex), clinical data (such as cholesterol levels and blood pressure), and lifestyle factors. This dataset is used to train and test the machine learning models, enabling the prediction of heart disease risk based on the provided attributes.

**Installation**

To run the project, clone this repository and install the necessary dependencies like Flask, scikit-learn, and others. After installation, you can run the Flask application, which will be accessible on your local server. Detailed instructions are provided for easy setup, allowing you to start the project with minimal configuration.

**Web Interface**

The web application provides a user-friendly interface where users can enter their health data. Upon submission, the system predicts the likelihood of heart disease and provides the corresponding severity level. Additionally, it offers personalized health advice and precautions based on the prediction. The interface is built using modern web technologies, ensuring a smooth and intuitive user experience.

Model Evaluation

Several machine learning models were trained and evaluated for this project. The models include Logistic Regression, Random Forest, SVM, and Gradient Boosting. The Gradient Boosting model achieved the highest accuracy (98.37%), followed by Random Forest (97.28%). These models were evaluated using metrics such as accuracy, F1-score, and ROC curves, with Gradient Boosting emerging as the best model for predicting heart disease.
