
def predict_price(input, model) : 
    """
    Predict a price of car 
    Argument: 
        - list of features :  [Present_Price, Kms_Driven2,Owner, Year, Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]
        - model     
    Returns:
        - price of the car based on the features given in inputs
    
    """
    prediction = model.predict([input])
    return round(prediction[0],2)