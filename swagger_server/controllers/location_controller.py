import connexion
import six

from swagger_server.models.location import Location  # noqa: E501
from swagger_server import util


def add_location(location):  # noqa: E501
    """Add a new user location to the system

    Add a new location of the user # noqa: E501

    :param location:
    :type location: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        location = Location.from_dict(connexion.request.get_json())  # noqa: E501
    return 'New location added'


def get_historic_location():  # noqa: E501
    """Get a historic of locations

    Get a historic of locations # noqa: E501


    :rtype: str
    """
    return 'locations!'


def get_location():  # noqa: E501
    """Get user location

    Get user location # noqa: E501


    :rtype: str
    """
    return 'user location!'
