from requests import post
from json import dumps
info = {
    "CONNECT_INFO": {
        "userid": "089131",
        "password": "350888",
        "brokerid": "9999",
        "md_address": "tcp://180.168.146.187:10131",
        "td_address": "tcp://180.168.146.187:10130",
        "product_info": "",
        "appid": "simnow_client_test",
        "auth_code": "0000000000000000",
    },
    "INTERFACE": "ctp",
    "TD_FUNC": True,
    "MD_FUNC": False,
    "app_name": "089131"
}
data = post('http://127.0.0.1:8000/trade/add', data=dumps(info)).json()
print(f"receive:  {data}")
