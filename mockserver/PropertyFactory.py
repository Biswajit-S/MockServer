'''

PropertyFactory is responsible to read the property file from the server and initialize the property data.
Also helps to set dummy data to test locally.

'''

import configparser

localPropertyFileName = "app.properties"

class PropertyFactory():
    DB_URL = None
    APP_PORT = None
    APP_SECRET_KEY = None

    '''
    This function can be implemented to read the property file, depending on the server type and deployment model.
    By default it initialize the values with the local property file (app.properties)
    '''
    @classmethod
    def load_properties(cls):
        config = configparser.ConfigParser()
        config.read(localPropertyFileName)

        if len(config.get("DATABASE", "database.url")) > 0:
            cls.DB_URL = config.get("DATABASE", "database.url")
        else:
            raise ValueError("Database could not be initialized")

        if len(config.get("APPLICATION", "application.secret.key")) > 0:
            cls.APP_SECRET_KEY = config.get("APPLICATION", "application.secret.key")
        else:
            raise ValueError("Flask App could not be initialized")

        if len(config.get("APPLICATION", "application.port")) > 0:
            cls.APP_PORT = config.get("APPLICATION", "application.port")
        else:
            raise ValueError("Could not identify a port to run")
