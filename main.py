from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import joblib

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("linear_regression_model.pkl")


@app.get("/")
def home():
    return {"message": "Linear Regression API is running"}


@app.get("/predict")
def predict(
    gre: float,
    toefl: float,
    lor: float,
    cgpa: float,
    research: float
):

    # Check limits
    if gre < 0 or gre > 340:
        raise HTTPException(
            status_code=400,
            detail="GRE Score must be between 0 and 340"
        )

    if toefl < 0 or toefl > 120:
        raise HTTPException(
            status_code=400,
            detail="TOEFL Score must be between 0 and 120"
        )

    if lor < 1 or lor > 5:
        raise HTTPException(
            status_code=400,
            detail="LOR Rating must be between 1 and 5"
        )

    if cgpa < 0 or cgpa > 10:
        raise HTTPException(
            status_code=400,
            detail="CGPA must be between 0 and 10"
        )

    if research != 0 and research != 1:
        raise HTTPException(
            status_code=400,
            detail="Research must be 0 or 1"
        )

    # If all values are valid, make prediction
    prediction = model.predict([
        [gre, toefl, lor, cgpa, research]
    ])

    return {
        "chance_of_admit": prediction[0]
    }