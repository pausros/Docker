#!/bin/bash
set -e
# Create an admin user
fabmanager create-admin --app superset $@
# Initialize the database
superset db upgrade
# Load some data to play with
superset load_examples
# Create default roles and permissions
superset init
