import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from scipy.stats import linregress, pearsonr

# Load your dataset
data = pd.read_json('data.json')

#HeatMap-Pesticide imports
complete_e = pd.read_csv('Heat_map/complete_e.csv')
outlier_e = pd.read_csv('Heat_map/outlier_e.csv')
q1_e = pd.read_csv('Heat_map/q1_e.csv')
q2_e = pd.read_csv('Heat_map/q2_e.csv')
q3_e = pd.read_csv('Heat_map/q3_e.csv')
q4_e = pd.read_csv('Heat_map/q4_e.csv')


cumulative = pd.read_csv('GDP_m/cumulative_df.csv')
c_summary = pd.read_csv('GDP_m/cumulative_summary_stats.csv')
Main_m = pd.read_csv('GDP_m/Main_m.csv')

co2_crop_j = pd.read_csv('Crop_j/co2_crop_j.csv')
merged_j = pd.read_csv('Crop_j/merged_j.csv')


# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("CO2 Emissions Dashboard & Correlation Analysis"),

    # Section 1: General CO2 Emissions Dashboard
    html.H2("General CO2 Emissions Dashboard"),
    
    html.Div([
        html.Label('Select Country:'),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in data['Area'].unique()],
            value='Afghanistan'
        ),
        html.Label('Select Data:'),
        dcc.Dropdown(
            id='data-dropdown',
            options=[
                {'label': 'Total Emission', 'value': 'total_emission'},
                {'label': 'Average Temperature', 'value': 'Average Temperature °C'},
                {'label': 'Manure Management', 'value': 'Manure Management'},
                {'label': 'Fertilizers Manufacturing', 'value': 'Fertilizers Manufacturing'},
                {'label': 'Rice Cultivation', 'value': 'Rice Cultivation'},
                {'label': 'Forest Fires', 'value': 'Forest fires'},
                {'label': 'Savanna Fires', 'value': 'Savanna fires'}
            ],
            value='total_emission'
        )
    ], style={'width': '45%', 'display': 'inline-block'}),

    html.Div([
        html.Label('Select Visualization Type:'),
        dcc.Dropdown(
            id='chart-dropdown',
            options=[
                {'label': 'Line Chart', 'value': 'line'},
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Scatter Plot', 'value': 'scatter'},
                {'label': 'Stacked Bar Chart', 'value': 'stacked_bar'},
                {'label': 'Area Chart', 'value': 'area'}
            ],
            value='line'
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding-left': '5%'}),

    # Graph to display the general data visualizations
    dcc.Graph(id='graph'),

    # Second visualization - Scatter plot to show correlation between temperature and emissions
    dcc.Graph(id='scatter-plot'),

    # Section 2: CO2 Emissions Correlation Dashboard
    html.H2("CO2 Emissions Correlation Dashboard"),

    # First Section: CO2 Emissions vs. Forest Fires & Savanna Fires
    html.H3("CO2 Emissions vs. Forest Fires & Savanna Fires"),
    dcc.Graph(id='fires-emissions-graph'),

    # Second Section: CO2 Emissions vs. Industrial Activities (Manure Management, Fertilizer Production)
    html.H3("CO2 Emissions vs. Industrial Activities"),
    dcc.Graph(id='industry-emissions-graph'),

    #Creation of scatter plots based on co2 and crop type
    html.Div([
        html.Label('CO2 emissions by crop type'),
        dcc.Dropdown(
            id='crop-emissions-dropdown',
            options = [
                {'label':'Select Crop', 'value': 'None'},
                {'label': 'World', 'value': 'world'},
                {'label':'Coffee', 'value': 'Coffee'},
                {'label': 'Vegetables', 'value':'Vegetables'},
                {'label': 'Barley', 'value': 'Barley'},
                {'label': 'Rice', 'value': 'Rice'},
                {'label': 'Cotton', 'value': 'Cotton'},
                {'label': 'Sugarcane', 'value': 'Sugarcane'},
                {'label': 'Wheat', 'value': 'Wheat'},
                {'label': 'Fruits', 'value': 'Fruits'},
                {'label': 'Corn', 'value': 'Corn'},
                {'label': 'Soybeans', 'value': 'Soybeans'}

            ],
            value = 'world'
        ),
    ], style={'width': '45%', 'display': 'inline-block'}),
    html.H3("CO2 Emissions by crop type"),
    dcc.Graph(id='crop-emissions-scatter'),
    dcc.Markdown(id='correlation--crop-coefficient'),  # New component to display text



     #Creation of Heatmap based on pesticides
     html.Div([
        html.Label('Correlation Heatmaps/Pesticides:'),
        dcc.Dropdown(
            id='correlation-heatmap-dropdown',
            options = [
                {'label':'Select Variables', 'value': 'None'},
                {'label':'World', 'value': 'world'},
                {'label': 'Outlier', 'value':'outlier'},
                {'label': 'Q1', 'value': 'q1'},
                {'label': 'Q2', 'value': 'q2'},
                {'label': 'Q3', 'value': 'q3'},
                {'label': 'Q4', 'value': 'q4'}
            ],
            value = 'world'
        ),
    ], style={'width': '45%', 'display': 'inline-block'}),
    html.H3("Pesticide Correlation Heatmaps"),
    dcc.Graph(id='correlation-pest-chart'),

    #Creation of Scatter plots based on pesticides
     html.Div([
        html.Label('Scatter Plots/Pesticides:'),
        dcc.Dropdown(
            id='scatter-pest-dropdown',
            options = [
                {'label':'Select Variables', 'value': 'None'},
                {'label':'World', 'value': 'world'},
                {'label': 'Outlier', 'value':'outlier'},
                {'label': 'Q1', 'value': 'q1'},
                {'label': 'Q2', 'value': 'q2'},
                {'label': 'Q3', 'value': 'q3'},
                {'label': 'Q4', 'value': 'q4'}
            ],
            value = 'world'
        ),
    ], style={'width': '45%', 'display': 'inline-block'}),
    html.H3("Pesticide Scatter Plots"),
    dcc.Graph(id='scatter-pest-figure'),
    dcc.Markdown(id='correlation--pest-coefficient'),  # New component to display text

    
    #Creation of CO2 emissions by country with GDP quartiles
    html.Div([
        html.Label('CO2 Emissions by Country'),
        dcc.Dropdown(
            id='co2-emissions-dropdown',
            options = [
                {'label':'Select Quartile', 'value': 'None'},
                {'label':'Q1', 'value': 'q1'},
                {'label': 'Q2', 'value':'q2'},
                {'label': 'Q3', 'value': 'q3'},
                {'label': 'Q4', 'value': 'q4'}
            ],
            value = 'q1'
        ),
    ], style={'width': '45%', 'display': 'inline-block'}),
    html.H3("CO2 Emissions based on GDP Quartile"),
    dcc.Graph(id='co2-emissions-graph'),


    
])




# Callback to update the main general dashboard graph based on dropdown selections
@app.callback(
    Output('graph', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('data-dropdown', 'value'),
     Input('chart-dropdown', 'value')]
)
def update_graph(selected_country, selected_data, selected_chart_type):
    # Filter the data based on country selection
    filtered_data = data[data['Area'] == selected_country]

    if filtered_data.empty:
        # Fallback if no data is available
        return {
            'layout': {
                'xaxis': {'visible': False},
                'yaxis': {'visible': False},
                'annotations': [{
                    'text': 'No data available for the selected options',
                    'xref': 'paper',
                    'yref': 'paper',
                    'showarrow': False,
                    'font': {'size': 20}
                }]
            }
        }

    # Generate the figure based on the selected chart type
    if selected_chart_type == 'line':
        fig = px.line(filtered_data, x='Year', y=selected_data, title=f'{selected_data} Over Time for {selected_country}')
    elif selected_chart_type == 'bar':
        fig = px.bar(filtered_data, x='Year', y=selected_data, title=f'{selected_data} Over Time for {selected_country}')
    elif selected_chart_type == 'scatter':
        fig = px.scatter(filtered_data, x='Year', y=selected_data, title=f'{selected_data} Over Time for {selected_country}')
    elif selected_chart_type == 'stacked_bar':
        fig = px.bar(filtered_data, x='Year', y=['Manure Management', 'Fertilizers Manufacturing', 'Forest fires', 'Savanna fires'], 
                     title=f'Stacked Emissions Breakdown for {selected_country}', barmode='stack')
    elif selected_chart_type == 'area':
        fig = px.area(filtered_data, x='Year', y=['Manure Management', 'Fertilizers Manufacturing', 'Forest fires', 'Savanna fires'], 
                      title=f'Area Chart of Emissions Breakdown for {selected_country}')
    else:
        fig = {}

    return fig

# Callback for CO2 Emissions vs. Forest Fires & Savanna Fires
@app.callback(
    Output('fires-emissions-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_fires_emissions_graph(selected_country):
    filtered_data = data[data['Area'] == selected_country]
    fig = px.line(filtered_data, x='Year', 
                  y=['total_emission', 'Forest fires', 'Savanna fires'],
                  labels={'value': 'CO2 Emissions and Fires', 'variable': 'Type'},
                  title=f'CO2 Emissions vs. Forest Fires & Savanna Fires for {selected_country}')
    return fig

# Callback for CO2 Emissions vs. Industrial Activities
@app.callback(
    Output('industry-emissions-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_industry_emissions_graph(selected_country):
    filtered_data = data[data['Area'] == selected_country]
    fig = px.line(filtered_data, x='Year', 
                  y=['total_emission', 'Manure Management', 'Fertilizers Manufacturing'],
                  labels={'value': 'CO2 Emissions and Industrial Activities', 'variable': 'Type'},
                  title=f'CO2 Emissions vs. Industrial Activities for {selected_country}')
    return fig

# Callback to create a scatter plot to show correlation between temperature and total emissions
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_scatter(selected_country):
    filtered_data = data[data['Area'] == selected_country]
    fig = px.scatter(filtered_data, x='Average Temperature °C', y='total_emission',
                     title=f'Correlation between Temperature and Emissions for {selected_country}')
    return fig


#Callback for the new chart based on HeatMap correlation
@app.callback(
    Output('correlation-pest-chart', 'figure'),
    [Input('correlation-heatmap-dropdown', 'value')]
)
def update_pest_corr(selected_option):
    if selected_option =='world':
        worker_df = complete_e.drop(columns=['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier', 'Agri_Land_sq_km', 'Ag_perc_land',
                                                'Ag_perc_GDP'])
        # worker_df = complete_e

    elif selected_option == 'outlier':
        worker_df = outlier_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier', 'Agri_Land_sq_km', 'Ag_perc_land',
                                                'Ag_perc_GDP'])
        # worker_df = outlier_e
    elif selected_option == 'q1':
        worker_df = q1_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier', 'Agri_Land_sq_km', 'Ag_perc_land',
                                                'Ag_perc_GDP', 'Quartile'])
        # worker_df = q1_e
    elif selected_option == 'q2':
        worker_df = q2_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier', 'Agri_Land_sq_km', 'Ag_perc_land',
                                                'Ag_perc_GDP', 'Quartile'])
        # worker_df = q2_e

    elif selected_option == 'q3':
        worker_df = q3_e.drop(columns = ['Code', 'Year', 'Country', 'Agri_Land_sq_km', 'Ag_perc_land',
                                                'Ag_perc_GDP', 'Quartile'])
        
        # worker_df = q3_e
    elif selected_option == 'q4':
        worker_df = q4_e.drop(columns = ['Code', 'Year', 'Country', 'Agri_Land_sq_km', 'Ag_perc_land',
                                                'Ag_perc_GDP', 'Quartile'])
        # worker_df = q4_e
    else: 
        
        return px.imshow([])


     #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
    corr_matrix_df = worker_df
    corr_mat = corr_matrix_df.corr()
    # Generate a heatmap
    fig = px.imshow(corr_mat, title = 'Correlation Matrix World',
                    labels=dict(x='Variables', y='Variables'),
                    color_continuous_scale='sunset',
                    zmin=-1, zmax=1)
     # Add annotations
    for i in range(len(corr_mat.columns)):
        for j in range(len(corr_mat.columns)):
             fig.add_annotation(
                x=j,
                y=i,
                text=f'{corr_mat.iloc[i, j]:.2f}',
                font=dict(color='white' if abs(corr_mat.iloc[i, j]) > 0.5 else 'black'),
                showarrow=False
            )
            
    
    return fig

#Callback for the new chart based on co2_emissions and pesticides with quartiles of GDP
@app.callback(
    [Output('scatter-pest-figure', 'figure'),
     Output('correlation--pest-coefficient', 'children')],
    [Input('scatter-pest-dropdown', 'value')]
)
def update_pest_emissions_m(selected_option):
    if selected_option =='world':
        worker_df = complete_e

    elif selected_option == 'outlier':
        worker_df = outlier_e

    elif selected_option == 'q1':
        worker_df = q1_e

    elif selected_option == 'q2':
        worker_df = q2_e

    elif selected_option == 'q3':
        worker_df = q3_e

    elif selected_option == 'q4':
        worker_df = q4_e

    else: 
        return px.imshow([])
    
    


    x_axis = worker_df['Total_Pesticides']
    y_axis = worker_df['CO2_Emissions']

    # Linear regression
    slope, intercept, r, p, std_err = linregress(x_axis, y_axis)
    line = slope * x_axis + intercept

    fig = px.scatter(
        worker_df,
        x='Total_Pesticides',
        y = 'CO2_Emissions',
        title= f"CO2 Emissions vs. Pesticide Usage",
        labels = {'Total_Pesticides': 'Pest', 'CO2_Emissions': 'CO2'}
    )

    #Add Regression line
    fig.add_scatter(
        x=x_axis,
        y=line,
        mode='lines',
        name='Regression Line',
        line=dict(color='red', dash = 'dash')
    )
        
    # Pearson correlation coefficient
    correlation_coefficient = round(pearsonr(x_axis,y_axis)[0],2)


    return fig, f"The correlation coefficient between CO2 Emissions and Pesticide use is **{correlation_coefficient}**"


#Callback for the new chart based on co2 emissions with GDP screening
@app.callback(
    Output('co2-emissions-graph', 'figure'),
    [Input('co2-emissions-dropdown', 'value')]
)
def update_co2_emissions_m(selected_option):
    q_countries_df = pd.DataFrame()

    co2_25_percent = c_summary.loc[1, 'co2_emissions']
    co2_50_percent = c_summary.loc[2, 'co2_emissions']
    co2_75_percent = c_summary.loc[3, 'co2_emissions']

    q1_m = cumulative.loc[(cumulative["co2_emissions"] > co2_25_percent)]
    q2_m = cumulative.loc[(cumulative["co2_emissions"] <= co2_25_percent) & (cumulative["co2_emissions"] < co2_50_percent)] 
    q3_m = cumulative.loc[(cumulative["co2_emissions"] <= co2_50_percent) & (cumulative["co2_emissions"] < co2_75_percent)]
    q4_m = cumulative.loc[(cumulative["co2_emissions"] >= co2_75_percent)]



    if selected_option == 'q1':
        q_countries_df = q1_m
    elif selected_option == 'q2':
        q_countries_df = q2_m
    elif selected_option == 'q3':
        q_countries_df = q3_m
    elif selected_option == 'q4':
        q_countries_df = q4_m 
    else:
        fig ={}

    # Handle empty DataFrame
    if q_countries_df.empty:
        return {
            'data': [],
            'layout': {
                'title': 'No Data Available',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'CO2 Emissions (kt)'},
            }
        }
    
    # Prepare data for Plotly Express
    filtered_data = Main_m[Main_m['country'].isin(q_countries_df.country)]

    fig = px.line(
        filtered_data,
        x='year',
        y='co2_emissions',
        color='country',
        title='CO2 Emissions by Country',
        labels={'co2_emissions': 'CO2 Emissions (kt)', 'year': 'Year'}
    )

    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='CO2 Emissions (kt)',
        legend_title='Countries',
        template='plotly'
    )
    return fig
   

   


   
@app.callback(
    [Output('crop-emissions-scatter', 'figure'),
    Output('correlation--crop-coefficient', 'children')],
    [Input('crop-emissions-dropdown', 'value')]
)
def update_crop_emissions_m(crop_type):
    
    # Fixed country value
    country = 'USA'

    #Testing code for world
    if crop_type == 'world':
        filtered_df =merged_j
        x_holder = 'CO2_Emissions'
        y_holder = 'Mean_Crop_Yield_MT_per_HA'
    # Mean_Crop_Yield_MT_per_HA
    else:
        x_holder = 'CO2_Emissions_MT'
        y_holder = 'Crop_Yield_MT_per_HA'
        # Filter the DataFrame for the specific country and crop type
        filtered_df = co2_crop_j[
            (co2_crop_j['Country'] == country) &
            (co2_crop_j['Crop_Type'] == crop_type)
        ]

    if filtered_df.empty:
        empty_fig = px.scatter()  # Create an empty figure
        return empty_fig, "No data available for this option."
    
    # Get x and y data
    x = filtered_df[x_holder]
    y = filtered_df[y_holder]

    # Check if x and y have enough data points
    if len(x) < 2 or len(y) < 2:
        print("Not enough data points to perform correlation analysis.")
        return

    # Perform linear regression
    slope, intercept, r, p, std_err = linregress(x, y)
    line = slope * x + intercept
    if crop_type == 'world':
         # Create the scatter plot using Plotly Express
        fig = px.scatter(
            filtered_df,
            x='CO2_Emissions',
            y='Mean_Crop_Yield_MT_per_HA',
            title=f"CO2 Emissions vs Mean Crop Yield",
            labels={'CO2_Emissions_MT': 'CO2_Emissions', 'Crop_Yield_MT_per_HA': 'Mean_Crop_Yield_MT_per_HA'}
        )
    else:
     # Create the scatter plot using Plotly Express
        fig = px.scatter(
            filtered_df,
            x='CO2_Emissions_MT',
            y='Crop_Yield_MT_per_HA',
            title=f"CO2 Emissions vs Crop Yield for {country} ({crop_type})",
            labels={'CO2_Emissions_MT': 'CO2 Emissions (MT)', 'Crop_Yield_MT_per_HA': 'Crop Yield (MT/HA)'}
        )

    # Add the regression line
    fig.add_scatter(
        x=x,
        y=line,
        mode='lines',
        name='Regression Line',
        line=dict(color='red', dash='dash')
    )

    # Print the Pearson correlation coefficient
    correlation_coefficient = round(pearsonr(x, y)[0], 2)
    

    return fig, f"The correlation coefficient between CO2 Emissions and Crop Yield is **{correlation_coefficient}**"



if __name__ == '__main__':
    app.run_server(debug=True)



# =======================================================================================

    
   







