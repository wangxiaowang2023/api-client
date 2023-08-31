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

class CosmosTxV1beta1ModeInfoMulti(object):
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
        'bitarray': 'BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning',
        'mode_infos': 'list[CosmosTxV1beta1ModeInfo]'
    }

    attribute_map = {
        'bitarray': 'bitarray',
        'mode_infos': 'mode_infos'
    }

    def __init__(self, bitarray=None, mode_infos=None):  # noqa: E501
        """CosmosTxV1beta1ModeInfoMulti - a model defined in Swagger"""  # noqa: E501
        self._bitarray = None
        self._mode_infos = None
        self.discriminator = None
        if bitarray is not None:
            self.bitarray = bitarray
        if mode_infos is not None:
            self.mode_infos = mode_infos

    @property
    def bitarray(self):
        """Gets the bitarray of this CosmosTxV1beta1ModeInfoMulti.  # noqa: E501


        :return: The bitarray of this CosmosTxV1beta1ModeInfoMulti.  # noqa: E501
        :rtype: BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning
        """
        return self._bitarray

    @bitarray.setter
    def bitarray(self, bitarray):
        """Sets the bitarray of this CosmosTxV1beta1ModeInfoMulti.


        :param bitarray: The bitarray of this CosmosTxV1beta1ModeInfoMulti.  # noqa: E501
        :type: BitarraySpecifiesWhichKeysWithinTheMultisigAreSigning
        """

        self._bitarray = bitarray

    @property
    def mode_infos(self):
        """Gets the mode_infos of this CosmosTxV1beta1ModeInfoMulti.  # noqa: E501


        :return: The mode_infos of this CosmosTxV1beta1ModeInfoMulti.  # noqa: E501
        :rtype: list[CosmosTxV1beta1ModeInfo]
        """
        return self._mode_infos

    @mode_infos.setter
    def mode_infos(self, mode_infos):
        """Sets the mode_infos of this CosmosTxV1beta1ModeInfoMulti.


        :param mode_infos: The mode_infos of this CosmosTxV1beta1ModeInfoMulti.  # noqa: E501
        :type: list[CosmosTxV1beta1ModeInfo]
        """

        self._mode_infos = mode_infos

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
        if issubclass(CosmosTxV1beta1ModeInfoMulti, dict):
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
        if not isinstance(other, CosmosTxV1beta1ModeInfoMulti):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
