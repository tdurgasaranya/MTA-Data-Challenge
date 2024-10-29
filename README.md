# MTA-Data-Challenge
--- 
## MTA Open Data challenge 2024 ##
https://new.mta.info/article/mta-open-data-challenge

## Overview
The **MTA Data Challenge** project analyzes public transit data from the Metropolitan Transportation Authority (MTA) to uncover insights into subway ridership patterns. Using data analysis and visualization techniques, this project provides a deeper understanding of commuter behavior and trends, which can be valuable for transit planning, improving services, and optimizing resource allocation.

---

## Table of Contents
- [Project Objective](#project-objective)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)


---

## Project Objective
The goal of this project is to:
- Analyze MTA subway turnstile data to identify ridership trends and patterns.
- Investigate peak transit times, station activity levels, and entry/exit patterns.
- Provide visual insights that can assist in enhancing transit services and optimizing scheduling.

---

## Dataset

**Source**: https://data.ny.gov/browse?Dataset-Information_Agency=Metropolitan+Transportation+Authority

---

## Data Preprocessing
The raw dataset contains several million records, so data cleaning and preprocessing are crucial. Key steps involved:
- Removing duplicates and irrelevant columns.
- Handling cumulative entry/exit values by calculating the daily changes.
- Managing missing or erroneous data points.

The cleaned data was then aggregated by station, time, and date for further analysis.

---

## Exploratory Data Analysis (EDA) 📊
Exploratory Data Analysis was performed to gain insights into ridership patterns:
- **Ridership Trends**: Analyzed trends over time to identify peak and off-peak hours.
- **Station Activity**: Identified stations with the highest and lowest traffic.
- **Entry/Exit Patterns**: Explored differences between station entries and exits at different times of the day.

### Key Visualizations:
- **Daily Ridership Trends**: Visualized how ridership fluctuates throughout the day.
- **Top Stations by Volume**: Highlighted the busiest subway stations.
- **Weekday vs Weekend Patterns**: Analyzed the shift in ridership during weekdays vs weekends.

---

## Key Insights
The analysis led to several notable findings:
- **Peak Transit Hours**: Ridership peaks during weekday rush hours (8-9 AM, 5-7 PM), while weekends exhibit more scattered usage patterns.
- **High-Traffic Stations**: Times Sq-42 St is the busiest, followed by 34 St-Herald Sq and Grand Central-42 St, all major transit hubs in Manhattan.
Metrocard remains the dominant payment method, with a growing number of riders using OMNY.
Manhattan holds the majority of the highest ridership stations, reflecting its role as a transit hub.
- **Pandemic Impact**: There was a noticeable dip in ridership due to the COVID-19 pandemic, with recovery trends visible post-2021.

---

## Technologies Used
The following technologies were used for data analysis and visualization:
- **Python**: Main programming language for data manipulation and analysis.
- **Pandas**: Used for data cleaning and wrangling.
- **Power BI & Tableau**: Insightful visualizations.
- **SQLite Online**: For interactive data exploration and reporting.
  
---

## Future Enhancements
Potential future improvements to the project:
- **Real-Time Data Analysis**: Incorporate live data to monitor current ridership trends.
- **Predictive Modeling**: Develop models to predict future ridership based on historical trends and external factors (e.g., weather, events).
- **Interactive Dashboards**: Create interactive dashboards for real-time visualization and user-friendly exploration of ridership data.
