import requests
import pandas as pd


def get_Air_quality():
    url = "https://api.openaq.org/v3/parameters/2/latest"
    key = {
    "X-API-Key" : "d3bb8a2647b6e74077ace95fdd102baa193d903393afe7e4a1c334da9466af35"
    }
    response = requests.get(url, headers= key)

    data = response.json()

    results = data["results"]

    df = pd.DataFrame(results)

    return df


# for testing purpose only
if __name__ == "__main__":
    df = get_Air_quality()
    print(df.head())




















