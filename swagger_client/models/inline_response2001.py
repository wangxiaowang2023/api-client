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

class InlineResponse2001(object):
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
        'accounts': 'list[dict(str, object)]',
        'pagination': 'CosmosAuthV1beta1QueryAccountsResponsePagination'
    }

    attribute_map = {
        'accounts': 'accounts',
        'pagination': 'pagination'
    }

    def __init__(self, accounts=None, pagination=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._accounts = None
        self._pagination = None
        self.discriminator = None
        if accounts is not None:
            self.accounts = accounts
        if pagination is not None:
            self.pagination = pagination

    @property
    def accounts(self):
        """Gets the accounts of this InlineResponse2001.  # noqa: E501


        :return: The accounts of this InlineResponse2001.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this InlineResponse2001.


        :param accounts: The accounts of this InlineResponse2001.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._accounts = accounts

    @property
    def pagination(self):
        """Gets the pagination of this InlineResponse2001.  # noqa: E501


        :return: The pagination of this InlineResponse2001.  # noqa: E501
        :rtype: CosmosAuthV1beta1QueryAccountsResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this InlineResponse2001.


        :param pagination: The pagination of this InlineResponse2001.  # noqa: E501
        :type: CosmosAuthV1beta1QueryAccountsResponsePagination
        """

        self._pagination = pagination

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
