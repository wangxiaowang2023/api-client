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

class CosmosStakingV1beta1QueryAllKycResponseKyc(object):
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
        'account': 'str',
        'creator': 'str',
        'region_id': 'str',
        'region_name': 'str'
    }

    attribute_map = {
        'account': 'account',
        'creator': 'creator',
        'region_id': 'regionId',
        'region_name': 'regionName'
    }

    def __init__(self, account=None, creator=None, region_id=None, region_name=None):  # noqa: E501
        """CosmosStakingV1beta1QueryAllKycResponseKyc - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._creator = None
        self._region_id = None
        self._region_name = None
        self.discriminator = None
        if account is not None:
            self.account = account
        if creator is not None:
            self.creator = creator
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name

    @property
    def account(self):
        """Gets the account of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501


        :return: The account of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CosmosStakingV1beta1QueryAllKycResponseKyc.


        :param account: The account of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def creator(self):
        """Gets the creator of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501


        :return: The creator of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CosmosStakingV1beta1QueryAllKycResponseKyc.


        :param creator: The creator of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def region_id(self):
        """Gets the region_id of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501


        :return: The region_id of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CosmosStakingV1beta1QueryAllKycResponseKyc.


        :param region_id: The region_id of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501


        :return: The region_name of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this CosmosStakingV1beta1QueryAllKycResponseKyc.


        :param region_name: The region_name of this CosmosStakingV1beta1QueryAllKycResponseKyc.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

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
        if issubclass(CosmosStakingV1beta1QueryAllKycResponseKyc, dict):
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
        if not isinstance(other, CosmosStakingV1beta1QueryAllKycResponseKyc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
