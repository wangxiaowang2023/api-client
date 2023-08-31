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

class ConnectionAssociatedWithTheRequestIdentifier(object):
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
        'client_id': 'str',
        'versions': 'list[IbcCoreConnectionV1ConnectionEndVersions]',
        'state': 'str',
        'counterparty': 'IbcCoreConnectionV1IdentifiedConnectionCounterparty',
        'delay_period': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'versions': 'versions',
        'state': 'state',
        'counterparty': 'counterparty',
        'delay_period': 'delay_period'
    }

    def __init__(self, client_id=None, versions=None, state='STATE_UNINITIALIZED_UNSPECIFIED', counterparty=None, delay_period=None):  # noqa: E501
        """ConnectionAssociatedWithTheRequestIdentifier - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._versions = None
        self._state = None
        self._counterparty = None
        self._delay_period = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if versions is not None:
            self.versions = versions
        if state is not None:
            self.state = state
        if counterparty is not None:
            self.counterparty = counterparty
        if delay_period is not None:
            self.delay_period = delay_period

    @property
    def client_id(self):
        """Gets the client_id of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501

        client associated with this connection.  # noqa: E501

        :return: The client_id of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ConnectionAssociatedWithTheRequestIdentifier.

        client associated with this connection.  # noqa: E501

        :param client_id: The client_id of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def versions(self):
        """Gets the versions of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501

        IBC version which can be utilised to determine encodings or protocols for channels or packets utilising this connection.  # noqa: E501

        :return: The versions of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :rtype: list[IbcCoreConnectionV1ConnectionEndVersions]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ConnectionAssociatedWithTheRequestIdentifier.

        IBC version which can be utilised to determine encodings or protocols for channels or packets utilising this connection.  # noqa: E501

        :param versions: The versions of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :type: list[IbcCoreConnectionV1ConnectionEndVersions]
        """

        self._versions = versions

    @property
    def state(self):
        """Gets the state of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501

        current state of the connection end.  # noqa: E501

        :return: The state of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ConnectionAssociatedWithTheRequestIdentifier.

        current state of the connection end.  # noqa: E501

        :param state: The state of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATE_UNINITIALIZED_UNSPECIFIED", "STATE_INIT", "STATE_TRYOPEN", "STATE_OPEN"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def counterparty(self):
        """Gets the counterparty of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501


        :return: The counterparty of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :rtype: IbcCoreConnectionV1IdentifiedConnectionCounterparty
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this ConnectionAssociatedWithTheRequestIdentifier.


        :param counterparty: The counterparty of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :type: IbcCoreConnectionV1IdentifiedConnectionCounterparty
        """

        self._counterparty = counterparty

    @property
    def delay_period(self):
        """Gets the delay_period of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501

        delay period that must pass before a consensus state can be used for packet-verification NOTE: delay period logic is only implemented by some clients.  # noqa: E501

        :return: The delay_period of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._delay_period

    @delay_period.setter
    def delay_period(self, delay_period):
        """Sets the delay_period of this ConnectionAssociatedWithTheRequestIdentifier.

        delay period that must pass before a consensus state can be used for packet-verification NOTE: delay period logic is only implemented by some clients.  # noqa: E501

        :param delay_period: The delay_period of this ConnectionAssociatedWithTheRequestIdentifier.  # noqa: E501
        :type: str
        """

        self._delay_period = delay_period

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
        if issubclass(ConnectionAssociatedWithTheRequestIdentifier, dict):
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
        if not isinstance(other, ConnectionAssociatedWithTheRequestIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
