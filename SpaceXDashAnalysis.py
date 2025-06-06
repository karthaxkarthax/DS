# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("/Users/css145296/Desktop/Content/PyDev/Certify/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()


# Create a dash application
app = dash.Dash(__name__)


# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(options=[{'label': 'CCAFS LC-40','value': 'CCAFS LC-40'}, {'label':'VAFB SLC-4E', 'value':'VAFB SLC-4E'},  {'label':'KSC LC-39A', 'value': 'KSC LC-39A'}, {'label' : 'CCAFS SLC-40', 'value' : 'CCAFS SLC-40'}, {'label': 'ALL sites', 'value': 'ALL'}], value='ALL', id='site-dropdown', placeholder="Select the interested site", searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='id', min=0, max=10000, step=1000, marks={0: '0',100: '100'},value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart', figure=px.scatter(spacex_df, x='Payload Mass (kg)', y='class', color='Booster Version'))),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df,  names='Launch Site', title='Site ratio chart')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='class', title='Success ratio chart')
        return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, entered_range):
    spacexrange_df=spacex_df[spacex_df['Payload Mass (kg)'] < entered_range]
    if entered_site == 'ALL':
        fig = px.scatter(spacexrange_df, x='Payload Mass (kg)', y='class', color='Booster Version')
        return fig
    else:
        filtered_df = spacexrange_df[spacexrange_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version')
        return fig

# Run the app
if __name__ == '__main__':
    app.run()

