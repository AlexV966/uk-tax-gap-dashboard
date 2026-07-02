import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Output, Input, dash_table

# Load data
dashboard_data = pd.read_csv('/Users/alexandruvasile/Desktop/dashboard_data.csv')

# Initialise dashboard
app = Dash()

# Prepare table data
table_df = dashboard_data.copy()
table_df.columns = [col.replace("_", " ").title() for col in table_df.columns]

# Build dashboard
app.layout = html.Div(style={"fontFamily": "Arial, sans-serif", "maxWidth": "1200px", "margin": "0 auto", "padding": "20px"}, children=[
    html.H1("UK Tax Gap vs Income Dashboard (2006–2024)"),
    html.P("Explore the relationship between median annual earnings and the total tax gap year by year."),
    html.Hr(),

    # --- Scatter plot ---
    dcc.Graph(
        id="scatter-plot",
        figure={},
        style={"height": "550px"}
    ),

    html.P("Colour points by:"),
    dcc.RadioItems(
        id="colour-options",
        options=[
            {"label": "Income YoY % Change", "value": "income_yoy_pct"},
            {"label": "Tax Gap YoY % Change", "value": "taxgap_yoy_pct"},
            {"label": "Year",                 "value": "year"}
        ],
        value="year",
        style={"marginBottom": "40px"}
    ),

    html.Hr(),

    # --- Data table ---
    html.H2("Cleaned Dataset"),
    html.P("The table below shows the full cleaned dataset used in this dashboard."),
    dash_table.DataTable(
        id="data-table",
        columns=[{"name": col, "id": col} for col in table_df.columns],
        data=table_df.to_dict("records"),
        page_size=10,
        sort_action="native",
        filter_action="native",
        style_table={"overflowX": "auto"},
        style_header={
            "backgroundColor": "#2c3e50",
            "color": "white",
            "fontWeight": "bold",
            "textAlign": "left",
            "padding": "10px"
        },
        style_cell={
            "textAlign": "left",
            "padding": "8px",
            "fontFamily": "Arial, sans-serif",
            "fontSize": "14px"
        },
        style_data_conditional=[
            {"if": {"row_index": "odd"}, "backgroundColor": "#f2f2f2"}
        ]
    ),

    html.Hr(),

    # --- Insights section ---
    
    html.H2("Key Insights"),
    html.Div(style={"backgroundColor": "#f9f9f9", "padding": "20px", "borderRadius": "8px", "border": "1px solid #ddd"}, children=[
        html.H4("What the axes show"),
    html.P("Each dot is one year. Its horizontal position (x-axis) is that year's median annual earnings, and its vertical position (y-axis) is the total tax gap in £bn. So dots further right = higher wages, dots further up = bigger tax gap."),

    html.H4("The overall trend"),
    html.P("The dots form a rough upward slope from left to right — as earnings have grown over time, the tax gap has also generally grown. 2023 and 2024 sit at the top right, with both the highest wages and the biggest tax gap (around £46–47bn)."),

    html.H4("The colour (Income YoY %)"),
    html.P("The colour scale shows how fast income grew that year. Yellow/orange dots (2022, 2023, 2024) had fast income growth — those are the post-COVID years where wages surged. Dark purple dots (2010, 2012) had near-zero or negative income growth — the austerity years after the 2008 financial crisis."),

    html.H4("Outliers"),
    html.Ul([
        html.Li("2020 sits unusually high for its earnings level — the tax gap spiked during COVID despite wages barely moving, likely due to disrupted tax collection."),
        html.Li("2010 is the lowest dot overall — earnings actually fell slightly that year (dark purple) and the tax gap was at its smallest."),
        html.Li("2014 appears above the trend line — the tax gap jumped to £36.5bn while earnings were still relatively modest at £22k."),
    ]),

    html.H4("Conclusion"),
    html.P("There is a loose correlation that requires further research. Earnings and the tax gap have broadly risen together, but the tax gap has accelerated sharply since 2022 while income growth, though faster, hasn't kept pace."),
    ]),
])


@app.callback(
    Output(component_id="scatter-plot", component_property="figure"),
    Input(component_id="colour-options", component_property="value")
)
def update_scatter(colour_by):
    df = dashboard_data.dropna().copy()
    df["year"] = df["year"].astype(str)

    fig = px.scatter(
        data_frame=df,
        x="median_annual_earnings_gbp",
        y="total_tax_gap_bn",
        color=colour_by,
        text="year",
        title="Median Annual Earnings vs Total Tax Gap",
        labels={
            "median_annual_earnings_gbp": "Median Annual Earnings (£)",
            "total_tax_gap_bn": "Total Tax Gap (£bn)",
            "income_yoy_pct": "Income YoY %",
            "taxgap_yoy_pct": "Tax Gap YoY %",
            "year": "Year"
        },
        hover_data=["year", "income_yoy_pct", "taxgap_yoy_pct"]
    )
    fig.update_traces(textposition="top center", marker=dict(size=10))
    return fig


# Run
if __name__ == '__main__':
    app.run(debug=True)