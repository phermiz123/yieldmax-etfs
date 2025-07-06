class DistributionDetail:
    def __init__(
        self,
        dividend: str,
        declared_date: str,
        ex_date: str,
        record_date: str,
        payable_date,
    ):
        self.dividend = dividend
        self.declared_date = declared_date
        self.ex_date = ex_date
        self.record_date = record_date
        self.payable_date = payable_date
