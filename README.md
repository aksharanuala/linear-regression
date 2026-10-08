# Linear Regression Prediction

A simple Machine Learning project that uses **Linear Regression** to make predictions from input data.

## Features

* Data preprocessing and analysis
* Linear Regression model training
* Model evaluation
* Saved trained model using Pickle
* FastAPI backend
* HTML, CSS, and JavaScript frontend
* Prediction through a web interface

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Jupyter Notebook
* FastAPI
* HTML
* CSS
* JavaScript

## Project Structure

```text
linear-regression/
│
├── linear.ipynb
├── linear_regression_model.pkl
├── main.py
├── index.html
├── style.css
├── script.js
└── README.md
```

## How It Works

The project follows these steps:

1. Load and explore the dataset.
2. Prepare the data.
3. Split the data into training and testing sets.
4. Train a Linear Regression model.
5. Evaluate the model.
6. Save the trained model as a `.pkl` file.
7. Load the saved model using FastAPI.
8. Connect the API to the frontend.
9. Enter input values and receive a prediction.

## Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

The basic equation is:

```text
y = mx + c
```

Where:

* `y` = predicted value
* `x` = input
* `m` = coefficient
* `c` = intercept

## Model

The trained model is saved as:

```text
linear_regression_model.pkl
```

This allows the trained model to be reused without training it again.

## Installation

Clone the repository:

```bash
git clone https://github.com/aksharanuala/linear-regression.git
```

Move into the project directory:

```bash
cd linear-regression
```

Install the required libraries:

```bash
pip install numpy pandas scikit-learn fastapi uvicorn
```

## Running the API

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

The API will run locally.

You can then open the frontend using `index.html`.

## Project Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Save Model
   ↓
FastAPI Backend
   ↓
Frontend
   ↓
Prediction
```

## Future Improvements

* Improve the frontend design
* Add input validation
* Display prediction results more clearly
* Add model performance metrics
* Deploy the application online

