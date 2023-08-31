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

class InlineResponse20025(object):
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
        'block_id': 'BlockID',
        'block': 'DeprecatedPleaseUseSdkBlockInstead',
        'sdk_block': 'SinceCosmossdk047'
    }

    attribute_map = {
        'block_id': 'block_id',
        'block': 'block',
        'sdk_block': 'sdk_block'
    }

    def __init__(self, block_id=None, block=None, sdk_block=None):  # noqa: E501
        """InlineResponse20025 - a model defined in Swagger"""  # noqa: E501
        self._block_id = None
        self._block = None
        self._sdk_block = None
        self.discriminator = None
        if block_id is not None:
            self.block_id = block_id
        if block is not None:
            self.block = block
        if sdk_block is not None:
            self.sdk_block = sdk_block

    @property
    def block_id(self):
        """Gets the block_id of this InlineResponse20025.  # noqa: E501


        :return: The block_id of this InlineResponse20025.  # noqa: E501
        :rtype: BlockID
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this InlineResponse20025.


        :param block_id: The block_id of this InlineResponse20025.  # noqa: E501
        :type: BlockID
        """

        self._block_id = block_id

    @property
    def block(self):
        """Gets the block of this InlineResponse20025.  # noqa: E501


        :return: The block of this InlineResponse20025.  # noqa: E501
        :rtype: DeprecatedPleaseUseSdkBlockInstead
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this InlineResponse20025.


        :param block: The block of this InlineResponse20025.  # noqa: E501
        :type: DeprecatedPleaseUseSdkBlockInstead
        """

        self._block = block

    @property
    def sdk_block(self):
        """Gets the sdk_block of this InlineResponse20025.  # noqa: E501


        :return: The sdk_block of this InlineResponse20025.  # noqa: E501
        :rtype: SinceCosmossdk047
        """
        return self._sdk_block

    @sdk_block.setter
    def sdk_block(self, sdk_block):
        """Sets the sdk_block of this InlineResponse20025.


        :param sdk_block: The sdk_block of this InlineResponse20025.  # noqa: E501
        :type: SinceCosmossdk047
        """

        self._sdk_block = sdk_block

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
        if issubclass(InlineResponse20025, dict):
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
        if not isinstance(other, InlineResponse20025):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
