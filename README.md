# Diabetes-Mellitus-Prediction

**Predictive Analysis of Diabetes Mellitus using Data Mining Algorithms**

This project presents a web-based system that predicts the likelihood of Diabetes Mellitus in individuals using classic data mining classification techniques. The objective is to enable early diagnosis and improve healthcare interventions through interpretable and accessible models.

**Overview**

Diabetes Mellitus (DM) is a chronic disease affecting millions globally. This project leverages data mining algorithms—specifically Decision Tree, Naïve Bayes, and Random Forest—to build predictive models based on patient health attributes. The system is designed to deliver accurate, interpretable, and real-time predictions, and is integrated into a user-friendly web application using Flask.

**Algorithms Used**

Decision Tree
Naïve Bayes
Random Forest (Best performer with 96.97% accuracy)

**Dataset**

The dataset includes medical records with features such as:

Age
Body Mass Index (BMI)
HbA1c level
Blood glucose level
History of hypertension and heart disease
Target: Presence (1) or Absence (0) of Diabetes

**Methodology**

Data Preprocessing: Handle missing values, normalize features, encode categories.
Model Training: Train Decision Tree, Naïve Bayes, and Random Forest on a 70:30 train-test split.
Model Evaluation: Use Accuracy, Precision, Recall, and F1-score for performance measurement.
Web Deployment: Integrate the best model (Random Forest) into a Flask-based web app.
User Interaction: Web interface (HTML/CSS/JS) takes user input and displays prediction results.

**Features**

Reliable prediction system with 96.97% accuracy
Simple and clear user interface
Real-time results
Easy deployment and integration
Open for further improvement (real-time data, more features, cloud deployment)

**Results**

Model	            Accuracy	    Precision	     Recall	      F1 Score
Decision Tree	     93.78%    	    Good	        Good	        Good
Naïve Bayes	       91.89%	       Moderate	      Good	        Fair
Random Forest	     96.97%	      Excellent	    Excellent	    Excellent

**Future Scope**

Integration of live Electronic Health Records (EHR)
More health metrics (e.g., insulin levels, cholesterol)
Mobile app development
Real-time cloud-based deployment

**Technologies Used**

Python
Flask
HTML / CSS / JavaScript
Scikit-learn, Pandas, NumPy

**Authors**

Om Hojage

Omkar Waghade

Atharva Padwal

Arnav Pachori

Avishkar Padwal

Dr. Kiran More (Guide)
