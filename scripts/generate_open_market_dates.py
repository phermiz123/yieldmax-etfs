import pandas as pd
import numpy as np
from pandas.tseries.holiday import (
    USFederalHolidayCalendar,
    AbstractHolidayCalendar,
    Holiday,
    nearest_workday,
    GoodFriday,
)
from pandas.tseries.offsets import CustomBusinessDay


# Define US stock market holidays (NYSE)
class USTradingCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday("NewYearsDay", month=1, day=1, observance=nearest_workday),
        Holiday(
            "MartinLutherKingJrDay", month=1, day=1, offset=pd.DateOffset(weekday=2)
        ),  # 3rd Monday in Jan
        Holiday(
            "PresidentsDay", month=2, day=1, offset=pd.DateOffset(weekday=2)
        ),  # 3rd Monday in Feb
        GoodFriday,
        Holiday(
            "MemorialDay", month=5, day=31, offset=pd.DateOffset(weekday=0)
        ),  # Last Monday in May
        Holiday("Juneteenth", month=6, day=19, observance=nearest_workday),
        Holiday("IndependenceDay", month=7, day=4, observance=nearest_workday),
        Holiday(
            "LaborDay", month=9, day=1, offset=pd.DateOffset(weekday=0)
        ),  # 1st Monday in Sep
        Holiday(
            "Thanksgiving", month=11, day=1, offset=pd.DateOffset(weekday=3)
        ),  # 4th Thursday in Nov
        Holiday("Christmas", month=12, day=25, observance=nearest_workday),
    ]


# Create custom business day with US trading holidays
us_bd = CustomBusinessDay(calendar=USTradingCalendar())

# Generate all open market days from 2024-01-01 to 2026-12-31
market_days = pd.date_range(start="2024-01-01", end="2026-12-31", freq=us_bd)

# Save to CSV
df = pd.DataFrame({"date": market_days})
df.to_csv("src/resources/us_stock_market_open_days.csv", index=False)
