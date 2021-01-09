import os
import urllib.parse

from dotenv import load_dotenv
load_dotenv()

class FATConfig:
    SECRET_KEY='CheckOutThisSecret'

    # Azure SQL
    DB_SERVER='flasktest.database.windows.net'
    DB_NAME='test2'
    DB_USERNAME='flasktestroot@flasktest'
    DB_PASSWORD='Flask/0m'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(f'DRIVER={{SQL Server}};SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Azure Blobs
    BLOB_ACCOUNT='testflaskblob'
    BLOB_KEY='LybDrM6OJLCcl8ASyF/1TOpBMhzWEgGL/5asCM6G0u++NwTayp0PYIt5V5Y+3Yve4eH4w9XzU8HI4z6YYluddw=='
    BLOB_NAME='images'

    # Azure AD auth
    SESSION_TYPE = 'sqlalchemy'
    AD_REDIRECT_PATH = "/auth/get_token"
    AD_ID='db26d24d-9414-41a0-aa57-a29421f56734'
    AD_SECRET='6_8A4pl8Nm-.e-mh8zLHiUXT64~7QlG7eP'
    AD_AUTHORITY='https://login.microsoftonline.com/common'

    # Azure App Insight
    APP_INSIGHT_KEY = '57dd560e-a7fa-4498-a128-21034fd04bdc'