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

class CosmosBaseTendermintV1beta1ProofOp(object):
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
        'type': 'str',
        'key': 'str',
        'data': 'str'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key',
        'data': 'data'
    }

    def __init__(self, type=None, key=None, data=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1ProofOp - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._key = None
        self._data = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if key is not None:
            self.key = key
        if data is not None:
            self.data = data

    @property
    def type(self):
        """Gets the type of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501


        :return: The type of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CosmosBaseTendermintV1beta1ProofOp.


        :param type: The type of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def key(self):
        """Gets the key of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501


        :return: The key of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CosmosBaseTendermintV1beta1ProofOp.


        :param key: The key of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def data(self):
        """Gets the data of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501


        :return: The data of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CosmosBaseTendermintV1beta1ProofOp.


        :param data: The data of this CosmosBaseTendermintV1beta1ProofOp.  # noqa: E501
        :type: str
        """

        self._data = data

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
        if issubclass(CosmosBaseTendermintV1beta1ProofOp, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1ProofOp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
