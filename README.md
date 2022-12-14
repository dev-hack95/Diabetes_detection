![Title](https://user-images.githubusercontent.com/77664251/210039958-acb45b58-8a17-4232-ac67-7fd3a8e3ff6f.png)

# DIABETES DETECTION
![Python Version](https://img.shields.io/badge/Python-3.8.10-lightgrey)
![D#3](https://img.shields.io/badge/D3.js-v7.0-orange)
![Tensorflow version](https://img.shields.io/badge/Tensorflow.js-3.18.0-lightgrey)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-binary--classiification-red)

## Authors

- [@dev-hack95](https://www.github.com/dev-hack95)

## Project Status
- Complete

## Table of Contents

  - [Problem Statement](#Problem-Statement)
  - [Data source](#data-source)
  - [Methods](#methods)
  - [Tech Stack](#tech-stack)
  - [Quick glance at the results](#quick-glance-at-the-results)
  - [Run Locally](#run-locally)
  - [Explore the notebook](#explore-the-notebook)
  - [Deployment](#Deployment)
  - [Docker](#Docker)
  - [Kubernetes](#Kubernetes)
  - [Repository structure](#repository-structure)
  - [Results](#Results)
  
## Problem Statement
  - Create a machine learning model on diabetes detection
  
## Data Source
  - [Diabetes Prediction dataset](https://www.kaggle.com/datasets/vikasukani/diabetes-data-set)

## Methods

- Exploratory data analysis
- Bivariate analysis
- Multivariate correlation
- Explainable AI
- Model Comparison
- Model deployment

## Tech Stack

- Python (refer to requirement.txt for the packages used in this project)
- Tensorboard
- Javascript
- Docker
- Kubernetes
- Devops

## Quick glance at the results
Correlation between the features.

![heatmap](https://user-images.githubusercontent.com/77664251/210039991-bf26224b-b067-482b-ab43-3802e7d384a2.png)

Impact of feature

![Impact](https://user-images.githubusercontent.com/77664251/210039963-e11f3319-99c1-423c-9415-e35b337d1486.png)

Top 3 models (with default parameters)

| Model     	                |  score 	          |
|-------------------	        |------------------	|
| Gradient boosting   	      | 86% 	            |
| Random Forest    	          | 84% 	            |
| Bagging_Classifer           | 82.33% 	          |

- **The final model used for this project: Random Forest**
- **Metrics used: f1-score**
- **Lessions Learned: 1) How to handle skewness of data 2) How to deploy streamlit application on docker 3) SHAP: Explainable AI**

## Run Locally

1) Initialize git

```bash
git init
```


2) Clone the project

```bash
git clone https://github.com/dev-hack95/Diabetes_detection
```

3) enter the project directory

```bash
cd Diabetes_detection
```

4) install the requriments

```bash
pip install -r requirements.txt
```

5) run application

```bash
streamlit run app.py
```
  
#### Requriments(tensorflow.js)
   1) D3.js
    
   ```bash
   npm i d3 --save
   ```
   
   2) Alternative  is Pappaparse
   3) Tensorflow.js 
   ```bash
      npm i @tensorflow/tfjs
   ```
   
   4) Tensorflow visualation 
   ```bash
      npm i @tensorflow/tfjs-vis)
   ```

## Outputs: Prediction(@tensorflow/tf-vis)

![output](https://github.com/dev-hack95/Diabetes_detection/blob/main/Images/test.gif)

## Explore the notebook

To explore the notebook file [here](https://github.com/dev-hack95/Diabetes_detection/blob/main/ML_Dibeates_detection.ipynb)

## Deployment
## Docker
- Tool used for deployment: Docker (Raspberry pi)
- Platform used for testing of an application: [Play with Docker](https://labs.play-with-docker.com/) and lxd containers

![model](https://user-images.githubusercontent.com/77664251/210039977-89743b84-3074-4ea5-8ebc-91172c4124a1.gif)

## Kubernetes

```bash
kubectl -f apply application/deployment.yml
```


## Repository structure

![tree](https://github.com/dev-hack95/Diabetes_detection/blob/main/Images/Screenshot%20(13).png)
