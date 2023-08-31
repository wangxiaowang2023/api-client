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

class CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures(object):
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
        'block_id_flag': 'str',
        'validator_address': 'str',
        'timestamp': 'datetime',
        'signature': 'str'
    }

    attribute_map = {
        'block_id_flag': 'block_id_flag',
        'validator_address': 'validator_address',
        'timestamp': 'timestamp',
        'signature': 'signature'
    }

    def __init__(self, block_id_flag='BLOCK_ID_FLAG_UNKNOWN', validator_address=None, timestamp=None, signature=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures - a model defined in Swagger"""  # noqa: E501
        self._block_id_flag = None
        self._validator_address = None
        self._timestamp = None
        self._signature = None
        self.discriminator = None
        if block_id_flag is not None:
            self.block_id_flag = block_id_flag
        if validator_address is not None:
            self.validator_address = validator_address
        if timestamp is not None:
            self.timestamp = timestamp
        if signature is not None:
            self.signature = signature

    @property
    def block_id_flag(self):
        """Gets the block_id_flag of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501


        :return: The block_id_flag of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :rtype: str
        """
        return self._block_id_flag

    @block_id_flag.setter
    def block_id_flag(self, block_id_flag):
        """Sets the block_id_flag of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.


        :param block_id_flag: The block_id_flag of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :type: str
        """
        allowed_values = ["BLOCK_ID_FLAG_UNKNOWN", "BLOCK_ID_FLAG_ABSENT", "BLOCK_ID_FLAG_COMMIT", "BLOCK_ID_FLAG_NIL"]  # noqa: E501
        if block_id_flag not in allowed_values:
            raise ValueError(
                "Invalid value for `block_id_flag` ({0}), must be one of {1}"  # noqa: E501
                .format(block_id_flag, allowed_values)
            )

        self._block_id_flag = block_id_flag

    @property
    def validator_address(self):
        """Gets the validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501


        :return: The validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :rtype: str
        """
        return self._validator_address

    @validator_address.setter
    def validator_address(self, validator_address):
        """Sets the validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.


        :param validator_address: The validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :type: str
        """

        self._validator_address = validator_address

    @property
    def timestamp(self):
        """Gets the timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501


        :return: The timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.


        :param timestamp: The timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def signature(self):
        """Gets the signature of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501


        :return: The signature of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.


        :param signature: The signature of this CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures.  # noqa: E501
        :type: str
        """

        self._signature = signature

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
        if issubclass(CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockSignedHeaderCommitSignatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
