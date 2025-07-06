from polygon import RESTClient
from dotenv import load_dotenv
import os
from pathlib import Path


from src.utils.csv_loader import CSVLoader


def main() -> None:
    # load_dotenv()  # Load environment variables from .env file
    # api_key = os.getenv("API_KEY")
    # client = RESTClient(api_key=api_key)

    # response = client.get_daily_open_close_agg(ticker="NVDA", date="2025-07-03")

    # print(response)
    distribution_details_path = Path("distribution-details.csv")
    details = CSVLoader.load_csv(distribution_details_path.resolve())

    for detail in details:
        print(detail.dividend, detail.declared_date, detail.ex_date,
              detail.record_date, detail.payable_date)


if __name__ == "__main__":
    main()
