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

class CosmosGroupV1QueryGroupsByAdminResponseGroups(object):
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
        'id': 'str',
        'admin': 'str',
        'metadata': 'str',
        'version': 'str',
        'total_weight': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'admin': 'admin',
        'metadata': 'metadata',
        'version': 'version',
        'total_weight': 'total_weight',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, admin=None, metadata=None, version=None, total_weight=None, created_at=None):  # noqa: E501
        """CosmosGroupV1QueryGroupsByAdminResponseGroups - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._admin = None
        self._metadata = None
        self._version = None
        self._total_weight = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if admin is not None:
            self.admin = admin
        if metadata is not None:
            self.metadata = metadata
        if version is not None:
            self.version = version
        if total_weight is not None:
            self.total_weight = total_weight
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501

        id is the unique ID of the group.  # noqa: E501

        :return: The id of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CosmosGroupV1QueryGroupsByAdminResponseGroups.

        id is the unique ID of the group.  # noqa: E501

        :param id: The id of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def admin(self):
        """Gets the admin of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501

        admin is the account address of the group's admin.  # noqa: E501

        :return: The admin of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :rtype: str
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this CosmosGroupV1QueryGroupsByAdminResponseGroups.

        admin is the account address of the group's admin.  # noqa: E501

        :param admin: The admin of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :type: str
        """

        self._admin = admin

    @property
    def metadata(self):
        """Gets the metadata of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501

        metadata is any arbitrary metadata to attached to the group.  # noqa: E501

        :return: The metadata of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CosmosGroupV1QueryGroupsByAdminResponseGroups.

        metadata is any arbitrary metadata to attached to the group.  # noqa: E501

        :param metadata: The metadata of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def version(self):
        """Gets the version of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501


        :return: The version of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CosmosGroupV1QueryGroupsByAdminResponseGroups.


        :param version: The version of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def total_weight(self):
        """Gets the total_weight of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501

        total_weight is the sum of the group members' weights.  # noqa: E501

        :return: The total_weight of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :rtype: str
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this CosmosGroupV1QueryGroupsByAdminResponseGroups.

        total_weight is the sum of the group members' weights.  # noqa: E501

        :param total_weight: The total_weight of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :type: str
        """

        self._total_weight = total_weight

    @property
    def created_at(self):
        """Gets the created_at of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501

        created_at is a timestamp specifying when a group was created.  # noqa: E501

        :return: The created_at of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CosmosGroupV1QueryGroupsByAdminResponseGroups.

        created_at is a timestamp specifying when a group was created.  # noqa: E501

        :param created_at: The created_at of this CosmosGroupV1QueryGroupsByAdminResponseGroups.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(CosmosGroupV1QueryGroupsByAdminResponseGroups, dict):
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
        if not isinstance(other, CosmosGroupV1QueryGroupsByAdminResponseGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
