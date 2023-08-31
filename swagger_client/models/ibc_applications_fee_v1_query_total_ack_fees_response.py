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

class IbcApplicationsFeeV1QueryTotalAckFeesResponse(object):
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
        'ack_fees': 'list[CosmosBankV1beta1InputCoins]'
    }

    attribute_map = {
        'ack_fees': 'ack_fees'
    }

    def __init__(self, ack_fees=None):  # noqa: E501
        """IbcApplicationsFeeV1QueryTotalAckFeesResponse - a model defined in Swagger"""  # noqa: E501
        self._ack_fees = None
        self.discriminator = None
        if ack_fees is not None:
            self.ack_fees = ack_fees

    @property
    def ack_fees(self):
        """Gets the ack_fees of this IbcApplicationsFeeV1QueryTotalAckFeesResponse.  # noqa: E501


        :return: The ack_fees of this IbcApplicationsFeeV1QueryTotalAckFeesResponse.  # noqa: E501
        :rtype: list[CosmosBankV1beta1InputCoins]
        """
        return self._ack_fees

    @ack_fees.setter
    def ack_fees(self, ack_fees):
        """Sets the ack_fees of this IbcApplicationsFeeV1QueryTotalAckFeesResponse.


        :param ack_fees: The ack_fees of this IbcApplicationsFeeV1QueryTotalAckFeesResponse.  # noqa: E501
        :type: list[CosmosBankV1beta1InputCoins]
        """

        self._ack_fees = ack_fees

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
        if issubclass(IbcApplicationsFeeV1QueryTotalAckFeesResponse, dict):
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
        if not isinstance(other, IbcApplicationsFeeV1QueryTotalAckFeesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
