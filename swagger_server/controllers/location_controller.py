import connexion
from flask import jsonify, abort
from muii_g2_family_lock_database.Database import PostgresDB

from swagger_server.models.location import Location  # noqa: E501


def add_location(location):  # noqa: E501
    """Add a new user location to the system

    Add a new location of the user # noqa: E501

    :param location:
    :type location: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        location = Location.from_dict(connexion.request.get_json())  # noqa: E501
    db = PostgresDB()
    error = db.insert_new_location(location.location)
    if error:
        return jsonify(msg=error)
    return jsonify(msg='Human detected at %s' % location.location)


def get_historic_location():  # noqa: E501
    """Get a historic of locations

    Get a historic of locations # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    historial = db.get_locations()
    if "Error" in historial:
        return jsonify(msg=historial)
    if len(historial) > 0:
        data = {"historial" : []}
        for row in historial:
            data['historial'].append(
                {
                    "id": row[0],
                    "name": row[1]
                }
            )
        return jsonify(data), 200
    else:
        return '', 204


def get_location():  # noqa: E501
    """Get user location

    Get user location # noqa: E501


    :rtype: str
    """
    db = PostgresDB()
    user_location = db.get_last_location()
    if "Error" in user_location:
        return jsonify(msg=user_location)
    if len(user_location) > 0:
        loc = user_location[0]
        if loc is None:
            return '', 204
        return jsonify({"location": loc[1]})
    return abort(404)
