from dotenv import load_dotenv
from pathlib import Path
from argparse import ArgumentParser


from src.main.utils.csv_util import CSVUtil
from src.main.services.stock_calculator_service import StockCalculatorService


def main() -> None:
    load_dotenv()  # Load environment variables from .env file
    parser = ArgumentParser(description="Stock Calculator")
    parser.add_argument(
        "-t",
        "--tickers",
        nargs="+",
        type=str,
        required=True,
        help="List of ticker symbols (e.g. MSTY AAPL TSLA)"
    )
    args = parser.parse_args()

    open_market_dates_path = Path("src/resources/us_stock_market_open_days.csv")
    open_market_dates = CSVUtil.load_open_market_dates(open_market_dates_path.resolve())

    for ticker in args.tickers:
        print(f"Processing ticker: {ticker}")
        distribution_details_path = Path(f"src/resources/distribution-details-{ticker}.csv")
        distribution_details = CSVUtil.load_distribtution_details(
            distribution_details_path.resolve()
        )

        stock_calculator_service = StockCalculatorService(
            ticker=ticker,
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
            file_path=f"src/resources/stock_calculations_{ticker}.csv",
            stock_calculations=stock_calculations,
        )


if __name__ == "__main__":
    main()
