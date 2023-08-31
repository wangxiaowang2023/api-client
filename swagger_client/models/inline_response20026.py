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

class InlineResponse20026(object):
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
        'default_node_info': 'InlineResponse20026DefaultNodeInfo',
        'application_version': 'CosmosBaseTendermintV1beta1GetNodeInfoResponseApplicationVersion'
    }

    attribute_map = {
        'default_node_info': 'default_node_info',
        'application_version': 'application_version'
    }

    def __init__(self, default_node_info=None, application_version=None):  # noqa: E501
        """InlineResponse20026 - a model defined in Swagger"""  # noqa: E501
        self._default_node_info = None
        self._application_version = None
        self.discriminator = None
        if default_node_info is not None:
            self.default_node_info = default_node_info
        if application_version is not None:
            self.application_version = application_version

    @property
    def default_node_info(self):
        """Gets the default_node_info of this InlineResponse20026.  # noqa: E501


        :return: The default_node_info of this InlineResponse20026.  # noqa: E501
        :rtype: InlineResponse20026DefaultNodeInfo
        """
        return self._default_node_info

    @default_node_info.setter
    def default_node_info(self, default_node_info):
        """Sets the default_node_info of this InlineResponse20026.


        :param default_node_info: The default_node_info of this InlineResponse20026.  # noqa: E501
        :type: InlineResponse20026DefaultNodeInfo
        """

        self._default_node_info = default_node_info

    @property
    def application_version(self):
        """Gets the application_version of this InlineResponse20026.  # noqa: E501


        :return: The application_version of this InlineResponse20026.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1GetNodeInfoResponseApplicationVersion
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this InlineResponse20026.


        :param application_version: The application_version of this InlineResponse20026.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1GetNodeInfoResponseApplicationVersion
        """

        self._application_version = application_version

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
        if issubclass(InlineResponse20026, dict):
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
        if not isinstance(other, InlineResponse20026):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
