import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Clean the dataset
# Drop unnecessary columns and rows with missing values
df_cleaned = df[['location', 'date', 'total_cases', 'total_deaths', 'total_vaccinations']].dropna()

# Convert 'date' column to datetime format
df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])

# Display cleaned dataset
print(df_cleaned.head())

# Calculate total cases, deaths, and recoveries by country
df_summary = df_cleaned.groupby('location').agg({
    'total_cases': 'max',
    'total_deaths': 'max',
    'total_vaccinations': 'max'
}).reset_index()

# Rename columns for clarity
df_summary.rename(columns={
    'total_cases': 'Total Cases',
    'total_deaths': 'Total Deaths',
    'total_vaccinations': 'Total Vaccinations'
}, inplace=True)

# Display summary statistics
print(df_summary.head())

# Visualize trends over time for a specific country (e.g., United States)
country = "United States"
df_country = df_cleaned[df_cleaned['location'] == country]

plt.figure(figsize=(12, 6))
plt.plot(df_country['date'], df_country['total_cases'], label='Total Cases')
plt.plot(df_country['date'], df_country['total_deaths'], label='Total Deaths', color='red')
plt.plot(df_country['date'], df_country['total_vaccinations'], label='Total Vaccinations', color='green')
plt.title(f'COVID-19 Trends in {country}')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid()
plt.show()

# Compare the impact of COVID-19 across different countries
countries = ["United States", "India", "Brazil", "United Kingdom", "Germany"]
df_comparison = df_cleaned[df_cleaned['location'].isin(countries)]

plt.figure(figsize=(14, 8))
for country in countries:
    df_temp = df_comparison[df_comparison['location'] == country]
    plt.plot(df_temp['date'], df_temp['total_cases'], label=country)

plt.title('Comparison of COVID-19 Cases Across Countries')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid()
plt.show()