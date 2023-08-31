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

class CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate(object):
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
        'annual_rate_1_months': 'str',
        'annual_rate_3_months': 'str',
        'annual_rate_6_months': 'str',
        'annual_rate_12_months': 'str',
        'annual_rate_24_months': 'str',
        'annual_rate_36_months': 'str',
        'annual_rate_48_months': 'str'
    }

    attribute_map = {
        'annual_rate_1_months': 'annualRate_1_months',
        'annual_rate_3_months': 'annualRate_3_months',
        'annual_rate_6_months': 'annualRate_6_months',
        'annual_rate_12_months': 'annualRate_12_months',
        'annual_rate_24_months': 'annualRate_24_months',
        'annual_rate_36_months': 'annualRate_36_months',
        'annual_rate_48_months': 'annualRate_48_months'
    }

    def __init__(self, annual_rate_1_months=None, annual_rate_3_months=None, annual_rate_6_months=None, annual_rate_12_months=None, annual_rate_24_months=None, annual_rate_36_months=None, annual_rate_48_months=None):  # noqa: E501
        """CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate - a model defined in Swagger"""  # noqa: E501
        self._annual_rate_1_months = None
        self._annual_rate_3_months = None
        self._annual_rate_6_months = None
        self._annual_rate_12_months = None
        self._annual_rate_24_months = None
        self._annual_rate_36_months = None
        self._annual_rate_48_months = None
        self.discriminator = None
        if annual_rate_1_months is not None:
            self.annual_rate_1_months = annual_rate_1_months
        if annual_rate_3_months is not None:
            self.annual_rate_3_months = annual_rate_3_months
        if annual_rate_6_months is not None:
            self.annual_rate_6_months = annual_rate_6_months
        if annual_rate_12_months is not None:
            self.annual_rate_12_months = annual_rate_12_months
        if annual_rate_24_months is not None:
            self.annual_rate_24_months = annual_rate_24_months
        if annual_rate_36_months is not None:
            self.annual_rate_36_months = annual_rate_36_months
        if annual_rate_48_months is not None:
            self.annual_rate_48_months = annual_rate_48_months

    @property
    def annual_rate_1_months(self):
        """Gets the annual_rate_1_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_1_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_1_months

    @annual_rate_1_months.setter
    def annual_rate_1_months(self, annual_rate_1_months):
        """Sets the annual_rate_1_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_1_months: The annual_rate_1_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_1_months = annual_rate_1_months

    @property
    def annual_rate_3_months(self):
        """Gets the annual_rate_3_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_3_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_3_months

    @annual_rate_3_months.setter
    def annual_rate_3_months(self, annual_rate_3_months):
        """Sets the annual_rate_3_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_3_months: The annual_rate_3_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_3_months = annual_rate_3_months

    @property
    def annual_rate_6_months(self):
        """Gets the annual_rate_6_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_6_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_6_months

    @annual_rate_6_months.setter
    def annual_rate_6_months(self, annual_rate_6_months):
        """Sets the annual_rate_6_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_6_months: The annual_rate_6_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_6_months = annual_rate_6_months

    @property
    def annual_rate_12_months(self):
        """Gets the annual_rate_12_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_12_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_12_months

    @annual_rate_12_months.setter
    def annual_rate_12_months(self, annual_rate_12_months):
        """Sets the annual_rate_12_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_12_months: The annual_rate_12_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_12_months = annual_rate_12_months

    @property
    def annual_rate_24_months(self):
        """Gets the annual_rate_24_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_24_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_24_months

    @annual_rate_24_months.setter
    def annual_rate_24_months(self, annual_rate_24_months):
        """Sets the annual_rate_24_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_24_months: The annual_rate_24_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_24_months = annual_rate_24_months

    @property
    def annual_rate_36_months(self):
        """Gets the annual_rate_36_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_36_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_36_months

    @annual_rate_36_months.setter
    def annual_rate_36_months(self, annual_rate_36_months):
        """Sets the annual_rate_36_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_36_months: The annual_rate_36_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_36_months = annual_rate_36_months

    @property
    def annual_rate_48_months(self):
        """Gets the annual_rate_48_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501


        :return: The annual_rate_48_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :rtype: str
        """
        return self._annual_rate_48_months

    @annual_rate_48_months.setter
    def annual_rate_48_months(self, annual_rate_48_months):
        """Sets the annual_rate_48_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.


        :param annual_rate_48_months: The annual_rate_48_months of this CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate.  # noqa: E501
        :type: str
        """

        self._annual_rate_48_months = annual_rate_48_months

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
        if issubclass(CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate, dict):
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
        if not isinstance(other, CosmosStakingV1beta1QueryGetFixedDepositInterestRateResponseFixedDepositAnnualRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
