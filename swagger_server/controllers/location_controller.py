import connexion
import six
from flask import jsonify, abort

from swagger_server.db.Database import PostgresDB
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
        print(location)
        db = PostgresDB()
        db.insert_new_location(location.location)
    return 'Human detected at %s' % location.location


def get_historic_location():  # noqa: E501
    """Get a historic of locations

    Get a historic of locations # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    historial = db.get_locations()
    if len(historial) > 0:
        return jsonify({"historial": historial}), 200
    else:
        return '', 204


def get_location():  # noqa: E501
    """Get user location

    Get user location # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    user_location = db.get_last_location()
    if len(user_location) > 0:
        loc = user_location[0]
        if loc is None:
            return '', 204
        return jsonify({"location": loc[1]})
    return abort(404)
