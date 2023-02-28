This repository contains the study projects I completed as part of the OTUS Data Science course.

You'll find a brief overview of the projects below.

Please note that some of the commentary in the code and project reports is in Russian, as it was sometimes easier and faster for me to express my ideas in my native language. I needed to balance my regular job and course assignments with deadlines! However, I was trying to write in English as much as possible.

# Projects for Data Science course
## project_01
This is a small, mostly research-based project. The theme is Identification of Psychiatric Disorders From EEG Using Methods of Machine Learning (Идентификация психических расстройств методами машинного обучения на основе данных ЭЭГ)

I believe that it will be more convenient to check it out on Kaggle:  
- [Exploratory Data Analysis and multiclass classification](https://www.kaggle.com/code/lazygene/eda-and-multi-class-classification)  
- [Binary classification and feature importance](https://www.kaggle.com/code/lazygene/binary-classification-and-feature-importance/)
### presentation.pttx
Presentation in Russian about the project and its results

# Homework for Data Science course
## homework_01
Basic programming tasks on Python
## homework_02
Basic OOP tasks on Python + tests with pytest (test_homework_02 folder)
## homework_03
Basics of numpy, pandas and data visualisation with seaborn and matplotlib
## homework_04
Binary classification:
- EDA
- KNN
- Logistic Regression
- Cross-validation
## homework_05
Regression with Linear Regression algorithm:
- EDA
- pre-processing: missing data, categorical feature encoding, outliers, scaling, feature engineering
- L1 and L2 regularisation
- Cross-validation
- Comparison between different models with different regularisations, scaling and features
## homework_06
Binary classification with gradient boosting algorithms:
- Data Cleaning
- EDA
- Pre-processing: missing data, categorical feature encoding
- Cross-validation
- Comparison between different gradient boosting algorithms: sklearn, XGBoost, Catboost, LightGBM
- Feature importance
## homework_07
Basic linear regression on PyTorch
## homework_08
Clusterisation with K-means, Agglomerative hierarchical clustering and DBSCAN
- EDA
- Pre-processing
- Dimension reduction (PCA, t-SNE, UMAP)
- Choosing number of cluster with elbow method and silhouette score
- Results interpretation

## homework_09
Overfitting MNIST on PyTorch to understand what might lead to overfitting of FC-ANN. Practiced monitoring training progress with [WANDB](https://wandb.ai)  
In my project, I was able to overfit only using many epochs and small datasets. Experiments with larger FC-ANN led to poor model performance overall:  
![overfitting_fails.png](homework_09%2Foverfitting_fails.png)
