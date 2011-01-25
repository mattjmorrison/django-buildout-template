from lettuce import before

from django.db import connections

@before.harvest
def setup_database(variables):
    for alias in connections:
        connections[alias].creation.create_test_db(1, autoclobber=False)