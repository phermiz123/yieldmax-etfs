from dataclasses import dataclass


@dataclass
class StockCalculation:
    """
    A class for StockCalculation
    """

    declared_date: str
    payable_date: str
    closing_price_declare: float
    closing_price_payable: float
    percentage_change: float
