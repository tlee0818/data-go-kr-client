"""Shared fixtures and response bodies for all test modules."""

FAKE_KEY = "test_api_key_1234"


GET_POWER_USAGE_SERVICE_JSON = {
    "header": {"resultCode": "00", "resultMsg": "OK"},
    "body": {
        "items": {
            "item": [
                {
                    "pwst_nm": "test_value",
                    "tag_data_nvl": "test_value",
                    "meno_nm": "test_value",
                }
            ]
        },
        "totalCount": 1,
        "pageNo": 1,
        "numOfRows": 10,
    },
}


GET_ELECTRICAL_EFFICIENCY_JSON = {
    "header": {"resultCode": "00", "resultMsg": "OK"},
    "body": {
        "items": {
            "item": [
                {
                    "pwst_nm": "test_value",
                    "tag_data_nvl": "test_value",
                    "meno_nm": "test_value",
                }
            ]
        },
        "totalCount": 1,
        "pageNo": 1,
        "numOfRows": 10,
    },
}


GET_PLANT_PERFORMANCE_PREDICTION_SERVICE_JSON = {
    "header": {"resultCode": "00", "resultMsg": "OK"},
    "body": {
        "items": {
            "item": [
                {
                    "pwst_nm": "test_value",
                    "tag_data_nvl": "test_value",
                    "meno_nm": "test_value",
                }
            ]
        },
        "totalCount": 1,
        "pageNo": 1,
        "numOfRows": 10,
    },
}


RATE_LIMIT_JSON = {"header": {"resultCode": "22", "resultMsg": "요청 제한을 초과하였습니다."}}
INVALID_KEY_JSON = {"header": {"resultCode": "30", "resultMsg": "인증키가 유효하지 않습니다."}}
