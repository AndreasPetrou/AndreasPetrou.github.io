import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)





app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("/Users/andreaspetrou/Desktop/ONS/map/map_stock_data.csv")


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="selectLevel",
                 options=[
                     {"label": "Higher", "value": 'Stock levels are higher than normal'},
                     {"label": "No Change", "value": 'Stock levels have not changed'},
                     {"label": "Lower", "value": 'Stock levels are lower than normal'},
                     {"label": "Not sure", "value": 'Not sure'},
                     {"label": "N/A", "value": 'Not applicable'}],
                 multi=False,
                 value='Stock levels are higher than normal',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_stock_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_stock_map', component_property='figure')],
    [Input(component_id='selectLevel', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The stock levels chosen are: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Level"] == option_slctd]
   # dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='country names',
        locations='Region',
        scope="europe",
        color='Level',
        hover_data=['Region', 'Level'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Region': 'Stock Level difference'},
        template='plotly_dark'
    )

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)