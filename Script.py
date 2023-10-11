import pandas as pd

# Load the data from the three files into separate dataframes
df1 = pd.read_csv(r"6B 06-22.Last.txt", sep=";", names=["DateTime", "Ask", "Bid", "Last", "Volume"])
df2 = pd.read_csv(r"6B 09-22.Last.txt", sep=";", names=["DateTime", "Ask", "Bid", "Last", "Volume"])
df3 = pd.read_csv(r"6B 12-22.Last.txt", sep=";", names=["DateTime", "Ask", "Bid", "Last", "Volume"])

# Concatenate the dataframes
final_df = pd.concat([df1, df2, df3], ignore_index=True, axis=0)

# Convert the DateTime column to a datetime object
final_df["DateTime"] = pd.to_datetime(final_df["DateTime"], format="%Y%m%d %H%M%S %f")

# Filter out rows outside desired date range
start_date = pd.to_datetime("2022-03-28")
end_date = pd.to_datetime("2022-10-28")
final_df = final_df.loc[(final_df["DateTime"] >= start_date) & (final_df["DateTime"] < end_date)]

# Set DateTime column as the index of the DataFrame
final_df.set_index("DateTime", inplace=True)

# Save the filtered data to a new file
final_df.to_csv(r"All-Time-Filtered.txt", index=True, sep=';')

# Resample data into 15 minute intervals and aggregate OHLC data
resampled_data = final_df["Last"].resample("15T").ohlc()

# Save the resampled data to a new file
resampled_data.to_csv(r"OHLC-Time-Filtered.txt", index=True, sep=';')

# Print the resampled data
print(resampled_data.head())
