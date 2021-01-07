import os


class FATConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')