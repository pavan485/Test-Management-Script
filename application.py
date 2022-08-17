from cgi import test
import datetime
import log
import request_handler,payload_builder
import yaml

catchpoint_config = './config/catchpoint_config.yaml'
monitor_type = './config/monitor_type.yaml'
override_settings = './config/override_settings.yaml'
test_config = './config/test_config.yaml'
test_type_details = './config/test_type.yaml'

conf = yaml.safe_load(open(catchpoint_config))
monitor_type_details = yaml.safe_load(open(monitor_type))
override_settings = yaml.safe_load(open(override_settings))
test_details =  yaml.safe_load(open(test_config))
test_type_details = yaml.safe_load(open(test_type_details))

logger = log.get_logger(__name__,conf['log_file'],conf['log_level'])

# Create single or multiple tests configured in config file 
class Application(object):

    def __init__(self):
        self.__request_handler = request_handler.Catchpoint()
        self.__payload_builder = payload_builder.TestSettings()

    # main function to create tests configured in config file
    def run(self):
        try:
            for test_detail in test_details['tests']:
                if test_detail['product_id'] == None:
                    product_payload = test_type_details['product']
                    product_payload['name'] = 'tms product' + str(datetime.datetime.now())
                    product_payload['divisionId']= test_detail['division_id']
                    prod_response = self.__request_handler.create_product(conf,product_payload)
                    logger.info(prod_response)
                    product_id = prod_response['id']
                    break
                if test_detail['folder_id'] == None:
                    folder_payload = test_type_details['folder']
                    folder_payload['name'] = 'tms folder' + str(datetime.datetime.now())
                    folder_payload['divisionId']= test_detail['division_id']
                    if test_detail['product_id'] is not None:
                        folder_payload['product_id'] = test_detail['product_id']
                    else:
                         folder_payload['product_id'] = product_id
                    folder_response = self.__request_handler.create_folder(conf,folder_payload)   
                    logger.info(folder_response)  
                    folder_id = folder_response['id']
                    break
            for test_detail in test_details['tests']:
                test_body = {}
                if test_detail['product_id'] is None:
                    test_detail['product_id'] = product_id
                test_body.update(self.__payload_builder.basic_test_details(test_detail))
                test_body.update(self.__payload_builder.more_setting(test_detail))
                test_body.update(self.__payload_builder.test_type(test_detail, test_type_details))
                test_body.update(self.__payload_builder.monitor_type(test_detail, monitor_type_details))
                test_body.update(self.__payload_builder.thresholds(test_detail, override_settings))
                if test_detail['test_type'] == 'web_socket':
                    test_body['thresholdRestModel']['testTimeMonitorTypeId'] = 30
                    test_body['thresholdRestModel']['availabilityMonitorTypeId'] = 30
                if test_detail['override']['advanced_settings'] == True:
                    test_body['advancedSettings'] = self.__payload_builder.advanced_settings(test_detail, override_settings)
                else:
                    test_body['advancedSettings'] = override_settings['advanced_settings']['inherited']
                if test_detail['test_type'] != 'ntp' and test_detail['test_type'] != 'transport':
                    if test_detail['override']['requests'] == True:
                        test_body['requestSettings'] = self.__payload_builder.request_settings(test_detail, override_settings)
                    else:
                        test_body['requestSettings'] = override_settings['request_settings']['inherited']
                if test_detail['test_type'] != 'ntp':
                    if test_detail['override']['insights'] == True:
                        test_body['insightData'] = self.__payload_builder.insights(test_detail, override_settings)
                    else:
                        test_body['insightData'] = override_settings['insights']['inherited']
                if test_detail['override']['targetting_schedule_settings'] == True:
                    test_body['scheduleSettings'] = self.__payload_builder.targeting_scheduling(test_detail, override_settings)
                else:
                    test_body['scheduleSettings'] = override_settings['schedule_settings']['inherited']
                if test_detail['override']['alerts'] == True:
                    test_body['alertGroup'] = self.__payload_builder.alert_settings(test_detail, override_settings)
                else:
                    test_body['alertGroup'] = override_settings['alerts']['inherited']
                test_response = self.__request_handler.create_test(conf,test_body)
                logger.info(test_response)
            
        except Exception as e:
            logger.exception(str(e))

 # Run main function              
if __name__ == '__main__':
    Application().run()
        