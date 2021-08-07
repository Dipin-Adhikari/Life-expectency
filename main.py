from joblib import load
import numpy as np 

model = load('Life expectency predictor')
countries = ['Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Italy', 'Japan', 'Mexico', 'Russia', 'Spain', 'Switzerland', 'United Kingdom', 'United States']
arr_data = []
year = int(input("Which year you want to know?\n"))
arr_data.append(year)
print("Currently we are only available for countries like Australia, Brazil, Canada, China, France, Germany, India, Italy, Japan, Mexico, Russia, Spain, Switzerland, United Kingdom, United States.")
country = input("Which country you want to know life expectency?\n")


for cnt in countries:
    if cnt.lower() == country.lower():
        arr_data.append(1) 
    else:
        arr_data.append(0)

data = np.array([arr_data])

prediction = model.predict(data)[0]

print(f"The life expectency of {country} on {year} will be around {prediction}")