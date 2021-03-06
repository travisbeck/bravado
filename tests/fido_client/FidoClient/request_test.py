import mock
from mock import patch


from bravado.fido_client import FidoClient


def test_request_no_timeouts_passed_to_fido():
    with patch('bravado.fido_client.fido.fetch') as fetch:
        request_params = dict(url='http://foo.com/')
        FidoClient().request(request_params)
        assert fetch.call_args == mock.call(
            url='http://foo.com/',
            body=None,
            headers={},
            method='GET',
        )


def test_request_timeout_passed_to_fido():
    with patch('bravado.fido_client.fido.fetch') as fetch:
        request_params = dict(url='http://foo.com/', timeout=1)
        FidoClient().request(request_params)
        assert fetch.call_args == mock.call(
            url='http://foo.com/',
            body=None,
            headers={},
            method='GET',
            timeout=1,
        )


def test_request_connect_timeout_passed_to_fido():
    with patch('bravado.fido_client.fido.fetch') as fetch:
        request_params = dict(url='http://foo.com/', connect_timeout=1)
        FidoClient().request(request_params)
        assert fetch.call_args == mock.call(
            url='http://foo.com/',
            body=None,
            headers={},
            method='GET',
            connect_timeout=1,
        )


def test_request_connect_timeout_and_timeout_passed_to_fido():
    with patch('bravado.fido_client.fido.fetch') as fetch:
        request_params = dict(url='http://foo.com/', connect_timeout=1,
                              timeout=2)
        FidoClient().request(request_params)
        assert fetch.call_args == mock.call(
            url='http://foo.com/',
            body=None,
            headers={},
            method='GET',
            connect_timeout=1,
            timeout=2,
        )
