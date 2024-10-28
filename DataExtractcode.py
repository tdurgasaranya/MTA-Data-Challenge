import pandas as pd

# Load the CSV file to examine its structure
file_path = '/mnt/data/MTA_Subway_Stations_20241019.csv'
data = pd.read_csv(file_path)

# Display the first few rows and summary info of the dataset to understand its structure
data.info(), data.head()

# Load the newly uploaded CSV file to examine its structure as well
file_path_new = '/mnt/data/MTASubwayHourlyRS.csv'
data_ridership = pd.read_csv(file_path_new)

# Display the first few rows and summary info of the new dataset to understand its structure
data_ridership.info(), data_ridership.head()
