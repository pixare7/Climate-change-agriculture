# Climate Change and Agriculture

## Overview

This project investigates the relationship between climate change and agricultural variables, focusing on how increasing CO2 emissions over time correlate with crop yields, pesticide usage, and agricultural GDP. The analysis examines CO2 emissions on national and global scales to determine how these emissions interact with a country’s agricultural profile. Key variables include crop yield, crop type, pesticide use, and gross domestic product (GDP).

## Table of Contents
1. [Overview](#overview)
2. [Project Details](#project-details)
   - [Background](#background)
   - [Goals](#goals)
   - [Methodology](#methodology)
   - [Visuals](#visuals)
   - [Interactive Dashboard](#interactive-dashboard)
3. [Conclusions](#conclusions)
4. [Future Work](#future-work)
5. [Collaborators](#collaborators)

## Project Details

### Goals
The primary objectives of this analysis are:
- To determine whether countries with higher agricultural land use have higher CO2 emissions.
- To explore the correlation between CO2 emissions and crop yield.
- To examine whether pesticide use has led to improved crop yields and reduced land use over time.
- To analyze whether countries with higher CO2 emissions utilize more pesticides in agricultural production.
- To identify the relationship between CO2 emissions and agricultural GDP.

### Methodology

1. **Data Collection:**  
   Data was sourced from [Our World in Data](https://ourworldindata.org/) and the Kaggle dataset [Climate Change Impact on Agriculture](https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture/data).

2. **Data Cleaning:**  
   Relevant columns related to CO2 emissions and agricultural variables were selected for analysis. The cleaning process involved the removal of missing data, duplicates, and renaming columns for consistency. Merging datasets required standardizing country names for compatibility.

3. **Exploratory Data Analysis (EDA):**  
   Summary statistics were generated to analyze the central tendencies and variations in crop yields per hectare. Linear regressions and Pearson’s correlation tests were conducted to examine the relationships between CO2 emissions and other variables. Time series data were also visualized to track CO2 emissions over time by country.

4. **Feature Engineering:**  
   New variables were created, such as:
   - **ag_gdp**: Agricultural GDP relative to the country's total GDP.
   - **pop_to_gdp**: Population-to-GDP ratio.
   - **pop_to_ag_gdp**: Population-to-agricultural-GDP ratio.

5. **Database Setup and Management:**  
   A MongoDB database was used to manage and store the datasets, facilitating efficient querying and analysis of key variables such as CO2 emissions, GDP, and agricultural data.

6. **Data Analysis:**  
   Correlation analysis was performed on both individual and cumulative datasets. A multiple linear regression model was built to predict CO2 emissions based on population, GDP, and agricultural GDP. Additional linear regressions analyzed the relationship between CO2 emissions and crop yield both in the USA and globally for various crops.

7. **Visualization:**  
   Various visualizations were generated, including scatter plots, line charts, and heatmaps to explore relationships among CO2 emissions, agricultural variables, and GDP quartiles.

8. **Statistical Analysis:**  
   A statistical summary was compiled, and Pearson’s correlation tests were performed. Multiple linear regression models were used to analyze trends and relationships between key variables.

9. **Tools and Libraries:**  
   - **Pandas**: Data cleaning and manipulation  
   - **Numpy**: Numerical computations  
   - **Matplotlib & Seaborn**: Visualizations  
   - **Sklearn**: Linear regression modeling  
   - **Plotly**: Interactive visualizations  
   - **Dash**: Dashboard development  
   - **Pymongo**: Database interactions  

## Visuals

### Figure 1: CO2 Emissions Over Time by Country
This line chart illustrates the trend of CO2 emissions over time for several countries. It highlights both global and regional differences in CO2 emission patterns and the impact of industrial growth in key regions.

![Figure 1](https://github.com/EdGonz44/Project-3/blob/main/images/ds1.png)

### Figure 2: Top 10 Countries by CO2 Emissions
This bar plot presents the countries with the highest CO2 emissions, showcasing their contributions relative to the rest of the world. 

![Figure 2](https://github.com/EdGonz44/Project-3/blob/main/images/ds2.png)

### Figure 3: Summary Statistics of Crop Yield
This table summarizes the central tendencies of crop yields, such as mean, standard deviation, and range. It offers insights into the variability of crop production efficiency across different countries.

<img src="https://github.com/EdGonz44/Project-3/blob/main/images/jj1.png" alt="Figure 3" width="600"/>

### Figure 4a: CO2 Emissions vs. Average Crop Yield (Global)
This scatter plot examines the relationship between CO2 emissions and average crop yields across all countries, revealing whether higher emissions correspond to better yields.

![Figure 4a](https://github.com/EdGonz44/Project-3/blob/main/images/jj2.png)

### Figure 4b: CO2 Emissions vs. Average Crop Yield by Crop Type
This scatter plot compares CO2 emissions with crop yields for specific crop types, allowing for analysis of how different crops may respond to environmental factors linked to emissions.

![Figure 4b](https://github.com/EdGonz44/Project-3/blob/main/images/jj3.png)

### Figure 5a: Pesticide Correlation Heatmap (Global)
This heatmap highlights the correlation between pesticide use and various agricultural and environmental factors globally, identifying areas of significant interaction.

![Figure 5a](https://github.com/EdGonz44/Project-3/blob/main/images/eg1.png)

### Figure 5b: Pesticide Correlation Heatmap (By Quartiles & Outliers)
This heatmap further analyzes pesticide use correlations, segmented by GDP quartiles and outliers, to explore how economic factors may influence agricultural practices.

![Figure 5b](https://github.com/EdGonz44/Project-3/blob/main/images/eg2.png)

### Figure 6a: CO2 Emissions vs. Pesticide Use (Global)
This scatter plot explores the relationship between CO2 emissions and pesticide usage on a global scale, assessing whether higher emissions correlate with increased pesticide application.

![Figure 6a](https://github.com/EdGonz44/Project-3/blob/main/images/eg3.png)

### Figure 6b: CO2 Emissions vs. Pesticide Use (By Quartiles & Outliers)
This scatter plot compares CO2 emissions with pesticide usage, divided by GDP quartiles and outliers, to provide a more granular understanding of the relationships within different economic strata.

![Figure 6b](https://github.com/EdGonz44/Project-3/blob/main/images/eg4.png)

### Figure 7: CO2 Emissions by GDP Quartile
This box plot visualizes CO2 emissions across GDP quartiles, offering insights into how wealth impacts environmental outputs in different economies.

![Figure 7](https://github.com/EdGonz44/Project-3/blob/main/images/mo1.png)

## Interactive Dashboard

1. Clone the repository.  
2. Install the required libraries:  
   ```bash
   pip install dash plotly pandas
   ```  
3. Place data files (e.g., `data.json`) in the project directory.  
4. Run the app:  
   ```bash
   python app.py
   ```  

## Conclusions
- No significant correlation was found between CO2 emissions and crop yields.
- Pesticide use and CO2 emissions show inconsistent correlations across different economic groupings.
- Strong relationships were identified between CO2 emissions, population, and agricultural GDP.
- The dataset suggests consistency in crop yields per hectare across countries, as indicated by small standard deviations and low standard error of the mean.
- The dashboard provides insights into how variables like industrial activities, forest fires, crop yield, and pesticide use impact CO2 emissions.

## Future Work
- Explore the relationship between CO2 emissions and the nutritional value of crops.
- Include additional health metrics to examine disease prevalence linked to air pollution.
- Incorporate real-time data for monitoring the effects of climate policies.
- Investigate the role of agricultural trade in CO2 emissions and food production.

## Collaborators
- **Eddie Gonzalez**: Data analysis, visualization, database and dashboard development, CO2, pesticides, and GDP analysis.
- **Dhwani Shah**: Data analysis, visualization, database and dashboard development, trend analysis.
- **Jenny Jaurequi**: Data analysis, visualization, CO2 emissions, crop yield analysis, and README development.
- **Megan O'Connor**: Secondary research, narrative development, CO2 emissions and agricultural GDP analysis.
