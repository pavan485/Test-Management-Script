# TEST-MANAGEMENT-SCRIPT 
Catchpoint Integration with MongoDB
---
Test management script is a python script to set up tests in Catchpoint Portal based on details given in a config file. This script uses REST API v2 and allows to set up all test types with all properties supported in the UI. 

This integration makes use of a python script that runs to Post data to Catchpoint POST: API. It can be used to create a list of tests in the same division. 

## Prerequisites
1.	Python 3.8 installed
2.	Pip – latest available version installed
3.	Catchpoint account with REST API consumer

## Installation and Configuration
1.	Copy the ‘Test-Management-Script’ folder to your machine
2.	Run the below commands:
    •	Pip install requests
    •	Pip install sys
    •	Pip install html
    •	Pip install random
    •	Pip install logger
    •	Pip install yaml
3.	In the "catchpoint_config.yaml" file under “config” sub-directory, enter your Catchpoint API consumer key and secret
4.	In the tests object of the "test_config.yaml" file, enter the test details you want to create in an array format.


### Configuration

#### Basic test configuration
1.	Enter a new test name for the test to be created as shown in the below example.
    ````
    test_name: 'html_test'
    ````

2.	Add a description to your test.
    ````
    description: 'My html test’
    ````

3.	The status of the test can be set to ‘active’ or ‘inactive’.
    ````
    status: 'active’
    ````

4.	Enter your catchpoint division id.
    ````
    division_id: 1234
    ````

5.	Enter the product and folder id where the test should be created as shown below. For a new product or folder leave them blank 
    ````
    product_id: 15330
    folder_id: 1233
    ````

#### Test type and Monitor type 

Enter the test type and monitor type from the available test types, monitor types available corresponding to each test type is given below with example test data belonging to the test type.

````
test_type: web 
monitors: [‘chrome’, ‘object’, ‘emulated’, ‘playback’, ‘mobile’, ‘mobile_playback’]
test_url:`

test_type: ‘transaction’
monitor_type: [‘emulated’, ‘chrome’, ‘mobile’]
script:


test_type: ‘html’
monitor_type: [‘emulated’, ‘chrome’, ‘mobile’]
test_html:

test_type: ‘api
monitor_type: ‘ ‘
script:

test_type: ‘websocket’
monitor_type: ‘ ’
script:

test_type: ‘dns’
monitor_type: [‘direct’, ‘experience’]
test_url:

test_type: ‘ftp’
monitor_type: ‘’
test_url:

test_type: ‘transport’
monitor_type: [‘transport_tcp’, ‘transport_udp’]
test_url:
test_data

test_type: ‘ping’
monitor_type: [‘ping_icmp’ , ‘ping_tcp’, ‘ping_udp’]
test_url:

test_type: ‘traceroute’
monitor_type: [‘traceroute _tcp’,’ traceroute _udp’, ‘traceroute_icmp’]
test_url:

test_type: ‘custom’
monitor_type: [‘ssh’]
test_url:
user_name:
password

test_type: ‘ntp’
monitor_type: ‘’
test_url:

test_type: ‘imap’
monitor_type: ‘ ’
test_location

test_type: ‘streaming’
monitor_type: ‘’
test_url:

test_type: ‘mqtt’
monitor_type: ‘’
test_url

test_type: ‘ssl’
monitor_type:’’
test_location:

test_type: ‘bgp’
monitor_type: ‘’
prefix:

````
#### More settings 

Under more_settings enter the start and end time along with labels and enable test data webhook.

•	Enter start time for the test to be created.
o	start_time: '3/25/2022 4:00:00 AM'

•	Enter end time for the test to be created.
o	end_time: '8/28/2022 3:59:00 AM'

•	Set enable test data webhook to true or false.
o	enable_test_data_webhook: true

•	Enter labels in key:value format each key with one value. For keys with multiple values duplicate the key and enter the value as shown below.
o	labels: {‘key1’:’val1’,’key2’:’val2’, ‘key1’:’value3’}


#### Thresholds

•	Under thresholds specify the test_time_warning and test_time_critical in (ms) where test_time_warning is lesser than test_time_critical as show in the below example.

o	test_time_warning: 30
o	test_time_critical: 50

•	Specify the availability_warning and availability_critical the availability_warning is greater than availability_critical as show in the below example.

o	availability_warning: 80
o	availability_critical: 40



#### Override

Under override set the sections required to be overridden to true and ignore the sections to be inherited as shown below.
````
override: {
    requests: true,
    advanced_settings: true,
    insights: true,
    targetting_schedule_settings: ,
    alerts: true
  }
  
````


#### Advanced settings

Under advanced_settings enter test flag ids as shown in the example from the list of available test flags.
````
Test_flag_ids:  [2,8,27]
````
````
[
   {
      ‘id’: 2,
      ‘name’: ‘Verify Test on Failure’
    },
    {
      ‘id’: 3,
      ‘name’: ‘Debug Primary Host on Failure’
    },
    {
      ‘id’: 8,
      ‘name’: ‘Debug Referenced Hosts on Failure’
    },
    {
      ‘id’: 9,
      ‘name’: ‘Capture HTTP Headers’
    },
    {
      ‘id’: 11,
      ‘name’: ‘Capture Response Content’
    },
    {
      ‘id’: 17,
      ‘name’: ‘Ignore SSL Failures’
    },
    {
      ‘id’: 23,
      ‘name’: ‘Host Data Collection Enabled’
    },
    {
      ‘id’: 24,
      ‘name’: ‘Zone Data Collection Enabled’
    },
    {
      ‘id’: 27,
      ‘name’: ‘Treat 40X or 50X HTTP Response as successful test run’
    },
    {
      ‘id’: 36,
      ‘name’: ‘Enable Self Versus Third Party Zones’
    },
    {
      ‘id’: 37,
      ‘name’: ‘Allow Test Download Limit Override’
    },
    {
      ‘id’: 10,
      ‘name’: ‘Capture HTTP headers on error’
    },
    {
      ‘id’: 14,
      ‘name’: ‘Capture Screenshot at Test End’
    }, 
    {
      ‘id’: 18,
      ‘name’: ‘Capture Screenshot on Error’
    },
    {
      ‘id’: 28,
      ‘name’: ‘Capture HTTP headers on error page’
    }
]
````
#### Requests

Configure each setting in the requests as mentioned below.

•	Enter authentication type available as shown from the list below.
````
authentication: ‘basic’
````
````
[
   1: ‘basic’,
   2: ‘digest’,
   3: ‘ntlm’,
   5: ‘login’
]
````

•	Enter the http header ids as shown below from the list.
````
http_headers: [1,3,4]
````
````

[
            1:  ‘user_agent’,
            2:  ‘accept’,
            3:  ‘accept_encoding’,
            4:  ‘accept_language’,
            5:  ‘accept_charset’,
            6:  ‘cookie’,
            7:  ‘cache_control’,
            9:  ‘pragma’,
            10: ‘referer’,
            12: ‘host’,
            13: ‘request_override’,
            14: ‘dns_override’,
            15: ‘request_block’,
            16: ‘request_delay’
 ]

````

#### Insights

Under insights configure indicators and tracepoints as mentioned below

•	Enter the required indicator ids  available below as shown below.
````
indicators: [8268, 6336, 6192]
````
````
        [
        8268: ‘Audio_out_bitrate’
        8268: ‘Audio_out_jitter’
        8267: ‘Audio_out_latency’
        6336: ‘Duration’
        6337: DurationTime1’
        6192 : ‘Content-Length’
        ]
````

•	Enter the required tracepoints available in the list as shown below.
````
tracepoints: [6193, 6194]
````
````
    [
    6194: ‘Server’
    6193: ‘X-cache’
    ]
````

Targeting and schedule settings

Configure targetting_schedule_settings as mentioned below:

•	Enter the frequency from the list of given frequencies.
````
frequency: ‘15 minutes’
````
````
        [
        ‘none’ 
        ‘1 minute’     
        ‘5 minutes’    
        ‘10 minutes’   
        ‘15 minutes’  
        ‘20 minutes’  
        ‘30 minutes’   
        ‘60 minutes’   
        ‘2 hours’      
        ‘3 hours’      
        ‘4 hours’      
        ‘6 hours’      
        ‘8 hours’      
        ‘12 hours’     
        ‘24 hours’     
        ‘4 minutes’
        ‘2 minutes’
        ]
````
•	Enter the node distribution id from the available node distributions available below as show below.
````
test_node_distribution_id: 1
````
````
        [
        0: ‘random’
        1: ‘concurrent’
        ]
 ````
 
•	Enter the node ids available from catchpoint portal as shown above.
    ````
    node_ids: [11,98,766]
    ````


#### Alerts
Configure test basic alerts as mentioned below:

•	Enter the recipient id along with email id available in your division to receive alerts as shown in below
````
recipients: [
                 {
                     id: 136997 ,
                     email: pkumars@catchpoint.com
      			  }
   		        ]
````

•	Enter the alert web hook ids as shown below.
````
alert_webhook_id: [1655,3614]
````


Available alert types:

‘test_failure’
For ‘test_failure’ alert specify the number_of_runs or percentage_of_runs as show above.

‘host_failure’
 
For ‘host_failure’ alert specify the number_of_runs or percentage_of_runs as show above.

‘test_time_with_suspect’

For ‘test_time_with_suspect’ alert type specify the number_of_runs or percentage_of_runs as show above and in time_trigger specify the warning and critical test time in ms.
Specify warning operator id from the below available ids 
````
[
0: ‘not equals’,
2: ‘greater than’,
3: ‘greater than or equals’,
4: ‘less than’,
5: ‘less than or equals’
]
````
````
    alert_type_details: [
      { 
      alert_type: 'test_failure',
      number_of_runs: 3, 
      percentage_of_runs: 30,
      time_trigger: {
        warning: 30,
        warning_operator_id: 2,
        critical: 40
        }
       }
    ]
````

*Example:*

````
 tests: [
{
  test_name: 'html123',
  description: '',
  status: 'active',
  division_id: 3876,
  product_id: 123 ,
  folder_id: 4567,
  test_type: 'html',
  monitor_type: 'emulated',
  test_url: '',
  test_location: '',
  ftp_upload_file_size: 10,
  user_name: 'demo',
  password: '12abc345',
  authtication: ,
  request_data: '',
  script: '',
  test_html: html><head></head><body><h1>This is python</h1></body></html',
  test_domain: '',
  prefix: '',
  more_settings: {
    start_time: '3/25/2022 4:00:00 AM',
    end_time: '8/28/2022 3:59:00 AM',
    enable_test_data_webhook: true,
    labels: {"abc":"val1","abcs":"val2"}
  },
  thresholds: {
    test_time_warning: 30,
    test_time_critical: 50,
    availability_warning: 80,
    availability_critical: 40
  },
  override: {
    requests: true,
    advanced_settings: true,
    insights: true,
    targetting_schedule_settings: ,
    alerts: true
  },
  advanced_settings: {
    test_flag_ids: []
  },
  requests: {
    authentication_type:  ,
    username: ,
    password: ,
    http_headers: []
  },
  insights: {
    indicators: [8268, 6336, 6192],
    tracepoints: [6193, 6194]
  },
  targetting_schedule_settings: {
    frequency: '15 minutes',
    test_node_distribution_id: 1,
    node_ids: [11,98,766]
  },
  alerts: {
    recipients: [
      {
      id: 136997 ,
      email: pkumars@catchpoint.com
      }
    ],
    alert_webhook_id: [1655,3614],
    alert_type_details: [
      { 
      alert_type: 'test_failure',
      number_of_runs: 3, 
      percentage_of_runs: 30,
      time_trigger: {
        warning: 30,
        warning_operator_id: 2,
        critical: 40
      }
    }
    ]
  }
}
]
````


## How to run
- In the /Test_Management-Script directory, run `python application.py` 



## File Structure

    Test_management-Script/     
    ├── config
    | ├── catchpoint_config.yaml   ## Configuration file for Catchpoint configuration to provide APIv2 key
    | ├── monitor_type.yaml        ## Configuration file that contains monitor details of each test type having monitors
    | ├── override_settings.yaml   ## Configuration file for Catchpoint 
    | ├── test_config.yaml         ## Configuration file for configuring tests in list of dictionaries
    | ├── test_type.yaml           ## Configuration file for different test types
    ├── logs
    | ├── app.log                  ## Contains informational and errorlogs. 
    ├── application.py             ## main file
    ├── log,py                     ## file to handle logs
    ├── payload_builder.py         ## contains methods to build payload for different test types
    ├── request_handler.py         ## handles post requests to create product, folder, test
    └── utils.py                   ## utilites for creating payload


Once the script runs all the tests configured will be setup onn catchpoint portal for the given division id.
