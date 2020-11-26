#!/usr/bin/env python3
import os

import connexion
from flask import Flask

from swagger_server import encoder


def create_app():
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Location Management API'}, pythonic_params=True)
    return app

port = int(os.environ.get('PORT', 2456))
server = create_app().run(port)

if __name__ == '__main__':
    create_app().run(port=port)
