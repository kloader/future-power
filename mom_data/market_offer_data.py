class MarketOfferData:
    program_id: int
    product_id: int
    portfolio_id: int
    year: int
    mon: int
    day: int
    start_hour: int
    last_hour: int
    utc_diff: int

    def __init__(
        self,
        program_id,
        product_id,
        portfolio_id,
        year: int,
        mon: int,
        day: int,
        start_hour: int,
        last_hour: int,
        utc_diff: int,
    ) -> None:
        self.program_id = program_id
        self.product_id = product_id
        self.portfolio_id = portfolio_id
        self.year = year
        self.mon = mon
        self.day = day
        self.start_hour = start_hour
        self.last_hour = last_hour
        self.utc_diff = utc_diff
