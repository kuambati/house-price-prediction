import pickle
import numpy as np


with open("lineear-regression-model.pkl", "rb") as f:
    model = pickle.load(f)

print("California House Price Predictor")
print("Enter the following values:")

MedInc = float(input("Median Income: "))
HouseAge = float(input("House Age: "))
AveRooms = float(input("Average Rooms: "))
AveBedrms = float(input("Average Bedrooms: "))
Population = float(input("Population: "))
AveOccup = float(input("Average Occupancy: "))
Latitude = float(input("Latitude: "))
Longitude = float(input("Longitude: "))


input_data = np.array([[
    MedInc, HouseAge, AveRooms, AveBedrms,
    Population, AveOccup, Latitude, Longitude
]])

prediction = model.predict(input_data)

print(f"\nPredicted Median House Value: {prediction[0]:.3f}")
