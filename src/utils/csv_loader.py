import csv
import pandas as pd

from src.model.distribution_detail import DistributionDetail


class CSVLoader:
    """
    A utility class to load CSV files and return their content as a list of dictionaries.
    Each dictionary corresponds to a row in the CSV file, with keys as column headers.
    """

    @staticmethod
    def load_csv(file_path: str) -> list[dict]:
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
                    declared_date=CSVLoader.transform_date(row.get("declared date")),
                    ex_date=CSVLoader.transform_date(row.get("ex date")),
                    record_date=CSVLoader.transform_date(row.get("record date")),
                    payable_date=CSVLoader.transform_date(row.get("payable date")),
                )
                list_of_distribution_details.append(distribution_detail)

            return list_of_distribution_details

    @staticmethod
    def transform_date(date_str: str) -> str:
        """
        Transform a date string from 'MM/DD/YYYY' format to 'YYYY-MM-DD'.

        :param date_str: Date string in 'MM/DD/YYYY' format.
        :return: Date string in 'YYYY-MM-DD' format.
        """
        date_obj = pd.to_datetime(date_str, format="%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
