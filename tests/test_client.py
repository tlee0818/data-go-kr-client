"""Tests for DataGoKrClientClient — endpoint routing, error handling."""

import httpx
import pytest
import respx

from data_go_kr_client.exceptions import APIKeyError, RateLimitError
from data_go_kr_client.http.client import DataGoKrClientClient
from tests.conftest import (
    FAKE_KEY,
    GET_ELECTRICAL_EFFICIENCY_JSON,
    GET_PLANT_PERFORMANCE_PREDICTION_SERVICE_JSON,
    GET_POWER_USAGE_SERVICE_JSON,
    INVALID_KEY_JSON,
    RATE_LIMIT_JSON,
)


@respx.mock
def test_get_power_usage_service_hits_correct_endpoint():
    route = respx.get(
        "https://apis.data.go.kr/B552522/PowerUsageService/getPowerUsageService"
    ).mock(
        return_value=httpx.Response(
            200,
            json=GET_POWER_USAGE_SERVICE_JSON,
        )
    )
    DataGoKrClientClient(FAKE_KEY).get_power_usage_service(
        from_date="test_from_date",
        to_date="test_to_date",
        plant="test_plant",
        clsf_cd="test_clsf_cd",
        hogi="test_hogi",
        tag="test_tag",
    )
    assert route.called


@respx.mock
def test_get_power_usage_service_injects_auth_key():
    route = respx.get(
        "https://apis.data.go.kr/B552522/PowerUsageService/getPowerUsageService"
    ).mock(
        return_value=httpx.Response(
            200,
            json=GET_POWER_USAGE_SERVICE_JSON,
        )
    )
    DataGoKrClientClient(FAKE_KEY).get_power_usage_service(
        from_date="test_from_date",
        to_date="test_to_date",
        plant="test_plant",
        clsf_cd="test_clsf_cd",
        hogi="test_hogi",
        tag="test_tag",
    )
    assert "serviceKey" in dict(route.calls[0].request.url.params)


@respx.mock
def test_get_electrical_efficiency_hits_correct_endpoint():
    route = respx.get(
        "https://apis.data.go.kr/B552522/ElectricalEfficiencyService/getElectricalEfficiency"
    ).mock(
        return_value=httpx.Response(
            200,
            json=GET_ELECTRICAL_EFFICIENCY_JSON,
        )
    )
    DataGoKrClientClient(FAKE_KEY).get_electrical_efficiency(
        from_date="test_from_date",
        to_date="test_to_date",
        plant="test_plant",
        clsf_cd="test_clsf_cd",
        hogi="test_hogi",
        tag="test_tag",
    )
    assert route.called


@respx.mock
def test_get_electrical_efficiency_injects_auth_key():
    route = respx.get(
        "https://apis.data.go.kr/B552522/ElectricalEfficiencyService/getElectricalEfficiency"
    ).mock(
        return_value=httpx.Response(
            200,
            json=GET_ELECTRICAL_EFFICIENCY_JSON,
        )
    )
    DataGoKrClientClient(FAKE_KEY).get_electrical_efficiency(
        from_date="test_from_date",
        to_date="test_to_date",
        plant="test_plant",
        clsf_cd="test_clsf_cd",
        hogi="test_hogi",
        tag="test_tag",
    )
    assert "serviceKey" in dict(route.calls[0].request.url.params)


@respx.mock
def test_get_plant_performance_prediction_service_hits_correct_endpoint():
    route = respx.get(
        "https://apis.data.go.kr/B552522/PlantPerformancePredictionService/getPlantPerformancePredictionService"
    ).mock(
        return_value=httpx.Response(
            200,
            json=GET_PLANT_PERFORMANCE_PREDICTION_SERVICE_JSON,
        )
    )
    DataGoKrClientClient(FAKE_KEY).get_plant_performance_prediction_service(
        from_date="test_from_date",
        to_date="test_to_date",
        plant="test_plant",
        clsf_cd="test_clsf_cd",
        hogi="test_hogi",
        tag="test_tag",
    )
    assert route.called


@respx.mock
def test_get_plant_performance_prediction_service_injects_auth_key():
    route = respx.get(
        "https://apis.data.go.kr/B552522/PlantPerformancePredictionService/getPlantPerformancePredictionService"
    ).mock(
        return_value=httpx.Response(
            200,
            json=GET_PLANT_PERFORMANCE_PREDICTION_SERVICE_JSON,
        )
    )
    DataGoKrClientClient(FAKE_KEY).get_plant_performance_prediction_service(
        from_date="test_from_date",
        to_date="test_to_date",
        plant="test_plant",
        clsf_cd="test_clsf_cd",
        hogi="test_hogi",
        tag="test_tag",
    )
    assert "serviceKey" in dict(route.calls[0].request.url.params)


@respx.mock
def test_raises_rate_limit_error():
    respx.get("https://apis.data.go.kr/B552522/PowerUsageService/getPowerUsageService").mock(
        return_value=httpx.Response(
            200,
            json=RATE_LIMIT_JSON,
        )
    )
    with pytest.raises(RateLimitError):
        DataGoKrClientClient(FAKE_KEY).get_power_usage_service(
            from_date="test_from_date",
            to_date="test_to_date",
            plant="test_plant",
            clsf_cd="test_clsf_cd",
            hogi="test_hogi",
            tag="test_tag",
        )


@respx.mock
def test_raises_api_key_error():
    respx.get("https://apis.data.go.kr/B552522/PowerUsageService/getPowerUsageService").mock(
        return_value=httpx.Response(
            200,
            json=INVALID_KEY_JSON,
        )
    )
    with pytest.raises(APIKeyError):
        DataGoKrClientClient(FAKE_KEY).get_power_usage_service(
            from_date="test_from_date",
            to_date="test_to_date",
            plant="test_plant",
            clsf_cd="test_clsf_cd",
            hogi="test_hogi",
            tag="test_tag",
        )
