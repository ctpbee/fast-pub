from pydantic import BaseModel
from ctpbee.constant import OrderData


class Fuzzy(BaseModel):
    app_name: str


class Order(Fuzzy):
    pass


class Cancel(Fuzzy):
    order_id: str


class Market(Fuzzy):
    typed: str


class TradeLogin(Fuzzy):
    CONNECT_INFO: dict
    INTERFACE: str
    TD_FUNC: bool
    MD_FUNC: bool
