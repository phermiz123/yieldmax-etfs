import csv
import pandas as pd

from src.main.model.distribution_detail import DistributionDetail
from src.main.model.stock_calcuation import StockCalculation

from dataclasses import asdict


class CSVUtil:
    """
    A utility class to load CSV files and return their content as a list of dictionaries.
    Each dictionary corresponds to a row in the CSV file, with keys as column headers.
    """

    @staticmethod
    def load_distribtution_details(file_path: str) -> list[dict]:
        """
        Load a CSV file and return its content as a list of dictionaries.

        :param file_path: Path to the CSV file.
        :return: List of dictionaries representing the CSV content.
        """

        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            list_of_distribution_details: list[DistributionDetail] = []
            for row in reader:
                distribution_detail = DistributionDetail(
                    dividend=row.get("Distribution per Share"),
                    declared_date=CSVUtil.transform_date(row.get("declared date")),
                    ex_date=CSVUtil.transform_date(row.get("ex date")),
                    record_date=CSVUtil.transform_date(row.get("record date")),
                    payable_date=CSVUtil.transform_date(row.get("payable date")),
                )
                list_of_distribution_details.append(distribution_detail)

            return list_of_distribution_details

    @staticmethod
    def load_open_market_dates(file_path: str) -> dict[str, str]:
        """
        Load a CSV file containing market open dates and return them as a list of strings.

        :param file_path: Path to the CSV file.
        :return: dict of market open dates as key and next open day as value.
        """
        df = pd.read_csv(file_path)
        list_of_open_dates = df["date"].tolist()

        dict_of_open_dates = {}
        for i in range(0, len(list_of_open_dates) - 1):
            current_date = list_of_open_dates[i]
            next_open_date = list_of_open_dates[i + 1]
            dict_of_open_dates[current_date] = next_open_date

        return dict_of_open_dates

    @staticmethod
    def write_stock_calculations_to_csv(
        file_path: str, stock_calculations: list[StockCalculation]
    ) -> None:
        """
        Write stock calculations to a CSV file.

        :param file_path: Path to the CSV file.
        :param stock_calculations: List of stock calculations to write.
        """
        with open(file_path, mode="w", encoding="utf-8", newline="") as csvfile:
            fieldnames = [
                "declared_date",
                "payable_date",
                "closing_price_declared",
                "closing_price_payable",
                "percentage_change",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for calculation in stock_calculations:
                writer.writerow(asdict(calculation))

    @staticmethod
    def transform_date(date_str: str) -> str:
        """
        Transform a date string from 'MM/DD/YYYY' format to 'YYYY-MM-DD'.

        :param date_str: Date string in 'MM/DD/YYYY' format.
        :return: Date string in 'YYYY-MM-DD' format.
        """
        date_obj = pd.to_datetime(date_str, format="%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
