from dataclasses import dataclass


@dataclass
class DistributionDetail:
    dividend: str
    declared_date: str
    ex_date: str
    record_date: str
    payable_date: str
