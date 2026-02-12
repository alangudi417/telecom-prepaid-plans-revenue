import pandas as pd
import numpy as np

def add_plan_information(monthly_metrics, df_users_clean, df_plans_clean):
    """
    Here we merge the monthly user metrics with plan and pricing information.
    At the end, we'll have the full data.
    """

    # Merge user plan info
    full_data = monthly_metrics.merge(
        df_users_clean[['user_id', 'city', 'plan_name']],
        on='user_id',
        how='left'
    )

    # Merge plan pricing and limits
    full_data = full_data.merge(
        df_plans_clean[['plan_name', 'minutes_included', 'messages_included',
                  'gb_per_month_included', 'usd_monthly_pay',
                  'usd_per_minute', 'usd_per_message', 'usd_per_gb']],
        on='plan_name',
        how='left'
    )

    # Reorder key columns
    cols = list(full_data.columns)
    cols.insert(1, cols.pop(cols.index('plan_name')))
    cols.insert(2, cols.pop(cols.index('usd_monthly_pay')))
    full_data = full_data[cols]

    return full_data