import requests
from requests import Request, Session


class Sampler:

    def __init__(self):
        pass


class PostSampler(Sampler):
    def __init__(self, params, headers):
        super().__init__()

        url = f"{params['proto']}://{params['domain']}{params['path']}"

        req = Request(
            "POST",
            url,
            data=params["payload"],
            headers=headers
        )
        self.req = req.prepare()


class GetSampler(Sampler):
    def __init__(self, params, headers):
        super().__init__()

        url = f"{params['proto']}://{params['domain']}{params['path']}"

        req = Request(
            "GET",
            params["url"],
            params=params["payload"],
            headers=headers
        )
        prepped = req.prepare()


class SamplerFactory():
    d = {
        "get": GetSampler,
        "post": PostSampler
    }

    def create(self, params, headers):
        target_class = self.d[params["method"].lower()]
        return target_class(params, headers)


class HeaderManager:
    headers = {"Content-Type": "application/json"}


class RequestDefaults:
    defaults = {}

    _proto = "http"
    _domain = ""

    @property
    def proto(self):
        return self._proto

    @proto.setter
    def proto(self, val):
        if val not in ["http", "https"]:
            raise ValueError("Proto must be http or https")
        self._proto = val
        self.defaults["proto"] = val

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, val):
        self._domain = val
        self.defaults["domain"] = val


class Test:
    samplers = []

    header_manager = HeaderManager()
    request_defaults = RequestDefaults()
    s = Session()
    factory = SamplerFactory()

    def add(self, params, headers={}):
        marged_params = {**self.request_defaults.defaults, **params}

        r = self.factory.create(marged_params, self.header_manager.headers)

        self.samplers.append(r)

    def send_all(self):
        for sampler in self.samplers:
            resp = self.s.send(sampler.req)
            print(resp.content.decode("utf8"))