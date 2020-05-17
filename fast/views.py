from fast import fast_api
from ctpbee import get_app, CtpBee
from fast.rqw_model import Order, Cancel, Market, TradeLogin


@fast_api.post("/order/route")
async def send_order(item: Order):
    return get_app(item.app_name).send_order(item)


@fast_api.post("/order/cancel")
async def cancel_order(item: Cancel):
    return get_app(item.app_name).cancel(item.order_id)


@fast_api.post("/market/add")
async def add_market(item: Market):
    """
    注册行情提供行情
    """
    app = CtpBee(item.typed, __name__)
    app.config.from_mapping(item)
    app.start()
    return 1


@fast_api.post("/trade/add")
async def add_trade(item: TradeLogin):
    """
    增加交易账户,每日自动进行托管
    """
    app = CtpBee(item.app_name, __name__)
    app.config.from_mapping(item)
    app.start()
    return 1
