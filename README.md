<div align='center'>
    <h1>Forest Fire Prediction</h1>
    <h3><b>Machine Learning Project<b></h3>

</div>

<br>
<h3 align='center'><b>Homepage</b></h3>

<!--![Home Page](AppImages/Home.PNG)-->

![Home](https://github.com/abhichris63/Algerian_Forest_Fires_Prediction/assets/95648648/de869d9d-7037-4201-9572-e589a4ea6c12)


<h3>Project is Created by Abhishek B</h3>

[CLICK HERE TO START AZURE APP](https://forest-fire-predict.azurewebsites.net/)


* This is Forest Fire Prediction Project using **Data Science** and **Machine Learning**.
* Source Dataset is stored in **MongoDB**.
* Applied EDA (Exploratory Data Analysis), Feature Engineering, Feature Selection.
* Model Building.
* Deployment **Flask app** in **Microsoft Azure**.

<h3>Dataset</h3>

* Dataset from UCI Repository [Algerian Forest Fire Dataset.](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset)
* From this dataset (features with weather indexes) we will try to predict future fires by using machine learning algorithms in these regions.
* It is always a good pratice to understand dataset first.
* The dataset includes 244 instances and it is divided into 2 groups namely Bejaia region located in northeast of Algeria & Sidi-Bel-abbes region located in northwest of Algeria.
* In this dataset the time period is from June 2012 to September 2012.

<h3> Loading Dataset & inserting into MongoDB Database</h3>

* Using Pandas Library the Dataset(CSV) file is loaded in Jupyter notebook as DataFrame.
* DataFrame is converted to dictionary and inserted into MongoDB database.
* 'pymongo' library is used to connect MongoDB Atlas.
* 'client['Database_name]' is used to create database.
* 'Database_name['Collections]' is used to create Collection/Tables.
* 'collection.insert_many' (Tables in MongoDB are called **Collections**), records are called documents in MongoDB. 

<h3>EDA</h3>

* Exploratory Data Analysis helps to analysis the dataset using pandas, numpy, matplotlib & seaborn.
* EDA extracts insights from the dataset & provides the path for future forest fire predictions.
* EDA helps to find feature importance which are more contributed in predicting Forest Fire.

<h3>Feature Engineering</h3>

* Feature Engineering is a process of selecting & transforming features into suitable format for machine learning model training.
* Label Encoding technique is used in this project to transform categorical variables into numerical variables in Feature Engineering.
* Standardization is used to rescale the features to bring all the features to the same scale.

<h3>Model Building</h3>

* Model Building is done into Regression & Classification Algorithms.
* In Regression: **Linear regression, Ridge Regression, Lasso Regression,Support Vector Regressor, Decision tree, Random forest Regressor, K-Nearest Neighbour regressor.**  
* In Classification: **Logistic Regression, Support Vector Classifier, Decision Tree, Naive Bayes, Random Forest, K-Nearest Neighbour.**

<h3>Model Selection</h3>

* After applying various tunning techniques such as :
  1. HyperParameter Tuning for Regression & Classification :
      * Randomized Gridsearch CV
  2. HyperParameter Tuning for Classification :
      * Stratified Kfold Cross-Validation

    * The Best Model from Regression is Random Forest Regressor	with 97.91% R2 Score.
    * The Best Model from Classification is Random Forest Classification with 97.10% Accurary score.
    * HyperParameter is applied for both Models based on their availablity. 

<h3>Flask App Creation</h3>

* By importing 'Flask' module we created a flask instance called 'app'. Starts an app using **app.run** & Flask web server is created.
* Using Jinga2 temple engine we can display HTML files in the web browser by using render_template() function.
* Route '/' for home page.
* Route '/chooseinput' for chosing type of input page.
* Route '/c_prediction' for single prediction of classification model page.
* Route '/r_prediction' for single prediction of regression model page.
* Route '/bulk_prediction' for bulk inputs, using database name & collection name dataset is loaded from MongoDB Atlas. 
* Regression & classification models are predicted & displayed in Bulk results.

<h3>App Deployment in Azure</h3>

* Create a repo in Github, push all data from local to 'Github'.
* Login Azure and setup the app.
* Connect 'Github repo' with azure
* Start the app to host in web browser.

<h3>Steps to Run this Project</h3>

* Open Terminal.
* 'cd' to change directory to this project directory.
* 'pip install -r requirements.txt' run this command to install project dependencies.
* 'python app.py' to run the project. 



<h3>Contact me</h3>

* <a href="https://www.linkedin.com/in/abhishek-b-807b75219/" target="_blank">
    <img src="https://github.com/abhichris63/Algerian_Forest_Fires_Prediction/assets/95648648/e824922c-5b16-4cf4-a183-f43b3f8e280b" width="70" height="20" />
</a>


<h3>Technologies Used</h3>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![FLASK](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MONGODB ATLAS](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![PANDAS](https://img.shields.io/badge/Pandas-darkblue?style=for-the-badge&logo=pandas&logoColor=white)
![NUMPY](https://img.shields.io/badge/Numpy-orange?style=for-the-badge&logo=Numpy&logoColor=black)
![Matplotlib](https://img.shields.io/badge/Matplotlib-grey?style=for-the-badge&logo=Matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-red?style=for-the-badge&logo=Seaborn&logoColor=white)


<h3>IDE</h3>

![Visual Studio Code](https://img.shields.io/badge/VisualStudioCode-blue?style=for-the-badge&logo=VisualStudioCode&logoColor=white)

