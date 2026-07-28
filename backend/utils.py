# backend/utils.py

def get_result(prediction):
    if prediction == 1:
        return "Water is Potable"

    return "Water is Not Potable"