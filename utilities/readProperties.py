import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','base_url')
        return url

    @staticmethod
    def getEmailaddress():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
