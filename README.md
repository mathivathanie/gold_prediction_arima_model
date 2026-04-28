# Gold Dashboard

A time series forecasting application that predicts gold prices using ARIMA (AutoRegressive Integrated Moving Average) modeling.

## Features

- **Data Loading**: Reads historical gold price data from CSV files
- **Data Cleaning**: Handles date parsing and price formatting
- **ARIMA Modeling**: Trains an ARIMA(5,1,2) model on historical prices
- **Price Forecasting**: Predicts gold prices for future dates
- **Interactive Dashboard**: Visual interface to display historical trends and price predictions

## Requirements

- Python 3.7+
- pandas
- statsmodels

## Installation

1. Clone the repository:
```
git clone <your-repo-url>
cd gold_dashboard
```

2. Install dependencies:
```
pip install pandas statsmodels
```

## Usage

```python
from gold_dashboard.model import load_data, train_model, predict_date

# Load data
df = load_data('path/to/your/data.csv')

# Train the model
model = train_model(df)

# Predict price for a specific date
predicted_price = predict_date(model, df, '2026-05-15')
print(f"Predicted gold price: ${predicted_price:.2f}")
```

## Dataset

The model was trained using 5 years of daily gold price data (2020-2025). The dataset was downloaded from [Investing.com - Gold Historical Data](https://in.investing.com/commodities/gold-historical-data).

## Project Structure

```
gold_dashboard/                  
├── gold_dashboard/
│   ├── model.py             # streamlit dashboard
│   └── app.py               # arima model
|   └── gold_price           # Historical gold price data
├── README.md                   
```

## Contributing

Feel free to fork and submit pull requests for any improvements.

## License

MIT License
