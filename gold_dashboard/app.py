import dash
from dash import dcc, html, Input, Output
from model import load_data, train_model, predict_date

# Load data
df = load_data("gold_price.csv")
model_fit = train_model(df)

app = dash.Dash(__name__)

app.layout = html.Div(style={"padding": "40px"}, children=[

    html.H1("Gold Price Prediction (ARIMA Model)"),

    html.H3("Select a future date"),

    dcc.DatePickerSingle(
        id="date-input",
        display_format="YYYY-MM-DD"
    ),

    html.Button("Predict", id="btn", n_clicks=0),

    html.Div(id="output", style={
        "marginTop": "20px",
        "fontSize": "22px",
        "color": "green"
    }),

    dcc.Graph(
        figure={
            "data": [{
                "x": df.index,
                "y": df["Price"],
                "type": "line",
                "name": "Gold Price"
            }],
            "layout": {"title": "Gold Price Trend"}
        }
    )
])


@app.callback(
    Output("output", "children"),
    Input("btn", "n_clicks"),
    Input("date-input", "date")
)
def predict(n, date):
    if n == 0 or date is None:
        return ""

    pred = predict_date(model_fit, df, date)

    if isinstance(pred, str):
        return pred

    return f"Predicted Gold Price for {date}: ${pred:.2f}"


if __name__ == "__main__":
    app.run(debug=True)