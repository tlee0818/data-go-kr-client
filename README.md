# data-go-kr-client

Python client for [공공데이터포털 OpenAPI](https://www.data.go.kr) — one method per endpoint.

Each API endpoint is exposed as a plain Python method with a descriptive English name. No raw URLs, no opaque parameter strings, no need to read Korean documentation to figure out what a call does.

## Install

```bash
pip install data-go-kr-client
```

## Setup

Get an API key from [https://www.data.go.kr](https://www.data.go.kr) and set it as an environment variable:

```bash
export PUBLIC_DATA_API_KEY="your_api_key_here"
```

Or add it to a `.env` file (loaded automatically):

```
PUBLIC_DATA_API_KEY=your_api_key_here
```

## Usage

```python
from data_go_kr_client import DataGoKrClient

client = DataGoKrClient()

# Each endpoint is a method — results come back as a dict
result = client.get_power_usage_service()
print(result)
```

## Available methods

11975 methods total — one per endpoint.

| Method | Description |
|--------|-------------|
| `get_power_usage_service` | 전력사용량 조회 |
| `get_electrical_efficiency` | 전기 설비 에너지 효율 정보 조회 |
| `get_plant_performance_prediction_service` | 플랜트 성능 예측 및 AI 검증용 플랜트 발전 운전 정보 조회 |
| `get_renewable_performance_prediction` | 플랜트 성능 예측 및 AI 검증용 신재생 정보 조회 |
| `get_weather_observation_service` | 기상관측 정보 조회 |
| `get_thesis_info_on_fnclty_by_food` | 식품별 기능성(효능)에 대한 논문정보 조회 |
| `get_thesis_info_on_food_by_irdnt` | 성분별 식품에 대한 논문정보 조회 |
| `get_info_cas_no` | 성분(CAS_NO) 정보 조회 |
| `get_thesis_info_on_food_by_fnclty` | 기능성(효능)별 식품에 대한 논문정보 조회 |
| `get_thesis_info_on_irdnt_and_fnclty_by_food` | 식품별 성분과 기능성(효능)에 대한 논문정보 조회 |
| `get_thesis_info_on_irdnt_and_food_by_fnclty` | 기능성(효능)별 성분과 식품에 대한 논문정보 조회 |
| `get_thesis_info_on_fnclty_by_irdnt` | 성분별 기능성(효능)에 대한 논문정보 조회 |
| `odms_stat_28_call_stat28_api` | 보건복지부_보건·복지현황_유형별 의료급여 대상자 현황 조회 |
| `odms_stat_29_call_stat29_api` | 보건복지부_보건·복지현황_연령별 의료급여 대상자 현황 조회 |
| `odms_stat_48_call_stat48_api` | 보건복지부_보건·복지현황_시도별 노인 취업알선 실적 조회 |
| `odms_stat_14_call_stat14_api` | 보건복지부_보건·복지현황_병원 및 의원 수 조회 |
| `odms_stat_38_call_stat38_api` | 보건복지부_보건·복지현황_백신종류별/시도별 만3세 전국예방접종률 현황 조회 |
| `odms_stat_17_call_stat17_api` | 보건복지부_보건·복지현황_등록장애인 수 조회 |
| `get_ulfd_info` | 지하역사 실내공기질 측정데이터 초미세먼지 정보 |
| `odms_stat_18_call_stat18_api` | 보건·복지현황_독거장애인 서비스 지원 현황 |
| `odms_stat_24_call_stat24_api` | 보건복지부_보건·복지현황_독거노인 수 조회 |
| `odms_stat_27_call_stat27_api` | 노인복지 이용시설 현황 조회 |
| `odms_stat_37_call_stat37_api` | 공급자별 경상의료비 추이 조회 |
| `odms_stat_32_call_stat32_api` | 보건복지부_보건·복지현황_건강보험 요양급여 실적 |
| `odms_stat_34_call_stat34_api` | 보건복지부_보건·복지현황_건강보험 보험료 및 요양급여의 급여액 조회 |
| `odms_stat_31_call_stat31_api` | 보건복지부_보건·복지현황_건강보험 보험급여 실적 |
| `odms_stat_07_call_stat07_api` | 보건복지부_보건·복지현황_HIV, AIDS 감염 내국인 발생 및 사망 신고현황 |
| `get_code_by_large_series` | 표준분류 대계열 코드조회 |
| `get_university_major_code` | 학교별학과 코드조회 |
| `get_code_by_middle_series` | 표준분류 중계열 코드조회 |
| … | 11945 more — see [API docs](https://tlee0818.github.io/data-go-kr-client/) |


## Pagination

All list methods accept `page` and `page_size` keyword arguments:

```python
result = client.get_power_usage_service(page=2, page_size=100)
```

Default page size: `1000`.

## Error handling

```python
from data_go_kr_client.exceptions import APIKeyError, RateLimitError, NoDataFoundError

try:
    result = client.get_power_usage_service()
except APIKeyError:
    print("Invalid or missing API key")
except RateLimitError:
    print("Rate limit exceeded — retry later")
except NoDataFoundError:
    print("No results for this query")
```

## API docs

Full method reference: [tlee0818.github.io/data-go-kr-client](https://tlee0818.github.io/data-go-kr-client/)

Source portal: [https://www.data.go.kr](https://www.data.go.kr)
