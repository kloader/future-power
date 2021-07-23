import logging
from mom_data.market_offer_data import MarketOfferData

from .config_env import ConfigEnv
from .market_offers import MarketOffers

logger = logging.getLogger(__name__)


program_id = 34
product_id = 34
portfolio_id = 36
year: int = 2021
mon: int = 6
day: int = 5
start_hour: int = 1
last_hour: int = 23
utc_diff: int = 2


def main(argv=None):

    print("Starting the scripts....")
    logging.basicConfig(level=logging.DEBUG)

    logger.info("Process started to insert market offers..")

    config_env = ConfigEnv()

    market_offer_data = MarketOfferData(
        program_id,
        product_id,
        portfolio_id,
        year,
        mon,
        day,
        start_hour,
        last_hour,
        utc_diff,
    )

    params: dict = config_env.get_params()

    market_offers: MarketOffers = MarketOffers(params, market_offer_data)

    market_offers.insert_market_offers()
