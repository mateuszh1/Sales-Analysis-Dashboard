# Sales Analysis Dashboard

Interactive sales analysis dashboard built with **Python**, **Streamlit**, **Pandas** and **Matplotlib**.

## Project Overview

This project presents a simple sales analysis dashboard based on supermarket sales data.

The goal of the project is to show the full flow from raw CSV data to a cleaned dataset and an interactive dashboard.  
Users can explore sales, profit, quantity and business performance by using filters and visual charts.

## Features

- Data cleaning with Pandas
- Interactive dashboard built in Streamlit
- Filters by:
  - Segment
  - Region
  - Category
  - City
- KPI metrics:
  - Total Sales
  - Total Profit
  - Total Quantity
  - Number of Records
- Data preview and filtered table
- Sales and profit visualizations with Matplotlib

## Tech Stack

- Python
- Pandas
- Streamlit
- Matplotlib

## Project Structure

sales-analysis-dashboard/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
│
└── src/
    └── clean_data.py

# Dataset
The dataset is not included in this repository.
Download the dataset from Kaggle and place the CSV file in:
data/raw/
Expected file name:
SampleSuperstore.csv

# Data Pipeline
Raw CSV file
      ↓
Data cleaning with Pandas
      ↓
Processed CSV file
      ↓
Streamlit dashboard

# Clone the repository:

git clone https://github.com/mateuszh1/Sales-Analysis-Dashboard.git
cd Sales-Analysis-Dashboard

## The dashboard can help answer questions such as:

- Which category generates the highest sales?
- Which region has the highest profit?
- Which cities generate the most sales?
- How do sales and profit change after applying filters?