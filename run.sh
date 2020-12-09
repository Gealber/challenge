#! /bin/bash

echo "Running as a development environment"

export FLASK_APP=challenge
export FLASK_ENV=development

flask run