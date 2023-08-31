# -*- coding: utf-8 -*-
from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = "http://192.168.0.207:1317/"
api_instance = swagger_client.QueryApi(swagger_client.ApiClient(configuration))

try:
    # CreateGroup creates a new group with an admin account address, a list of members and some optional metadata.
    api_response = api_instance.cosmos_auth_v1_beta1_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MsgApi->cosmos_group_v1_create_group: %s\n" % e)
