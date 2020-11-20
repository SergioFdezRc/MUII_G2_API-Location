# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.location import Location  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLocationController(BaseTestCase):
    """LocationController integration test stubs"""

    def test_add_location(self):
        """Test case for add_location

        Add a new user location to the system
        """
        body = Location()
        response = self.client.open(
            '/location',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_historic_location(self):
        """Test case for get_historic_location

        Get a historic of locations
        """
        response = self.client.open(
            '/location',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_location(self):
        """Test case for get_location

        Get user location
        """
        response = self.client.open(
            '/location/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
