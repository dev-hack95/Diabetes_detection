from pydantic import BaseModel

class datat(BaseModel):
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float 
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float