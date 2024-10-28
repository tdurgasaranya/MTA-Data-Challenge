# Merge the ridership data with the station data on the common column "Complex ID" and "station_complex_id"
# Renaming for consistency
data_ridership['station_complex_id'] = data_ridership['station_complex_id'].astype(str)
data['Complex ID'] = data['Complex ID'].astype(str)

# Merge datasets on 'Complex ID' and 'station_complex_id'
merged_data = pd.merge(data_ridership, data, left_on='station_complex_id', right_on='Complex ID', how='inner')

# Now, group by Station and aggregate ridership and payment methods
summary = merged_data.groupby(['station_complex', 'Stop Name', 'borough', 'payment_method']).agg({
    'ridership': 'sum'
}).reset_index()

# Sort to identify stations with highest ridership
summary_sorted = summary.sort_values(by='ridership', ascending=False).head(10)

summary_sorted
