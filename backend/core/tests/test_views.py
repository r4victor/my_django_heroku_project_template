from core.tests.common import MyAPITestCase


class EndpointTest(MyAPITestCase):

    def call_endpoint(self):
        return self.client.get('/api/endpoint/')

    def test_returns_401_if_api_key_not_provided(self):
        response = self.call_endpoint()
        self.assertEqual(response.status_code, 401)

    def test_return_data(self):
        self.authenticate_with_api_key()
        response = self.call_endpoint()
        self.assertEqual(response.status_code, 200)
        body = response.json()
        expected_body = {
            'data': 'Hello!'
        }
        self.assertDictEqual(body, expected_body)
