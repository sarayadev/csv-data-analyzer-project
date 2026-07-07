# Emergency Services Analytics

A comprehensive data analytics project exploring emergency service call patterns using Python, Pandas, and interactive visualizations.

## Overview

This project analyzes the Montgomery County 911 Calls dataset to identify trends in emergency incidents, call volume, and time-based activity patterns. The goal is to transform raw emergency call records into meaningful insights through data cleaning, feature engineering, exploratory data analysis (EDA), and visualization.

The project demonstrates a complete analytics workflow commonly used by Data Analysts, Business Analysts, and Data Scientists.

---

## Project Objectives

- Analyze the distribution of emergency call types.
- Identify peak hours and days for emergency activity.
- Explore monthly and seasonal trends.
- Investigate daily call volume patterns.
- Visualize relationships between time and emergency demand.
- Develop professional data analysis and visualization skills using Python.

---

## Dataset

The dataset contains emergency call records from Montgomery County, Pennsylvania.

### Features

| Column | Description |
|----------|------------|
| lat | Latitude |
| lng | Longitude |
| desc | Emergency call description |
| zip | Zip code |
| title | Emergency category and description |
| timeStamp | Date and time of call |
| twp | Township |
| addr | Address |
| e | Dummy variable |

---

## Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn
- Plotly
- Cufflinks

### Development Environment

- Jupyter Notebook

---

## Data Preparation

Several preprocessing steps were performed before analysis:

### Timestamp Conversion

Converted timestamps into Python datetime objects for time-based analysis.

```python
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
```

### Feature Engineering

Created additional analytical features:

- Hour
- Month
- Date
- Day of Week
- Reason

```python
df['Hour'] = df['timeStamp'].dt.hour
df['Month'] = df['timeStamp'].dt.month
```

### Emergency Category Extraction

Created a new feature from the title column to classify calls by emergency type.

```python
df['Reason'] = df['title'].apply(
    lambda title: title.split(':')[0]
)
```

---

## Exploratory Data Analysis

### Emergency Call Distribution

Analyzed the frequency of:

- EMS Calls
- Fire Calls
- Traffic Incidents

This provides insight into the most common reasons emergency services are requested.

### Weekly Activity Analysis

Examined emergency activity by day of week to identify recurring demand patterns.

Questions explored:

- Which day receives the highest number of calls?
- How do emergency categories vary throughout the week?

### Monthly Trend Analysis

Analyzed emergency call volume by month to uncover seasonal trends and long-term patterns.

### Daily Call Volume

Created time-series visualizations to evaluate changes in emergency activity over time.

### Hourly Activity Analysis

Investigated peak emergency service demand throughout the day.

### Heatmap Analysis

Generated heatmaps to visualize:

- Day of Week vs Hour
- High-demand periods
- Recurring emergency activity patterns

### Cluster Analysis

Used cluster maps to identify similarities between days and hours based on call volume.

---

## Interactive Visualizations

This project incorporates Plotly interactive visualizations, allowing users to:

- Hover for detailed metrics
- Zoom into trends
- Filter categories
- Explore data dynamically

Interactive visualizations include:

- Emergency Call Distribution
- Monthly Trends
- Daily Call Volume
- Hourly Activity Analysis
- Township Call Analysis
- Interactive Heatmaps

---

## Key Findings

### Emergency Type Distribution

EMS-related incidents represent the largest share of emergency calls, followed by Traffic and Fire-related incidents.

### Peak Activity Hours

Emergency activity tends to increase during daytime and early evening hours.

### Weekly Patterns

Traffic-related calls are generally more common during weekdays, while EMS demand remains relatively consistent.

### Long-Term Trends

Call volume demonstrates recurring patterns that may be useful for operational planning and resource allocation.

---

## Skills Demonstrated

### Data Analytics

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- Data Transformation
- Trend Analysis
- Statistical Interpretation

### Python Development

- Pandas
- NumPy
- Datetime Manipulation
- GroupBy Operations
- Data Aggregation

### Data Visualization

- Matplotlib
- Seaborn
- Plotly
- Interactive Dashboards
- Heatmaps
- Cluster Maps
- Time-Series Charts

### Professional Skills

- Analytical Thinking
- Problem Solving
- Data Storytelling
- Insight Communication

## Installation

Clone the repository:

```bash
git clone https://github.com/sarayadev/emergency-services-analytics.git
```

Navigate into the project directory:

```bash
cd emergency-services-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

## Future Improvements

- Interactive Plotly Dashboard
- Geographic Mapping
- Predictive Analytics
- Machine Learning Forecasting
- Real-Time Data Integration
- Automated Reporting

---

## Requirements

```text
pandas
numpy
matplotlib
seaborn
plotly
cufflinks
jupyter
```

---

## Author

Saraya

A Python Developer and Data Analyst focused on building projects that demonstrate practical programming, data analysis, and problem-solving skills.

---

## License

This project is licensed under the MIT License.