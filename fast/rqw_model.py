from pydantic import BaseModel


class Fuzzy(BaseModel):
    app_name: str


class Order(Fuzzy):
    pass


class Cancel(Fuzzy):
    order_id: str


class Market(Fuzzy):
    typed: str

