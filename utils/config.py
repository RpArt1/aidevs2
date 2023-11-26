# config.py
import configparser
import logging

class Config:
    def __init__(self, config_file_path='secrets.secret'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

    @property
    def aidevs_priv_key(self):
        return self.config.get('DEFAULT', 'PERSONAL_AIDEVS_API_KEY')

    @property
    def open_api_key(self):
        return self.config.get('DEFAULT', 'OPENAI_API_KEY')
  
