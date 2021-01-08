import os
import urllib.parse


class FATConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Azure AD auth
    SESSION_TYPE = "filesystem"
    AD_ID = os.getenv('AD_ID')
    AD_SECRET = os.getenv('AD_SECRET')
    AD_AUTHORITY = os.getenv('AD_AUTHORITY')
    AD_REDIRECT_PATH = "/auth/get_token"

    # Azure SQL
    DB_SERVER = os.getenv('DB_SERVER')
    DB_NAME = os.getenv('DB_NAME')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(f'DRIVER={{SQL Server}};SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Azure Blobs
    BLOB_ACCOUNT = os.getenv('BLOB_ACCOUNT')
    BLOB_KEY = os.getenv('BLOB_KEY')
    BLOB_NAME = os.getenv('BLOB_NAME')

    # Azure App Insight
    APP_INSIGHT_KEY = os.getenv('APP_INSIGHT_KEY')