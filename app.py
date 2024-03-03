import dash
from dash import Dash, dcc, html, Input, Output, dash_table
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd

# Sample data for demonstration
data1 = pd.read_csv(r'F:\\COWS\\data\\insem_data\\all.csv')
data2 = pd.read_csv(r'F:\\COWS\\data\\milk_data\\totals\\milk_aggregates\\tenday.csv')
data3 = pd.read_csv(r'F:\\COWS\\data\\status\\status_col.csv')

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define dropdown options
dropdown_options = [
    {'label': 'Data 1', 'value': 'data1'},
    {'label': 'Data 2', 'value': 'data2'},
    {'label': 'Data 3', 'value': 'data3'}
]

# Define table formats
table_formats = {
    'data1': data1,
    'data2': data2,
    'data3': data3
}

# Define app layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='table-dropdown',
                options=dropdown_options,
                value='data1'
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='data-table',
                columns=[{'name': col, 'id': col} for col in table_formats['data1'].columns],
                page_size=10
            )
        ])
    ])
])

# Define callback to update data table based on dropdown selection
@app.callback(
    [Output('data-table', 'data'),
    Output('data-table', 'columns')],
    [Input('table-dropdown', 'value')]
)
def update_data_table(selected_table):

    selected_data = table_formats[selected_table]
    columns = [{'name': col, 'id': col} for col in selected_data.columns    ]
    return selected_data.to_dict('records'), columns



if __name__ == '__main__':
    app.run_server(port=8081,debug=True)
