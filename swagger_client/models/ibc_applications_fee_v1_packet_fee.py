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

class IbcApplicationsFeeV1PacketFee(object):
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
        'fee': 'FeeEncapsulatesTheRecvAckAndTimeoutFeesAssociatedWithAnIBCPacket',
        'refund_address': 'str',
        'relayers': 'list[str]'
    }

    attribute_map = {
        'fee': 'fee',
        'refund_address': 'refund_address',
        'relayers': 'relayers'
    }

    def __init__(self, fee=None, refund_address=None, relayers=None):  # noqa: E501
        """IbcApplicationsFeeV1PacketFee - a model defined in Swagger"""  # noqa: E501
        self._fee = None
        self._refund_address = None
        self._relayers = None
        self.discriminator = None
        if fee is not None:
            self.fee = fee
        if refund_address is not None:
            self.refund_address = refund_address
        if relayers is not None:
            self.relayers = relayers

    @property
    def fee(self):
        """Gets the fee of this IbcApplicationsFeeV1PacketFee.  # noqa: E501


        :return: The fee of this IbcApplicationsFeeV1PacketFee.  # noqa: E501
        :rtype: FeeEncapsulatesTheRecvAckAndTimeoutFeesAssociatedWithAnIBCPacket
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this IbcApplicationsFeeV1PacketFee.


        :param fee: The fee of this IbcApplicationsFeeV1PacketFee.  # noqa: E501
        :type: FeeEncapsulatesTheRecvAckAndTimeoutFeesAssociatedWithAnIBCPacket
        """

        self._fee = fee

    @property
    def refund_address(self):
        """Gets the refund_address of this IbcApplicationsFeeV1PacketFee.  # noqa: E501


        :return: The refund_address of this IbcApplicationsFeeV1PacketFee.  # noqa: E501
        :rtype: str
        """
        return self._refund_address

    @refund_address.setter
    def refund_address(self, refund_address):
        """Sets the refund_address of this IbcApplicationsFeeV1PacketFee.


        :param refund_address: The refund_address of this IbcApplicationsFeeV1PacketFee.  # noqa: E501
        :type: str
        """

        self._refund_address = refund_address

    @property
    def relayers(self):
        """Gets the relayers of this IbcApplicationsFeeV1PacketFee.  # noqa: E501


        :return: The relayers of this IbcApplicationsFeeV1PacketFee.  # noqa: E501
        :rtype: list[str]
        """
        return self._relayers

    @relayers.setter
    def relayers(self, relayers):
        """Sets the relayers of this IbcApplicationsFeeV1PacketFee.


        :param relayers: The relayers of this IbcApplicationsFeeV1PacketFee.  # noqa: E501
        :type: list[str]
        """

        self._relayers = relayers

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
        if issubclass(IbcApplicationsFeeV1PacketFee, dict):
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
        if not isinstance(other, IbcApplicationsFeeV1PacketFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
