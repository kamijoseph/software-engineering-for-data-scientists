
# chapter 11: APIs
from fastapi import FastAPI
from trendline import country_trendline, TrendlineInput

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