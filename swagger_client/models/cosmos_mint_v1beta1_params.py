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

class CosmosMintV1beta1Params(object):
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
        'mint_denom': 'str',
        'inflation_rate_change': 'str',
        'inflation_max': 'str',
        'inflation_min': 'str',
        'goal_bonded': 'str',
        'blocks_per_year': 'str'
    }

    attribute_map = {
        'mint_denom': 'mint_denom',
        'inflation_rate_change': 'inflation_rate_change',
        'inflation_max': 'inflation_max',
        'inflation_min': 'inflation_min',
        'goal_bonded': 'goal_bonded',
        'blocks_per_year': 'blocks_per_year'
    }

    def __init__(self, mint_denom=None, inflation_rate_change=None, inflation_max=None, inflation_min=None, goal_bonded=None, blocks_per_year=None):  # noqa: E501
        """CosmosMintV1beta1Params - a model defined in Swagger"""  # noqa: E501
        self._mint_denom = None
        self._inflation_rate_change = None
        self._inflation_max = None
        self._inflation_min = None
        self._goal_bonded = None
        self._blocks_per_year = None
        self.discriminator = None
        if mint_denom is not None:
            self.mint_denom = mint_denom
        if inflation_rate_change is not None:
            self.inflation_rate_change = inflation_rate_change
        if inflation_max is not None:
            self.inflation_max = inflation_max
        if inflation_min is not None:
            self.inflation_min = inflation_min
        if goal_bonded is not None:
            self.goal_bonded = goal_bonded
        if blocks_per_year is not None:
            self.blocks_per_year = blocks_per_year

    @property
    def mint_denom(self):
        """Gets the mint_denom of this CosmosMintV1beta1Params.  # noqa: E501


        :return: The mint_denom of this CosmosMintV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._mint_denom

    @mint_denom.setter
    def mint_denom(self, mint_denom):
        """Sets the mint_denom of this CosmosMintV1beta1Params.


        :param mint_denom: The mint_denom of this CosmosMintV1beta1Params.  # noqa: E501
        :type: str
        """

        self._mint_denom = mint_denom

    @property
    def inflation_rate_change(self):
        """Gets the inflation_rate_change of this CosmosMintV1beta1Params.  # noqa: E501


        :return: The inflation_rate_change of this CosmosMintV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._inflation_rate_change

    @inflation_rate_change.setter
    def inflation_rate_change(self, inflation_rate_change):
        """Sets the inflation_rate_change of this CosmosMintV1beta1Params.


        :param inflation_rate_change: The inflation_rate_change of this CosmosMintV1beta1Params.  # noqa: E501
        :type: str
        """

        self._inflation_rate_change = inflation_rate_change

    @property
    def inflation_max(self):
        """Gets the inflation_max of this CosmosMintV1beta1Params.  # noqa: E501


        :return: The inflation_max of this CosmosMintV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._inflation_max

    @inflation_max.setter
    def inflation_max(self, inflation_max):
        """Sets the inflation_max of this CosmosMintV1beta1Params.


        :param inflation_max: The inflation_max of this CosmosMintV1beta1Params.  # noqa: E501
        :type: str
        """

        self._inflation_max = inflation_max

    @property
    def inflation_min(self):
        """Gets the inflation_min of this CosmosMintV1beta1Params.  # noqa: E501


        :return: The inflation_min of this CosmosMintV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._inflation_min

    @inflation_min.setter
    def inflation_min(self, inflation_min):
        """Sets the inflation_min of this CosmosMintV1beta1Params.


        :param inflation_min: The inflation_min of this CosmosMintV1beta1Params.  # noqa: E501
        :type: str
        """

        self._inflation_min = inflation_min

    @property
    def goal_bonded(self):
        """Gets the goal_bonded of this CosmosMintV1beta1Params.  # noqa: E501


        :return: The goal_bonded of this CosmosMintV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._goal_bonded

    @goal_bonded.setter
    def goal_bonded(self, goal_bonded):
        """Sets the goal_bonded of this CosmosMintV1beta1Params.


        :param goal_bonded: The goal_bonded of this CosmosMintV1beta1Params.  # noqa: E501
        :type: str
        """

        self._goal_bonded = goal_bonded

    @property
    def blocks_per_year(self):
        """Gets the blocks_per_year of this CosmosMintV1beta1Params.  # noqa: E501


        :return: The blocks_per_year of this CosmosMintV1beta1Params.  # noqa: E501
        :rtype: str
        """
        return self._blocks_per_year

    @blocks_per_year.setter
    def blocks_per_year(self, blocks_per_year):
        """Sets the blocks_per_year of this CosmosMintV1beta1Params.


        :param blocks_per_year: The blocks_per_year of this CosmosMintV1beta1Params.  # noqa: E501
        :type: str
        """

        self._blocks_per_year = blocks_per_year

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
        if issubclass(CosmosMintV1beta1Params, dict):
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
        if not isinstance(other, CosmosMintV1beta1Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
