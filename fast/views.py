from fast import fast_api
from ctpbee import get_app, CtpBee
from fast.rqw_model import Order, Cancel, Market, TradeLogin
from fast.response import RT


@fast_api.post("/order/route")
async def send_order(item: Order):
    return RT.true_response(data=get_app(item.app_name).send_order(item.order), message="insert order successful")


@fast_api.post("/order/cancel")
async def cancel_order(item: Cancel):
    return RT.true_response(data=get_app(item.app_name).cancel(item.order_id), message="cancel order successful")


@fast_api.post("/market/add")
async def add_market(item: Market):
    """
    注册行情提供行情
    """
    app = CtpBee(item.typed, __name__)
    app.config.from_mapping(item)
    app.start()
    return RT.true_response(data=None, message="add market successful")


@fast_api.post("/trade/add")
async def add_trade(item: TradeLogin):
    """
    增加交易账户,每日自动进行托管
    """
    app = CtpBee(item.app_name, __name__)
    app.config.from_mapping(item)
    app.start(log_output=False)
    return RT.true_response(message="add trade successful")
