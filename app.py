#!/usr/bin/env python3

import connexion
from flask import Flask

from swagger_server import encoder


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Location Management API'}, pythonic_params=True)
    return app


app = create_app().run(2456)

if __name__ == '__main__':
    app = create_app().run(port=2456)
