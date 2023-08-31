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

class QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc(object):
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
        'fee_enabled_channels': 'list[FeeEnabledChannelContainsThePortIDChannelIDForAFeeEnabledChannel]'
    }

    attribute_map = {
        'fee_enabled_channels': 'fee_enabled_channels'
    }

    def __init__(self, fee_enabled_channels=None):  # noqa: E501
        """QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc - a model defined in Swagger"""  # noqa: E501
        self._fee_enabled_channels = None
        self.discriminator = None
        if fee_enabled_channels is not None:
            self.fee_enabled_channels = fee_enabled_channels

    @property
    def fee_enabled_channels(self):
        """Gets the fee_enabled_channels of this QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc.  # noqa: E501


        :return: The fee_enabled_channels of this QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc.  # noqa: E501
        :rtype: list[FeeEnabledChannelContainsThePortIDChannelIDForAFeeEnabledChannel]
        """
        return self._fee_enabled_channels

    @fee_enabled_channels.setter
    def fee_enabled_channels(self, fee_enabled_channels):
        """Sets the fee_enabled_channels of this QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc.


        :param fee_enabled_channels: The fee_enabled_channels of this QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc.  # noqa: E501
        :type: list[FeeEnabledChannelContainsThePortIDChannelIDForAFeeEnabledChannel]
        """

        self._fee_enabled_channels = fee_enabled_channels

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
        if issubclass(QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc, dict):
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
        if not isinstance(other, QueryFeeEnabledChannelsResponseDefinesTheResponseTypeForTheFeeEnabledChannelsRpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
