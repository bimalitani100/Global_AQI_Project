import pandas as pd


def clean_air_data(df):

    # fitting the json parameter in dataframe
    df["utc_time"] = df["datetime"].apply(lambda x: x["utc"])
    df["latitude"] = df["coordinates"].apply(lambda x: x["latitude"])
    df["longitude"] = df["coordinates"].apply(lambda x: x["longitude"])

    # dropping/removing messy columns
    df = df.drop(columns=["datetime", "coordinates"])

    # removing the null columns
    df = df.dropna()

    # renaming the columns for better understanding
    df = df.rename(columns={"value": "pollution_value"})

    return df


# for testing purposes
if __name__ == "__main__":
    from extract import get_Air_quality

    df = get_Air_quality()
    clean_df = clean_air_data(df)

    print(clean_df.head())
