from src.main.model.distribution_detail import DistributionDetail
from src.main.model.stock_calcuation import StockCalculation

from polygon import RESTClient

import os
import time


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
        day_after_payable_date = self.market_open_dates.get(detail.payable_date, None)

        if day_after_payable_date is None:
            raise LookupError(f"No market open date found for {detail.payable_date}")

        response = self.list_aggs(
            start_date=detail.declared_date, end_date=day_after_payable_date
        )


        if len(response) < 3:
            raise ValueError(
                f"Expected at least 3 results, got {len(response)} for {self.ticker}"
                f"between {detail.declared_date} and {day_after_payable_date}"
            )

        closing_price_declared = response[0].close
        closing_price_payable = response[-2].close
        closing_price_after_payable = response[-1].close

        percentage_change_payable = (
            (closing_price_payable - closing_price_declared) / closing_price_declared
        ) * 100

        percentage_change_after_payable = (
            (closing_price_after_payable - closing_price_declared)
            / closing_price_declared
        ) * 100

        return StockCalculation(
            declared_date=detail.declared_date,
            payable_date=detail.payable_date,
            after_payable_date=day_after_payable_date,
            closing_price_declared=closing_price_declared,
            closing_price_payable=closing_price_payable,
            closing_price_after_payable=closing_price_after_payable,
            percentage_change_payable=percentage_change_payable,
            percentage_change_after_payable=percentage_change_after_payable,
        )

    def list_aggs(self, start_date: str, end_date: str) -> list:
        """
        Get the daily open and close aggregate for a given ticker and date.
        """
        print(f"Fetching data for {self.ticker} on {start_date} to {end_date}")
        response = []
        for a in self.client.list_aggs(
            ticker=self.ticker,
            multiplier=1,
            timespan="day",
            from_=start_date,
            to=end_date,
            adjusted=True,
            sort="asc",
            limit=120,
        ):
            response.append(a)
        time.sleep(12)  # Sleep to avoid hitting API rate limits
        return response
