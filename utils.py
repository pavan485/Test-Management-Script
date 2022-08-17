class Utils():
   
    @staticmethod
    def frequency_id(frequency):
        frequencies = { 
            "none":         0,
            "1 minute":     1,
            "5 minutes":    2,
            "10 minutes":   3,
            "15 minutes":   4,
            "20 minutes":   5,
            "30 minutes":   6,
            "60 minutes":   7,
            "2 hours":      8,
            "3 hours":      9,
            "4 hours":      10,
            "6 hours":      11,
            "8 hours":      12,
            "12 hours":     13,
            "24 hours":     14,
            "4 minutes":    15,
            "2 minutes":    16
        }
        for key, value in frequencies.items():
            if frequency == key:
                frequency_map = {
                    "id": value,
                    "name": key
                }
        return frequency_map
    
    def node_details(nodes):
        node_list = []
        for node_ids in nodes:
            node_details = {
                "id": node_ids,
                "name": 'node',
                "networkType": {
                    "id": 0,
                    "name": "Any"
                }
            }
            node_list.append(node_details)
        return node_list


    def node_distribution_id(node_distribution):
        node_distributions = {
        0: "random",
		1: "concurrent",
	    }
        for key, value in node_distributions.items():
            if node_distribution == value:
                test_node_distribution = {
                    "id": key,
                    "name": value
                }
                return test_node_distribution

    def node_threshold_id(node_threshold):
        node_threshold_types = {
            0: "runs",
            1: "average across nodes",
            2: "node",
        }
        for id, value in node_threshold_types.items():
            if node_threshold == value:
                return id
        return -1

    def operation_type_id(operation):
        operation_types = {
		0: "not equals",
		2: "greater than",
		3: "greater than or equals",
		4: "less than",
		5: "less than or equals",
	    }
        for id, value in operation_types.items():
            if operation == value:
                 operation_type = {
                    "id": id,
                    "name": value
                }
            else:
                operation_type = {
                    "id": 0,
                    "name": "NotEquals"
                }
        return operation_type

    def remainder_id(reminder):
        reminders = {
        0:    "none",
        1:    "1 minute",
        5:    "5 minutes",
        10:   "10 minutes",
        15:   "15 minutes",
        30:   "30 minutes",
        60:   "1 hour",
        1440: "daily"
        }
        for id, value in reminders.items():
            if reminder == value:
                return id
        return -1


    def alert_type_id(alert_type):
        alert_types = {
		9:  "test failure",
		7:  "timing",
		15: "availability"
	    }
        for id, value in alert_types.items():
            if alert_type == value:
                return id
        return -1

    
    def alert_sub_type_id(alert_subtype):
        alert_sub_types = {
        50:  "dns",
        51:  "connect",
        52:  "send",
        53:  "wait",
        54:  "load",
        55:  "ttfb",
        57:  "content load",
        58:  "response",
        59:  "test time",
        61:  "dom load",
        63:  "test time with suspect",
        64:  "server response",
        66:  "document complete",
        67:  "redirect",
        140: "test",
        141: "content",
        142: "% downtime"
	    }
        for id, value in alert_sub_types.items():
            if alert_subtype == value:
                return id
        return -1      

    def test_flag_id(test_flag): 
        test_flag_types = {
            2:  "verify_test_on_failure",
            3:  "debug_primary_host_on_failure",
            4:  "enable_http2",
            8:  "debug_referenced_hosts_on_failure",
            9:  "capture_http_headers",
            11: "capture_response_content",
            17: "ignore_ssl_failures",
            23: "host_data_collection_enabled",
            24: "zone_data_collection_enabled",
            27: "40x_or_50x_http_mark_successful",
            33: "30x_redirects_do_not_follow",
            36: "enable_self_versus_third_party_zones",
            37: "allow_test_download_limit_override",
        }
        for id, Value in test_flag_types.items():
            if test_flag == Value:
                return id
        return 0
      
    def alert_webhook_id(webhook_ids):
        webhook_list = []
        for webhook_id in webhook_ids:
            webhook_details = {
                'id':webhook_id
            }
            webhook_list.append(webhook_details)
        return webhook_list
        

    
    def req_header_type_id(request_header):
        request_header_types = {
            1:  "user_agent",
            2:  "accept",
            3:  "accept_encoding",
            4:  "accept_language",
            5:  "accept_charset",
            6:  "cookie",
            7:  "cache_control",
            9:  "pragma",
            10: "referer",
            12: "host",
            13: "request_override",
            14: "dns_override",
            15: "request_block",
            16: "request_delay"
	    }
        for id, request_header_type in request_header_types.items():
            if request_header_type == request_header:
                return id
        return 0

    def authentication_type_id(authentication_type):
        authentication_types = {
            1: "basic",
            2: "digest",
            3: "ntlm",
            5: "login"
        }
        for id, authentication in authentication_types.items():
            if authentication == authentication_type:
                authentication_id = {
                    "id": id,
                    "name": authentication
                }
                authentication_id['authenticationMethodType'] = authentication_id
                return authentication_id
        return -1
        