import requests,sys
import logger,json
import yaml
import log

catchpoint_config = './config/catchpoint_config.yaml'
conf = yaml.safe_load(open(catchpoint_config))
logger = log.get_logger(__name__,conf['log_file'],conf['log_level'])

# Authorise and fetch data from catchpoint api
class Catchpoint(object):
    
    def __init__(self):
        self.verbose = False 
        
    # Debug output. Set self.verbose to True to enable.
    def debug(self, msg):
        if self.verbose:
                logger.info(str(msg))

    def connection_error(e):
        msg = "Unable to reach {0}".format(e)
        sys.exit(msg)
    
    # function to create product.
    def create_product(self,creds,payload):
        uri = '{0}://{1}/{2}/{3}'.format(creds['protocol'],creds['domain'],creds['version'],creds['product_endpoint'])
        payload = json.dumps(payload)
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer {0}'.format(creds['apiKey'])
            }
        try:
            response = requests.post(uri, headers=headers, data=payload)
            if response.status_code != 200:
                self.debug("The response is "+str(response.content))	
                self.debug("there was some error"+str(response))
        except requests.ConnectionError as e:
            self.debug(str(e))
            self.connection_error(e)
        try:
            print(response)
            response_data = response.json()
        except TypeError as e:
            return e
        return response_data

    # function to create folder.
    def create_folder(self,creds,payload): 
        logger.info("calling API with the token") 
        uri = '{0}://{1}/{2}/{3}'.format(creds['protocol'],creds['domain'],creds['version'],creds['folder_endpoint'])
        payload = json.dumps(payload)
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer {0}'.format(creds['apiKey'])
            }
        try:
            response = requests.post(uri, headers=headers, data=payload)
            if response.status_code != 200:
                self.debug("The response is "+str(response.content))	
                self.debug("there was some error"+str(response))
        except requests.ConnectionError as e:
            self.debug(str(e))
            self.connection_error(e)
        try:
            response_data = response.json()
        except TypeError as e:
            return e
        return response_data

    # function to create test.
    def create_test(self,creds,payload): 
        logger.info("calling API with the token") 
        uri = '{0}://{1}/{2}/{3}'.format(creds['protocol'],creds['domain'],creds['version'],creds['test_endpoint'])
        payload = json.dumps(payload)
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer {0}'.format(creds['apiKey'])
            }
        try:
            response = requests.post(uri, headers=headers, data=payload)
            if response.status_code != 200:
                self.debug("The response is "+str(response.content))	
                self.debug("there was some error"+str(response))
        except requests.ConnectionError as e:
            self.debug(str(e))
            self.connection_error(e)
        try:
            response_data = response.json()
        except TypeError as e:
            return e
        return response_data