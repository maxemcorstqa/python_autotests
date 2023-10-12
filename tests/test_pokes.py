import requests
import pytest
import local_settings as settings
import json

# проверка статуса 200 от /trainers
def test_status_code():
    resp = requests.get(
        f'{settings.host}/trainers'
    )
    assert resp.status_code == 200

# проверка что после запроса с query с нашим id - в ответе есть наш id
def test_id_included():
    params = {"trainer_id": "2498"}
    resp = requests.get(
        f'{settings.host}/trainers',
        params = {"trainer_id": "2498"}
    )
    assert resp.json()["id"] == "2498"


