import json
import logging
import requests
from urllib.parse import urljoin


class Error(Exception):
    pass


class TokenError(Error):
    pass


class DataReadError(Error):
    pass


class JSONReadError(Error):
    pass


class BaseAPI(object):
    # Basic api class

    token = ""
    end_point = "https://api.vscale.io/v1/"

    def __init__(self, *args, **kwargs):
        self.token = ""
        self.end_point = "https://api.vscale.io/v1/"
        self._log = logging.getLogger(__name__)

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

    def _do_request(self, url, method='GET', params={}):
        # This method will return the request object.

        if not self.token:
            raise TokenError("No token provided. Please use a valid token")

        if "https" not in url:
            url = urljoin(self.end_point, url)

        # lookup table to find out the apropriate requests method,
        # headers and payload type (json or query parameters)
        def identity(data):
            return data

        def json_dumps(data):
            return json.dumps(data)

        lookup = {
            'GET': (requests.get, {}, 'params', identity),
            'POST': (requests.post, {'Content-type': 'application/json'},
                     'data',
                     json_dumps),
            'PUT': (requests.put, {'Content-type': 'application/json'},
                    'data',
                    json_dumps),
            'DELETE': (requests.delete, {'Content-type': 'application/json'},
                       'data',
                       json_dumps),
            'PATCH': (requests.patch, {'Content-type': 'application/json'},
                      'data',
                      json_dumps)
        }

        requests_method, headers, payload, transform = lookup[method]
        headers.update({'X-Token': self.token})
        kwargs = {'headers': headers, payload: transform(params)}

        # remove token from log
        headers_str = str(headers).replace(self.token.strip(), 'TOKEN')
        self._log.debug('{0} {1} {2}:{3} {4}'.format(method,
                                                     url,
                                                     payload,
                                                     params,
                                                     headers_str))

        return requests_method(url, **kwargs)

    def get_data(self, url, method='GET', params={}):

        req = self._do_request(url, method, params)
        if req.status_code == 204:
            return True

        try:
            data = req.json()
        except ValueError as e:
            raise JSONReadError('Read JSON failed: {}'.format(e))

        return data
