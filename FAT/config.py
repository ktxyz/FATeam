import os


class FATConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Azure AD auth
    SESSION_TYPE = "filesystem"
    AD_ID = os.getenv('AD_ID')
    AD_SECRET = os.getenv('AD_SECRET')
    AD_AUTHORITY = os.getenv('AD_AUTHORITY')
    AD_REDIRECT_PATH = "/auth/get_token"