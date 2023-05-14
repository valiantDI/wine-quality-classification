import joblib
import unicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
model = joblib.load('./model.joblib')


class WineSpecies(BaseModel):
    """
    Input features validation for the ML model.
    """
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


@app.post('/predict')
def predict(wine: WineSpecies):
    """
    :param wine: input data from the post request
    :return: predicted wine quality
    """
    features = [[
        wine.fixed_acidity,
        wine.volatile_acidity,
        wine.citric_acid,
        wine.residual_sugar,
        wine.chlorides,
        free_sulfur_dioxide,
        wine.total_sulfur_dioxide,
        wine.density,
        wine.pH,
        wine.sulphates,
        wine.alcohol,
    ]]
    prediction = model.predict(features).tolist()[0]
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    unicorn.run(app, host='127.0.0.1', port=80)