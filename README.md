# 📊 Megaline Prepaid Plans Revenue Analysis

## 📊 Project Overview
This project analyzes customer usage data from Megaline, a telecommunications operator offering two prepaid plans: Surf and Ultimate.
The objective is to determine which plan generates higher average revenue per customer to support strategic decisions regarding advertising budget allocation.
Using behavioral data from 500 customers, the project evaluates call duration, text messaging, and internet usage patterns through data cleaning, preprocessing, aggregation, exploratory data analysis (EDA), and statistical hypothesis testing. The final analysis provides actionable insights into customer consumption behavior and plan profitability.

## 📊 Dataset Description
The analysis integrates data from five different datasets, representing various aspects of customer usage:
- Users – Customer demographic and plan subscription data
- Calls – Call duration records
- Messages – SMS usage data
- Internet – Mobile data usage records
- Plans – Pricing details, usage limits, and overage charges
The datasets are merged and transformed to compute monthly consumption and revenue per user.

## ⚙️ Methodology
This project follows a complete data analysis workflow:
1. Data Preprocessing
- Cleaned and validated datasets from multiple sources
- Corrected data types and handled missing values
- Converted internet usage from MB to GB
- Applied Megaline billing rules:
    - Rounded call duration to full minutes
    - Rounded monthly internet consumption
- Aggregated monthly usage metrics per user:
    - Total call minutes
    - Total messages sent
    - Total internet usage (GB)
- Calculated monthly revenue per customer, including:
    - Base plan fee
    - Extra charges for exceeding usage limits

2. Exploratory Data Analysis (EDA)
- Compared user behavior across Surf and Ultimate plans
- Analyzed distribution of usage metrics (calls, messages, internet)
- Identified trends in overage charges
- Visualized consumption patterns using statistical plots

3. Hypothesis Testing
- Conducted Student’s t-tests to evaluate:
    - Revenue differences between Surf and Ultimate plans
    - Revenue differences between NY-NJ region users and users from other regions

## 📈 Project Highlights
- Integrated and transformed multiple datasets into a unified analytical structure
- Applied real-world telecom billing logic
- Performed statistical analysis to validate business hypotheses
- Generated actionable recommendations for marketing strategy

## 📈 Results
Key Findings
- Ultimate plan generates higher average monthly revenue per user
- Surf users frequently exceed usage limits, especially internet data
- Ultimate users produce more stable and predictable revenue
- Statistically significant revenue differences were confirmed between:
    - Surf vs Ultimate plans
    - NY-NJ region vs other regions

💼 Strategic Business Insight
Although the Surf plan occasionally generates high revenue through overage charges, the Ultimate plan is more consistently profitable per customer.
This suggests that Megaline’s marketing strategy should consider focusing on attracting and retaining Ultimate plan subscribers to maximize long-term revenue stability.

▶️ How to Run the Project
1.	Clone this repository: git clone  https://github.com/alangudi417/telecom-prepaid-plans-revenue.git
2.	Navigate to the project folder: cd telecom-prepaid-plans-revenue
3.	Create and activate virtual environment: python -m venv venv venv\Scripts\activate # Windows source venv/bin/activate # Mac/Linux
4.	Install dependencies: pip install -r requirements.txt
5.	Launch Jupyter Notebook: jupyter notebook
6.	Open notebooks/telecom_ revenue_analysis.ipynb