import pandas as pd
import numpy as np

def calculate_user_monthly(df_calls_clean, df_messages_clean, df_internet_clean):
    """
    This function will help to calculate the user metrics: 
    - total calls
    - total minutes
    - total messages
    - total data used (GB)
    """

    # Group by calls & minutes
    minutes_calls = (
        df_calls_clean.groupby(['user_id', 'month'])['duration'].agg(total_calls='count', total_minutes='sum').reset_index()
    )

    # Group by message
    messages = (
        df_messages_clean.groupby(['user_id', 'month'])['id']
        .count()
        .reset_index(name='total_messages')
    )

    # Group by internet (GB rounded up)
    internet = (
        df_internet_clean.groupby(['user_id', 'month'])['gb_used']
        .sum()
        .reset_index(name='total_data_gb')
    )
    internet['total_data_gb'] = np.ceil(internet['total_data_gb']).astype(int)  # Rounding up gb data

    # Merging all metrics
    monthly_metrics = (
        minutes_calls
        .merge(messages, on=['user_id', 'month'], how='outer')
        .merge(internet, on=['user_id', 'month'], how='outer')
        .fillna(0)
    )

    # Making sure to keep the int format
    cols = ['total_calls', 'total_minutes', 'total_messages', 'total_data_gb']
    monthly_metrics[cols] = monthly_metrics[cols].astype(int)

    return monthly_metrics