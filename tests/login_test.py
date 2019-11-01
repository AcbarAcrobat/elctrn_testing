import requests
from hamcrest import *


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
        assert r.status_code == 200
        print(r.status_code)
        if 'userName' in r.json() and r.json()['userName'] == 'Иван Астерикс':
            print('Received Answer Operator Ivan is correctly')
        else:
            print('response JSON and receive answer is not same. ERROR')
            print(r.json())

    def test_get_operatorExtension(self):
        url = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/calls/count/105'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(r.status_code)
        if r.text == '40':
            print('OperatorExtension is correct')
        else:
            print('Answer in OperatorExtension request is not correct')
            print(r.json())



