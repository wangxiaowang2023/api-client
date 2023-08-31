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

class CosmosGovV1QueryVotesResponse(object):
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
        'votes': 'list[CosmosGovV1QueryVotesResponseVotes]',
        'pagination': 'CosmosAuthV1beta1QueryAccountsResponsePagination'
    }

    attribute_map = {
        'votes': 'votes',
        'pagination': 'pagination'
    }

    def __init__(self, votes=None, pagination=None):  # noqa: E501
        """CosmosGovV1QueryVotesResponse - a model defined in Swagger"""  # noqa: E501
        self._votes = None
        self._pagination = None
        self.discriminator = None
        if votes is not None:
            self.votes = votes
        if pagination is not None:
            self.pagination = pagination

    @property
    def votes(self):
        """Gets the votes of this CosmosGovV1QueryVotesResponse.  # noqa: E501

        votes defines the queried votes.  # noqa: E501

        :return: The votes of this CosmosGovV1QueryVotesResponse.  # noqa: E501
        :rtype: list[CosmosGovV1QueryVotesResponseVotes]
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this CosmosGovV1QueryVotesResponse.

        votes defines the queried votes.  # noqa: E501

        :param votes: The votes of this CosmosGovV1QueryVotesResponse.  # noqa: E501
        :type: list[CosmosGovV1QueryVotesResponseVotes]
        """

        self._votes = votes

    @property
    def pagination(self):
        """Gets the pagination of this CosmosGovV1QueryVotesResponse.  # noqa: E501


        :return: The pagination of this CosmosGovV1QueryVotesResponse.  # noqa: E501
        :rtype: CosmosAuthV1beta1QueryAccountsResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this CosmosGovV1QueryVotesResponse.


        :param pagination: The pagination of this CosmosGovV1QueryVotesResponse.  # noqa: E501
        :type: CosmosAuthV1beta1QueryAccountsResponsePagination
        """

        self._pagination = pagination

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
        if issubclass(CosmosGovV1QueryVotesResponse, dict):
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
        if not isinstance(other, CosmosGovV1QueryVotesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
