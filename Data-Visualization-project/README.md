# Data Visualization Project Using Python

## Overview

This project demonstrates how to analyze and visualize data using Python. It includes simulations, probability experiments, and real-world data retrieval from APIs. The goal is to convert raw data into clear and meaningful visual representations using Python libraries.

The project is structured in a modular way and follows clean coding practices, including error handling, logging, and separation of concerns.

---

## Objectives

- Apply Python for data visualization and data analysis
- Work with real-world APIs and JSON data
- Simulate probability-based systems using randomness
- Implement error handling and retry logic for API requests
- Improve code structure using modular design principles
- Practice production-style Python development

---

## Technologies Used

- Python 3
- Matplotlib
- Plotly Express
- Plotly IO
- Requests
- Logging

---

## Project Structure

basic_visualization/
random_walk_simulation/
probability_simulation/
api_data_visualization/

---

## Project Breakdown

### 1. Basic Data Visualization

This section introduces fundamental plotting techniques using Matplotlib. Simple numerical datasets are used to generate visual representations of mathematical relationships.

Key concepts:
- Line plots
- Axis labeling
- Data visualization fundamentals
- Chart formatting and styling

---

### 2. Random Walk Simulation

This section simulates a random walk process, where each step is determined by random choices. The resulting path is visualized using a scatter plot.

Key concepts:
- Object-oriented programming
- Random number generation
- Iterative data generation
- Large dataset visualization
- Pattern recognition in randomness

---

### 3. Probability Simulation: Dice Rolls

This section simulates rolling a die multiple times to analyze the frequency distribution of outcomes.

Key concepts:
- Probability simulation
- Frequency analysis
- Data aggregation
- Statistical visualization using bar charts

---

### 4. Real-World Data Visualization (GitHub API)

This section retrieves real-world data from the GitHub API and visualizes repository popularity based on star counts.

Key Improvements Implemented:
- Retry logic for network reliability
- Timeout handling for API requests
- Structured logging for debugging and monitoring
- Defensive JSON parsing using safe access methods
- Graceful failure handling to prevent crashes
- Proper Plotly renderer configuration for environment compatibility

Key Concepts:
- REST API integration
- JSON parsing and data extraction
- Error handling (HTTP errors, timeouts, connection errors)
- Logging and debugging best practices
- Data transformation for visualization
- Production-style Python structure

---

## How to Run the Project

Install dependencies:

pip install -r requirements.txt

Run each module:

python basic_visualization/simple_plots.py
python random_walk_simulation/visualization.py
python probability_simulation/dice_analysis.py
python api_data_visualization/github_repository_analysis.py

---

## Requirements

matplotlib
plotly
requests

---

## Key Takeaways

This project demonstrates how raw data can be transformed into meaningful insights using Python. It combines simulation-based modeling with real-world API data to build practical data visualization skills.

It also introduces production-level practices such as error handling, logging, modular design, and safe API consumption.

---

## Author

Built as part of a Python learning path focused on data analysis, visualization, and machine learning foundations.