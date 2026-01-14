
# chapter 11: APIs
from fastapi import FastAPI
from trendline import country_trendline, TrendlineInput, fit_trendline
import requests

# intialise app
app = FastAPI()

# adding a get endpoint
@app.get("country_trendline/{country}")
def calculate_country_trendline(country: str):
    slope, r_squared = country_trendline(country)
    return {
        "slope": slope,
        "r_squared": r_squared
    }

# adding a post endpoint
@app.post(
        "/fit_trendline/",
        summary = "fit a trendline to any data",
        description = "provide a list of integer timestamps and a list of floats"
)
def calculate_trendline(trendline_input: TrendlineInput):
    slope, r_squared = fit_trendline(
        trendline_input.timestamps,
        trendline_input.data
    )

    return {
        "slope": slope,
        "r_squared": r_squared
    }
 # you can improve api doc by adding a summary and escription to the @app decorator arguments. check above

 # making requestsa to the API
response = requests.get("https://127.0.0.1:8000/country_trendline/Kenya")
print(response.status_code)
print(response.json())

# you can also response object in the code
url = "https://127.0.0.1:8000/country_trendline"
json_data = {
    "timestamps": [2000, 2001, 2002],
    "data": [0.5, 0.6, 0.7]
}
response = requests.post(
    url = url,
    json = json_data
)