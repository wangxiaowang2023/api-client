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

class IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams(object):
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
        'controller_enabled': 'bool'
    }

    attribute_map = {
        'controller_enabled': 'controller_enabled'
    }

    def __init__(self, controller_enabled=None):  # noqa: E501
        """IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams - a model defined in Swagger"""  # noqa: E501
        self._controller_enabled = None
        self.discriminator = None
        if controller_enabled is not None:
            self.controller_enabled = controller_enabled

    @property
    def controller_enabled(self):
        """Gets the controller_enabled of this IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams.  # noqa: E501

        controller_enabled enables or disables the controller submodule.  # noqa: E501

        :return: The controller_enabled of this IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams.  # noqa: E501
        :rtype: bool
        """
        return self._controller_enabled

    @controller_enabled.setter
    def controller_enabled(self, controller_enabled):
        """Sets the controller_enabled of this IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams.

        controller_enabled enables or disables the controller submodule.  # noqa: E501

        :param controller_enabled: The controller_enabled of this IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams.  # noqa: E501
        :type: bool
        """

        self._controller_enabled = controller_enabled

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
        if issubclass(IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams, dict):
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
        if not isinstance(other, IbcApplicationsInterchainAccountsControllerV1QueryParamsResponseParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
