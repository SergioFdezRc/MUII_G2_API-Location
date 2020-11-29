# coding: utf-8

from __future__ import absolute_import

from unittest import mock

from flask import json

from swagger_server.models.location import Location  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLocationController(BaseTestCase):
    """LocationController integration test stubs"""

    @mock.patch("database.Database.PostgresDB.insert_new_location")
    def test_add_location(self, mocked_insert_new_location):
        """Test case for add_location

        Add a new user location to the system
        """
        body = Location("kitchen")
        mocked_insert_new_location.assert_not_called()
        response = self.client.open(
            '/location',
            data=json.dumps(body),
            method='POST',
            content_type='application/json'
        )
        mocked_insert_new_location.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("database.Database.PostgresDB.get_locations")
    def test_get_historic_location(self, mocked_get_locations):
        """Test case for get_historic_location

        Get a historic of locations
        """
        mocked_get_locations.assert_not_called()
        mocked_get_locations.return_value = [
            [1, "mocked_location"],
            [2, "mocked_location_1"],
            [3, "mocked_location_2"],
            [4, "mocked_location_3"],
        ]
        response = self.client.open(
            '/location',
            method='GET')

        mocked_get_locations.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @mock.patch("database.Database.PostgresDB.get_last_location")
    def test_get_location(self, mocked_get_last_location):
        """Test case for get_location

        Get user location
        """
        mocked_get_last_location.assert_not_called()
        mocked_get_last_location.return_value = [
            [1, "mocked_location"]
        ]
        response = self.client.open(
            '/location/user',
            method='GET')
        mocked_get_last_location.assert_called_once()
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
