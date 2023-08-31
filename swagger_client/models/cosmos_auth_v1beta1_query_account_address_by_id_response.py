# coding: utf-8

"""
    HTTP API Console

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CosmosAuthV1beta1QueryAccountAddressByIDResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_address': 'str'
    }

    attribute_map = {
        'account_address': 'account_address'
    }

    def __init__(self, account_address=None):  # noqa: E501
        """CosmosAuthV1beta1QueryAccountAddressByIDResponse - a model defined in Swagger"""  # noqa: E501
        self._account_address = None
        self.discriminator = None
        if account_address is not None:
            self.account_address = account_address

    @property
    def account_address(self):
        """Gets the account_address of this CosmosAuthV1beta1QueryAccountAddressByIDResponse.  # noqa: E501


        :return: The account_address of this CosmosAuthV1beta1QueryAccountAddressByIDResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_address

    @account_address.setter
    def account_address(self, account_address):
        """Sets the account_address of this CosmosAuthV1beta1QueryAccountAddressByIDResponse.


        :param account_address: The account_address of this CosmosAuthV1beta1QueryAccountAddressByIDResponse.  # noqa: E501
        :type: str
        """

        self._account_address = account_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CosmosAuthV1beta1QueryAccountAddressByIDResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CosmosAuthV1beta1QueryAccountAddressByIDResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
