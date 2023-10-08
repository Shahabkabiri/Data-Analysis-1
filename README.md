# Financial Data Processing

This Python script is designed to process financial data from multiple files and perform various data manipulation tasks. The code is written to load, filter, and aggregate financial data from different sources into a unified dataset. It focuses on handling date and time data efficiently for financial analysis.

## Prerequisites

- Python
- pandas

## Usage

1. Clone this repository.
2. Modify the script's variables at the beginning of the file to specify your file paths and date range settings.
   - Update the file paths to point to your own financial data files.
   - Adjust the `start_date` and `end_date` variables to set your desired date range.
3. Run the script.

## Description

This script does the following:

- Loads financial data from multiple CSV files.
- Concatenates the data into a single dataframe.
- Converts date and time columns into datetime objects for easier manipulation.
- Filters the data to keep only records within a specified date range.
- Sets the datetime column as the index of the dataframe.
- Resamples the data into 15-minute intervals and aggregates OHLC (Open, High, Low, Close) data.

The resulting processed data can be used for various financial analysis tasks, such as time series analysis or charting.

## License

This project is licensed under the [MIT License](LICENSE).
