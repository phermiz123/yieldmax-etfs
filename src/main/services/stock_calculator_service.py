from src.main.model.distribution_detail import DistributionDetail
from src.main.model.stock_calcuation import StockCalculation

from polygon import RESTClient

import os


class StockCalculatorService:
    def __init__(self, ticker: str, distributions: list, market_open_dates: dict):
        self.ticker = ticker
        self.distributions = distributions
        self.ticker_calculation = []
        self.client = RESTClient(
            os.getenv("API_KEY")
        )  # Initialize the Polygon REST client with the API key
        self.market_open_dates = market_open_dates

    def calculate_percentage_difference(
        self, detail: DistributionDetail
    ) -> StockCalculation:
        """
        Calculate the percentage difference between the closing prices on the declared and payable dates.
        """
        # Placeholder for actual API calls to get closing prices

        response_declared = self.client.get_daily_open_close_agg(
            ticker=self.ticker, date=detail.declared_date
        )

        day_after_payable_date = self.market_open_dates.get(detail.payable_date, None)

        if day_after_payable_date is None:
            raise LookupError(f"No market open date found for {detail.payable_date}")

        response_after_payable = self.client.get_daily_open_close_agg(
            ticker=self.ticker, date=day_after_payable_date
        )

        percentage_change = (
            (response_after_payable.close - response_declared.close)
            / response_declared.close
        ) * 100

        return StockCalculation(
            declared_date=detail.declared_date,
            payable_date=detail.payable_date,
            closing_price_declared=response_declared.close,
            closing_price_payable=response_after_payable.close,
            percentage_difference=percentage_change,
        )
