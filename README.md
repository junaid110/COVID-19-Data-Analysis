# COVID-19 Data Analysis

This project analyzes global COVID-19 data to track cases, deaths, recoveries, and vaccinations. It provides insights into the pandemic's impact and visualizes trends using interactive charts and maps.

---

## **Features**
1. **Data Cleaning and Preparation:**
   - Load and clean the dataset from [Our World in Data](https://ourworldindata.org/covid-cases).
   - Handle missing values and calculate recovery rates.

2. **Summary Statistics:**
   - Calculate total cases, deaths, vaccinations, and recovery rates by country.

3. **Visualizations:**
   - **Interactive Line Chart:** Trends of cases, deaths, and vaccinations over time for a specific country.
   - **Choropleth Map:** Total COVID-19 cases by country on a world map.
   - **Correlation Heatmap:** Relationships between cases, deaths, vaccinations, and recovery rates.

4. **Dashboard:**
   - A web-based dashboard built with `Dash` to display visualizations and summary statistics.

---

## **Tech Stack**
- **Python Libraries:**
  - `Pandas` for data manipulation.
  - `Matplotlib` and `Seaborn` for static visualizations.
  - `Plotly` for interactive visualizations.
  - `Dash` for building the dashboard.

---

## **How to Run the Project**
1. **Install Dependencies:**
   ```bash
   pip install pandas matplotlib seaborn plotly dash
