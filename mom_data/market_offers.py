from mom_data.market_offer_data import MarketOfferData
import psycopg2

from datetime import datetime, time, timedelta
from pprint import pprint


class MarketOffers:

    params: dict = {}
    current_datetime: datetime

    offers: list = []

    def __init__(self, envs: dict, marketOfferData: MarketOfferData) -> None:
        self.params = envs
        cur_date = datetime(
            marketOfferData.year, marketOfferData.mon, marketOfferData.day
        )

        for i in range(marketOfferData.start_hour, marketOfferData.last_hour):
            cur_time = time(i, 0)
            current_datetime = datetime.combine(cur_date, cur_time)
            current_date = current_datetime.date()
            date_number = (
                current_datetime
                - timedelta(hours=marketOfferData.utc_diff, minutes=0)
            ).strftime("%Y%m%d%H%M")
            interval = i + 1
            item = (
                marketOfferData.program_id,
                74,
                marketOfferData.product_id,
                marketOfferData.portfolio_id,
                date_number,
                "N",
                1,
                1,
                "$MWH",
                0,
                "MW",
                None,
                100,
                "P",
                0,
                current_date,
                interval,
                current_datetime,
                current_date,
                interval,
                current_datetime,
            )
            self.offers.append(item)

        pprint(self.offers)

    def insert_market_offers(self):

        """insert multiple vendors into the market_offer table"""
        sql = """INSERT INTO oms_market_offer(oms_program_id,
                             oms_offer_state_id, oms_product_id, oms_portfolio_id,
                             utc_timestamp_number, offered_yn, program_band_number,
                             price, price_uom, volume, volume_uom, offer_id, 
                             band_volume_allocation, band_allocation_method, 
                             site_offer_volume, program_date, program_interval,
                             program_timestamp, local_date, local_interval,
                             local_timestamp) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        conn = None
        try:
            # read database configuration

            # connect to the PostgreSQL database
            print(f"Try to connect... {self.params}")

            conn = psycopg2.connect(**self.params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.executemany(sql, self.offers)

            # pprint(cur.fetchall())

            # commit the changes to the database
            conn.commit()

            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
