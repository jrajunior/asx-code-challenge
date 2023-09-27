import json
import sys
import requests

def validate_json(json_file):
    try:
        data = json.load(json_file)
    except ValueError as err:
        return {}
    return data

json_file = open('example.json')

vm_list = validate_json(json_file)

if not vm_list:
    print('Invalid Json')
    sys.exit(1)

public_vm_list = {}

for vm_key, vm_value in vm_list.items():
    if vm_value["private"] == False:
        public_vm_list[vm_key] = vm_value

print(public_vm_list)

url = 'https://www.asx.com.au/service/generate'

response = requests.post(url, public_vm_list)

mock_response = '''
{
  "test_false": {
    "dnszone": "whatever.asx.com.au.",
    "targets": "10.10.10.10",
    "private": true,
    "valid": false
  },
  "digital": {
    "dnszone": "digital.asx.com.au.",
    "targets": "10.1.4.1",
    "private": false,
    "valid": true
  }
}
'''

services = json.loads(mock_response)

for service_key, service_value in services.items():
    if service_value["valid"] == True:
        print(service_key)