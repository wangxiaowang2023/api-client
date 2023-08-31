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

class CosmwasmWasmV1QueryParamsResponseParams(object):
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
        'code_upload_access': 'CosmwasmWasmV1CodeInfoResponseInstantiatePermission',
        'instantiate_default_permission': 'str'
    }

    attribute_map = {
        'code_upload_access': 'code_upload_access',
        'instantiate_default_permission': 'instantiate_default_permission'
    }

    def __init__(self, code_upload_access=None, instantiate_default_permission='ACCESS_TYPE_UNSPECIFIED'):  # noqa: E501
        """CosmwasmWasmV1QueryParamsResponseParams - a model defined in Swagger"""  # noqa: E501
        self._code_upload_access = None
        self._instantiate_default_permission = None
        self.discriminator = None
        if code_upload_access is not None:
            self.code_upload_access = code_upload_access
        if instantiate_default_permission is not None:
            self.instantiate_default_permission = instantiate_default_permission

    @property
    def code_upload_access(self):
        """Gets the code_upload_access of this CosmwasmWasmV1QueryParamsResponseParams.  # noqa: E501


        :return: The code_upload_access of this CosmwasmWasmV1QueryParamsResponseParams.  # noqa: E501
        :rtype: CosmwasmWasmV1CodeInfoResponseInstantiatePermission
        """
        return self._code_upload_access

    @code_upload_access.setter
    def code_upload_access(self, code_upload_access):
        """Sets the code_upload_access of this CosmwasmWasmV1QueryParamsResponseParams.


        :param code_upload_access: The code_upload_access of this CosmwasmWasmV1QueryParamsResponseParams.  # noqa: E501
        :type: CosmwasmWasmV1CodeInfoResponseInstantiatePermission
        """

        self._code_upload_access = code_upload_access

    @property
    def instantiate_default_permission(self):
        """Gets the instantiate_default_permission of this CosmwasmWasmV1QueryParamsResponseParams.  # noqa: E501

        - ACCESS_TYPE_UNSPECIFIED: AccessTypeUnspecified placeholder for empty value  - ACCESS_TYPE_NOBODY: AccessTypeNobody forbidden  - ACCESS_TYPE_EVERYBODY: AccessTypeEverybody unrestricted  - ACCESS_TYPE_ANY_OF_ADDRESSES: AccessTypeAnyOfAddresses allow any of the addresses  # noqa: E501

        :return: The instantiate_default_permission of this CosmwasmWasmV1QueryParamsResponseParams.  # noqa: E501
        :rtype: str
        """
        return self._instantiate_default_permission

    @instantiate_default_permission.setter
    def instantiate_default_permission(self, instantiate_default_permission):
        """Sets the instantiate_default_permission of this CosmwasmWasmV1QueryParamsResponseParams.

        - ACCESS_TYPE_UNSPECIFIED: AccessTypeUnspecified placeholder for empty value  - ACCESS_TYPE_NOBODY: AccessTypeNobody forbidden  - ACCESS_TYPE_EVERYBODY: AccessTypeEverybody unrestricted  - ACCESS_TYPE_ANY_OF_ADDRESSES: AccessTypeAnyOfAddresses allow any of the addresses  # noqa: E501

        :param instantiate_default_permission: The instantiate_default_permission of this CosmwasmWasmV1QueryParamsResponseParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCESS_TYPE_UNSPECIFIED", "ACCESS_TYPE_NOBODY", "ACCESS_TYPE_EVERYBODY", "ACCESS_TYPE_ANY_OF_ADDRESSES"]  # noqa: E501
        if instantiate_default_permission not in allowed_values:
            raise ValueError(
                "Invalid value for `instantiate_default_permission` ({0}), must be one of {1}"  # noqa: E501
                .format(instantiate_default_permission, allowed_values)
            )

        self._instantiate_default_permission = instantiate_default_permission

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
        if issubclass(CosmwasmWasmV1QueryParamsResponseParams, dict):
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
        if not isinstance(other, CosmwasmWasmV1QueryParamsResponseParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
