import pandas as pd
import numpy as np

# Define a function to calculate the revenue
def calculate_revenue(row):
    revenue = row['usd_monthly_pay']
    
    # Revenue from extra minutes
    extra_minutes = row['total_minutes'] - row['minutes_included']
    if extra_minutes > 0:
        revenue += extra_minutes * row['usd_per_minute']
    
    # Revenue from extra messages
    extra_messages = row['total_messages'] - row['messages_included']
    if extra_messages > 0:
        revenue += extra_messages * row['usd_per_message']
    
    # Revenue from extra gigabytes
    extra_gb = row['total_data_gb'] - row['gb_per_month_included']
    if extra_gb > 0:
        revenue += extra_gb * row['usd_per_gb']
    
    return revenue