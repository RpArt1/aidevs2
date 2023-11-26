import logging
import requests
from utils.config import Config


class AssigmentUtils:

    BASE_URL = 'https://zadania.aidevs.pl/'
    TOKEN_URL = BASE_URL + 'token/'
    ASSIGMENT_URL = BASE_URL + 'task/'
    REVIEW_URL = BASE_URL + 'answer/'

    def __init__(self):
        pass

    @staticmethod
    def process_request(url: str, method: str = 'GET', data: str = None, auth_key:str=None):
        """
        Process http request of given type

        :param url: string
        :param method: GET or POST
        :param data: json data
        :return: response object
        """
        headers = {"Authorization": "Bearer {}".format(Config().aidevs_priv_key)}

        try:
            if method == 'POST':
                logging.debug(f"Sending post to {url} with data {data} and headers {headers}")
                response = requests.post(url, json=data, headers=headers)
            else:
                response = requests.get(url)
            response.raise_for_status()
            return response

        except requests.exceptions.RequestException as e:
            logging.error(f"RequestException: An error occurred while making the request: {response.text}")
            return None
        except ValueError as e:
            logging.error(f"ValueError: An error occurred while decoding the response JSON: {e}")
            return None
        except Exception as e:
            logging.error(f"Exception: An unexpected error occurred: {e}")
            return None

    @staticmethod
    def get_key_for_assigment(task_name: str = 'helloapi'):
        """
        Get key for assignment specified by task_name and return it

        :param task_name: string
        :return: token from response
        """
        url = AssigmentUtils.TOKEN_URL + task_name
        data = {
            'apikey': Config().aidevs_priv_key
        }
        response = AssigmentUtils.process_request(url, 'POST', data)
        if response and response.status_code == 200:
            json_data = response.json()
            logging.info(f"Key for assignment {task_name} is {json_data} ")
            return json_data['token']
        else:
            raise Exception("Request failed with status code:" + response.status_code)

    @staticmethod
    def get_assigment(key_for_assigment):
        """
        Get assigment specified by key_for_assigment and return its json content

        :param key_for_assigment:
        :return:
        """
        url = AssigmentUtils.ASSIGMENT_URL + key_for_assigment
        response = AssigmentUtils.process_request(url, 'GET')
        return response.json() if response else None

    @staticmethod
    def post_assigment(key_for_assigment, assigmnet_data):
        """
        Post assigment specified by key_for_assigment and return its json content or not :)

        :param key_for_assigment:
        :param assigmnet_data:
        :return:
        """
        url = AssigmentUtils.REVIEW_URL + key_for_assigment #none 
        data = {"answer": assigmnet_data}


        logging.debug(f"Sending JSON response to aidevs: {data}")

        response = AssigmentUtils.process_request(url, 'POST', data)
        return response.json() if response else None