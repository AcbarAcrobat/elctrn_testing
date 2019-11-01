import requests
from


class TestApi:

    def test_get_operators_list(self):
        url = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/operators'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(r.status_code)

    def test_get_active_operators(self):
        url = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/operators/active'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(r.status_code)

    def test_get_values(self):
        url = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/values'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(r.status_code)

    def test_get_users_submit_phonenumb(self):
        url = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/users/submit/112'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(r.status_code)

    def test_get_ivan_asterisk(self):
        url = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/operators/9cfe3583-cc70-44b9-b80d-6bed59f68f1a'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(r.status_code)
