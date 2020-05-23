import unittest


class TestTrade(unittest.TestCase):
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
    add_trade_url = "http://127.0.0.1:8000/trade/add"

    def test_add_trade(self):
        from requests import post
        from json import dumps
        data = post(self.add_trade_url, data=dumps(self.info)).json()
        print(f"receive: {data}")
        assert data["code"] == 200


if __name__ == '__main__':
    unittest.main()
