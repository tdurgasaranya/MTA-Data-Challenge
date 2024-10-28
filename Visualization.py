import matplotlib.pyplot as plt

# Data for the subway stations
stations = [
    "Times Sq-42 St", "34 St-Herald Sq", "Grand Central-42 St", "Fulton St", "Canal St", 
    "34 St-Herald Sq", "Flushing-Main St", "42 St-Port Authority", "Bedford Av", "14 St-Union Sq"
]

ridership = [3268, 2308, 1926, 1908, 1720, 1224, 1201, 817, 766, 732]
boroughs = ["Manhattan", "Manhattan", "Manhattan", "Manhattan", "Manhattan", 
            "Manhattan", "Queens", "Manhattan", "Brooklyn", "Manhattan"]
payment_methods = ["Metrocard", "OMNY", "Metrocard", "Metrocard", "Metrocard", 
                   "Metrocard", "Metrocard", "Metrocard", "OMNY", "Metrocard"]

# Bar chart for ridership by station
plt.figure(figsize=(10, 6))
plt.barh(stations, ridership, color="skyblue")
plt.xlabel("Ridership (in thousands)")
plt.title("Top 10 Busiest Subway Stations by Ridership")
plt.gca().invert_yaxis()  # Invert y-axis to have highest ridership at the top
plt.show()



# Improved bar chart with both ridership values and payment method displayed on bars

plt.figure(figsize=(10, 6))
bars = plt.barh(stations, ridership, color="skyblue")
plt.xlabel("Ridership (in thousands)")
plt.title("Top 10 Busiest Subway Stations by Ridership and Payment Method")
plt.gca().invert_yaxis()  # Invert y-axis to have highest ridership at the top

# Adding data points on bars with payment method
for bar, value, method in zip(bars, ridership, payment_methods):
    plt.text(value + 20, bar.get_y() + bar.get_height() / 2, f'{value} ({method})', 
             va='center', ha='left', color="black", fontweight="bold")

plt.show()
