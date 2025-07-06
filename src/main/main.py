from dotenv import load_dotenv
import os
from pathlib import Path


from src.main.utils.csv_util import CSVUtil
from src.main.services.stock_calculator_service import StockCalculatorService


def main() -> None:
    load_dotenv()  # Load environment variables from .env file

    distribution_details_path = Path("src/resources/distribution-details.csv")
    distribution_details = CSVUtil.load_distribtution_details(
        distribution_details_path.resolve()
    )

    open_market_dates_path = Path("src/resources/us_stock_market_open_days.csv")
    open_market_dates = CSVUtil.load_open_market_dates(open_market_dates_path.resolve())

    stock_calculator_service = StockCalculatorService(
        ticker="MSTY",
        distributions=distribution_details,
        market_open_dates=open_market_dates,
    )

    stock_calculations = []
    for detail in distribution_details:
        stock_calculation = stock_calculator_service.calculate_percentage_difference(
            detail
        )
        stock_calculations.append(stock_calculation)

    CSVUtil.write_stock_calculations_to_csv(
        file_path="src/resources/stock_calculations.csv",
        stock_calculations=stock_calculations,
    )


if __name__ == "__main__":
    main()
