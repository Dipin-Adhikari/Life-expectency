import numpy as np
from joblib import load


class Predict:
    def __init__(self):
        print(
            """
Currently we are only available for countries like 
Australia, Brazil, Canada, China, France,
Germany, India, Italy, Japan, Mexico, Russia,
Spain, Switzerland, United Kingdom, United States."""
        )
        print("Loading Model , Please Wait a While")
        self.model = load("Life expectency predictor")
        self.countries = [
            "Australia",
            "Brazil",
            "Canada",
            "China",
            "France",
            "Germany",
            "India",
            "Italy",
            "Japan",
            "Mexico",
            "Russia",
            "Spain",
            "Switzerland",
            "United Kingdom",
            "United States",
        ]
        self.arr_data = []

    def takeinput(self):
        self.arr_data.append(int(input("Input The Year You want to know about ~# ")))
        print("Input Country Name Of which You want to know Life expentancy !")
        self.country = input("Input Country Name ~#")
        for cnt in self.countries:
            if cnt.lower() == self.country.lower():
                self.arr_data.append(1)

            else:
                self.arr_data.append(0)

    def predict(self):
        data = np.array([self.arr_data])
        self.prediction = round(self.model.predict(data)[0])
        print(f"The life expectency of {self.country}will be around {self.prediction}")


obj = Predict()
obj.takeinput()
obj.predict()
