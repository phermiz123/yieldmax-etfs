from dataclasses import dataclass


@dataclass
class StockCalculation:
    """
    A class for StockCalculation
    """

    declared_date: str
    payable_date: str
    after_payable_date: str
    closing_price_declared: float
    closing_price_payable: float
    closing_price_after_payable: float
    percentage_change_payable: float
    percentage_change_after_payable: float
