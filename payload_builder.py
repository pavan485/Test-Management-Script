import html,log
import random
import utils
import yaml

catchpoint_config = './config/catchpoint_config.yaml'
conf = yaml.safe_load(open(catchpoint_config))
logger = log.get_logger(__name__,conf['log_file'], conf['log_level'])

# Authorise and fetch data from catchpoint api
class TestSettings(object):
    
    # function to create basic payload using config
    def basic_test_details(self, test_details):
        basic_payload = {}
        basic_payload['id'] = 0
        basic_payload['name'] = test_details['test_name']
        basic_payload['description'] = test_details['description']
        basic_payload['divisionId'] = test_details['division_id']
        basic_payload['productId'] = test_details['product_id']
        basic_payload['folderId'] = test_details['folder_id']
        if test_details['status'] =='active':
            basic_payload['status'] = {
                                        "id": 0,
                                        "name": "Active"
                                    }
        elif test_details['status'] == 'inactive':
            basic_payload['status'] = {
                                        "id": 1,
                                        "name": "Inactive"
                                    }                            
        return basic_payload
        
    # function to add more settings to payload using config
    def more_setting(self, test_config):
        more_settings = {}
        more_settings['startTime'] = test_config['more_settings']['start_time']
        more_settings['endTime'] = test_config['more_settings']['end_time']
        more_settings['enableTestDataWebhook'] = test_config['more_settings']['enable_test_data_webhook']
        raw_labels = test_config['more_settings']['labels']
        labels = []
        for name,value in raw_labels.items():
            temp = {
                "color": "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]),
                "name": name,
                "values": [value]
            }
            labels.append(temp)    
        more_settings['labels'] = labels
        return more_settings

    # function to update test type to payload using config
    def test_type(self,test_inputs,test_type_details):
        test_type = test_inputs['test_type']
        test_payload = {}
        match test_type:
            case 'web':
                test_payload = test_type_details['web']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'transaction':
                test_payload = test_type_details['transaction']
                test_payload['script'] = test_inputs['script']
                return test_payload
            case 'html':
                test_payload = test_type_details['html']
                test_payload['testRequestData']['requestData'] = html.escape(test_inputs['test_html'])
                return test_payload
            case 'dns':
                test_payload = test_type_details['dns']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'transport':
                test_payload = test_type_details['transport']
                test_payload['url'] = test_inputs['test_url']
                # test_payload['testRequestData']['requestData'] = test_inputs['request_data']
                return test_payload
            case 'ping':
                test_payload = test_type_details['ping']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'traceroute':
                test_payload = test_type_details['traceroute']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'api':
                test_payload = test_type_details['api']
                test_payload['testRequestData']['requestData'] = test_inputs['script']
                return test_payload
            case 'ftp':
                test_payload = test_type_details['ftp']
                test_payload['url'] = test_inputs['test_url']
                test_payload['ftpUploadFileSize'] = test_inputs['ftp_upload_file_size']
                return test_payload
            case 'ntp':
                test_payload = test_type_details['ntp']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'web_socket':
                test_payload = test_type_details['websocket']
                test_payload['testRequestData']['requestData'] = test_inputs['script']
                return test_payload
            case 'streaming':
                test_payload = test_type_details['streaming']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'imap':
                test_payload = test_type_details['imap']
                test_payload['url'] = test_inputs['test_location']
                return test_payload
            case 'mqtt':
                test_payload = test_type_details['mqtt']
                test_payload['url'] = test_inputs['test_url']
                return test_payload
            case 'ssl':
                test_payload = test_type_details['ssl']
                test_payload['url'] = test_inputs['test_location']
                return test_payload
            case 'custom':
                test_payload = test_type_details['custom']
                test_payload['url'] = test_inputs['test_location']
                return test_payload
            case 'bgp':
                test_payload = test_type_details['bgp']
                test_payload['url'] = test_inputs['prefix']
                return test_payload
            case _:        
                return {}

     # function to update monitor type to payload using config
    def monitor_type(self, test_inputs, monitor_type_details):
        monitor_type = test_inputs['monitor_type']
        test_payload = {}
        match monitor_type:
            case 'chrome':
                test_payload = monitor_type_details['web']['chrome']
                return test_payload
            case 'object':
                test_payload = monitor_type_details['web']['object']
                return test_payload
            case 'emulated':
                test_payload = monitor_type_details['web']['emulated']
                return test_payload
            case 'playback':
                test_payload = monitor_type_details['web']['playback']
                return test_payload
            case 'mobile':
                test_payload= monitor_type_details['web']['mobile']
                return test_payload
            case 'mobile_playback':
                test_payload = monitor_type_details['web']['mobile_playback']
                return test_payload
            case 'direct':
                test_payload = monitor_type_details['direct']
                return test_payload
            case 'experience':
                test_payload = monitor_type_details['experience']
                return test_payload
            case 'transport_tcp':
                test_payload = monitor_type_details['transport_tcp']
                return test_payload
            case 'transport_udp':
                test_payload = monitor_type_details['transport_udp']
                return test_payload
            case 'ping_icmp':
                test_payload = monitor_type_details['ping_icmp']
                return test_payload
            case 'ping_tcp':
                test_payload = monitor_type_details['ping_tcp']
                return test_payload
            case 'ping_udp':
                test_payload = monitor_type_details['ping_udp']
                return test_payload
            case 'traceroute_icmp':
                test_payload = monitor_type_details['traceroute_icmp']
                return test_payload
            case 'traceroute_tcp':
                test_payload = monitor_type_details['traceroute_tcp']
                return test_payload
            case 'traceroute_udp':
                test_payload = monitor_type_details['traceroute_udp']
                return test_payload
            case 'ssh':
                test_payload = monitor_type_details['ssh']
                test_payload['url'] = test_inputs['test_url']
                test_payload['authentication']['userName'] = test_inputs['  ']
                test_payload['authentication']['password'] = test_inputs['password']
                test_payload['authentication']['id'] = 0
                return test_payload
            case 'custom':
                test_payload = monitor_type['custom']
                return test_payload
            case _:        
                return {} 

    # function to override advanced settings
    def advanced_settings(self, test_config, override_settings):
        advanced_settings = {}
        test_flags = []
        advanced_settings.update(override_settings['advanced_settings']['overriden'])
        for flags in override_settings['advanced_settings']['applied_test_flags']:
            for flag_id in test_config['advanced_settings']['test_flag_ids']: 
                if flag_id == flags['id']:
                    test_flags.append(flags)
        advanced_settings['appliedTestFlags'] = test_flags
        return advanced_settings

    # function to override targetting and scheduling section
    def targeting_scheduling(self, test_config, override_settings):
        targeting_scheduling_settings = {}
        targeting_scheduling_settings.update(override_settings['schedule_settings']['overridden'])
        targeting_scheduling_settings['frequency'] = utils.Utils.frequency_id(test_config['targetting_schedule_settings']['frequency'])
        targeting_scheduling_settings['testNodeDistribution'] = utils.Utils.node_distribution_id(test_config['targetting_schedule_settings']['test_node_distribution_id'])
        targeting_scheduling_settings['nodes'] = utils.Utils.node_details(test_config['targetting_schedule_settings']['node_ids'])
        return targeting_scheduling_settings

    # function to add thrsholds to payload
    def thresholds(self, test_config, override_settings):
        threshold_settings = {}
        threshold_settings.update(override_settings['thresholds'])
        if test_config['thresholds']['test_time_warning'] and test_config['thresholds']['test_time_critical'] is not None:
            if test_config['thresholds']['test_time_critical'] > test_config['thresholds']['test_time_warning']:
                threshold_settings['thresholdRestModel']['testTimeApdexThresholdWarning'] = test_config['thresholds']['test_time_warning']
                threshold_settings['thresholdRestModel']['testTimeApdexThresholdCritical'] = test_config['thresholds']['test_time_critical']
        if test_config['thresholds']['availability_warning'] and test_config['thresholds']['availability_critical'] is not None:
            if test_config['thresholds']['availability_warning'] >test_config['thresholds']['availability_critical']:
                threshold_settings['thresholdRestModel']['availabilityApdexThresholdWarning'] = test_config['thresholds']['availability_warning']
                threshold_settings['thresholdRestModel']['availabilityApdexThresholdCritical'] = test_config['thresholds']['availability_critical']
        return threshold_settings
    
    # function to override insights section
    def insights(self, test_config, override_settings):
        insights = {}
        indicators_list = []
        insights.update(override_settings['insights']['overridden'])
        for indicator_id in test_config['insights']['indicators']:
            for indicator in override_settings['insights']['indicators']:
                if indicator_id == indicator['id']:
                    indicators_list.append(indicator)
        insights['indicators'] = indicators_list
        tracepoints_list = []
        for tracepoints_id in test_config['insights']['tracepoints']:
            for tracepoint in override_settings['insights']['tracepoints']:
                if tracepoints_id == tracepoint['id']:
                    tracepoints_list.append(tracepoint)
        insights['tracepoints'] = tracepoints_list
        return insights

    # function to override request section
    def request_settings(self, test_config, override_settings):
        http_header_list = []
        request_settings = override_settings['request_settings']['overridden']
        if test_config['requests']['authentication_type'] is not None:
            if test_config['requests']['username'] is not None:
                if test_config['requests']['password'] is not None:            
                    request_settings['authentication'] = override_settings['request_settings']['authentication']
                    request_settings['authentication']['userName'] = test_config['requests']['username']
                    request_settings['authentication']['password'] = test_config['requests']['password']
                    request_settings['authentication']['authenticationMethodType'] = utils.Utils.authentication_type_id(test_config['requests']['authentication_type'])
        for http_header in test_config['requests']['http_headers']:
            for http_header_request in override_settings['request_settings']['http_header_requests']:
                if http_header == http_header_request['headerName']:
                    http_header_list.append(http_header_request)
        request_settings['httpHeaderRequests'] = http_header_list

        return request_settings 

    # function to override alert section
    def alert_settings(self, test_config, override_settings):
        alert_setting = {}
        alert_group_items = []
        alert_setting = override_settings['alerts']['overridden']
        alert_setting['notificationGroup'] = override_settings['alerts']['notification_group']
        alert_setting['notificationGroup']['alertWebhooks'] = utils.Utils.alert_webhook_id(test_config['alerts']['alert_webhook_id'])
        alert_setting['notificationGroup']['recipients'] = test_config['alerts']['recipients']
        for alert_type_detail in test_config['alerts']['alert_type_details']:
            temp = {}
            if alert_type_detail['alert_type'] == 'test_time_with_suspect':
                temp = override_settings['alerts']['alert_group_items']
                temp['trigger']['operationType'] = utils.Utils.operation_type_id(alert_type_detail['time_trigger']['warning_operator_id'])
                temp['trigger']['warningTrigger'] = alert_type_detail['time_trigger']['warning']
                temp['trigger']['criticalTrigger'] = alert_type_detail['time_trigger']['critical']
                temp['alertType'] = override_settings['alerts']['alert_type']['test_time_with_suspect']
                temp['alertSubType'] = override_settings['alerts']['alert_type']['test_time_with_suspect_sub_alert']
                if alert_type_detail['number_of_runs'] is True:
                     temp['nodeThreshold']['numberOfUnits'] = alert_type_detail['number_of_runs']
                elif alert_type_detail['percentage_of_runs'] is True:
                    temp['nodeThreshold']['percentageOfUnits'] = alert_type_detail['percentage_of_runs']
            elif alert_type_detail['alert_type'] == 'test_failure':
                temp = override_settings['alerts']['alert_group_items']
                temp['trigger']['operationType'] = utils.Utils.operation_type_id(None)
                temp['alertType'] = override_settings['alerts']['alert_type']['test_failure']
                if alert_type_detail['number_of_runs'] is True:
                     temp['nodeThreshold']['numberOfUnits'] = alert_type_detail['number_of_runs']
                elif alert_type_detail['percentage_of_runs'] is True:
                    temp['nodeThreshold']['percentageOfUnits'] = alert_type_detail['percentage_of_runs']
            elif alert_type_detail['alert_type'] == 'host_failure':
                temp = override_settings['alerts']['alert_group_items']
                temp['trigger']['operationType'] = utils.Utils.operation_type_id(None)
                temp['alertType'] = override_settings['alerts']['alert_type']['host_failure']
                if alert_type_detail['number_of_runs'] is True:
                     temp['nodeThreshold']['numberOfUnits'] = alert_type_detail['number_of_runs']
                elif alert_type_detail['percentage_of_runs'] is True:
                    temp['nodeThreshold']['percentageOfUnits'] = alert_type_detail['percentage_of_runs']
            alert_group_items.append(temp)
        alert_setting['alertGroupItems'] = alert_group_items
        return alert_setting