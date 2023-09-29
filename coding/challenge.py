import json
from json.decoder import JSONDecodeError
import sys
import requests
import logging
import os


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

json_file = "example.json"
if os.path.isfile(json_file) is False:
    logger.error(f"File {json_file} does not exist. Aborting script")
    sys.exit(1)

try:
    vm_list = json.load(open(json_file))
except JSONDecodeError as exc:
    logger.exception(exc)
    logger.error(f"{json_file} is not a valid json file. Aborting script.")
    sys.exit(1)

logger.info(f"Filtering public vms")
public_vm_list = {}
for vm_key, vm_value in vm_list.items():
    if vm_value["private"] == False:
        logger.debug(f"{vm_key} is public. Removing from list")
        public_vm_list[vm_key] = vm_value

logging.debug(public_vm_list)

url = 'https://www.asx.com.au/service/generate'
logger.info("saving public vms")
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
logger.info(f"{len(services)} services created")
for service_key, service_value in services.items():
    if service_value["valid"] == True:
        print(service_key)