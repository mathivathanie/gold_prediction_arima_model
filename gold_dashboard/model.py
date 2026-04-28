import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def load_data(filepath):
    df = pd.read_csv(filepath)

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors="coerce")
    df = df.dropna(subset=["Date"])

    # Clean price
    df["Price"] = df["Price"].astype(str).str.replace(",", "").astype(float)

    df = df.sort_values("Date")
    df.set_index("Date", inplace=True)

    return df


def train_model(df):
    # ARIMA model
    model = ARIMA(df["Price"], order=(5,1,2))
    model_fit = model.fit()

    return model_fit


def predict_date(model_fit, df, target_date):
    last_date = df.index[-1]
    target_date = pd.to_datetime(target_date)

    # Number of days ahead
    steps = (target_date - last_date).days

    if steps <= 0:
        return "Date must be in the future"

    forecast = model_fit.forecast(steps=steps)

    return forecast.iloc[-1]