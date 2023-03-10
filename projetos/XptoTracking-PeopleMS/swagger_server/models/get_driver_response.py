# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class GetDriverResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, driver_id: str=None, name: str=None, customer_id: str=None, phone: str=None, mail: str=None):  # noqa: E501
        """GetDriverResponse - a model defined in Swagger

        :param driver_id: The driver_id of this GetDriverResponse.  # noqa: E501
        :type driver_id: str
        :param name: The name of this GetDriverResponse.  # noqa: E501
        :type name: str
        :param customer_id: The customer_id of this GetDriverResponse.  # noqa: E501
        :type customer_id: str
        :param phone: The phone of this GetDriverResponse.  # noqa: E501
        :type phone: str
        :param mail: The mail of this GetDriverResponse.  # noqa: E501
        :type mail: str
        """
        self.swagger_types = {
            'driver_id': str,
            'name': str,
            'customer_id': str,
            'phone': str,
            'mail': str
        }

        self.attribute_map = {
            'driver_id': 'driverId',
            'name': 'name',
            'customer_id': 'customerId',
            'phone': 'phone',
            'mail': 'mail'
        }
        self._driver_id = driver_id
        self._name = name
        self._customer_id = customer_id
        self._phone = phone
        self._mail = mail

    @classmethod
    def from_dict(cls, dikt) -> 'GetDriverResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetDriverResponse of this GetDriverResponse.  # noqa: E501
        :rtype: GetDriverResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def driver_id(self) -> str:
        """Gets the driver_id of this GetDriverResponse.


        :return: The driver_id of this GetDriverResponse.
        :rtype: str
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id: str):
        """Sets the driver_id of this GetDriverResponse.


        :param driver_id: The driver_id of this GetDriverResponse.
        :type driver_id: str
        """
        if driver_id is None:
            raise ValueError("Invalid value for `driver_id`, must not be `None`")  # noqa: E501

        self._driver_id = driver_id

    @property
    def name(self) -> str:
        """Gets the name of this GetDriverResponse.

        Complete Driver name  # noqa: E501

        :return: The name of this GetDriverResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this GetDriverResponse.

        Complete Driver name  # noqa: E501

        :param name: The name of this GetDriverResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def customer_id(self) -> str:
        """Gets the customer_id of this GetDriverResponse.


        :return: The customer_id of this GetDriverResponse.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """Sets the customer_id of this GetDriverResponse.


        :param customer_id: The customer_id of this GetDriverResponse.
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def phone(self) -> str:
        """Gets the phone of this GetDriverResponse.

        Telephone number  # noqa: E501

        :return: The phone of this GetDriverResponse.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this GetDriverResponse.

        Telephone number  # noqa: E501

        :param phone: The phone of this GetDriverResponse.
        :type phone: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def mail(self) -> str:
        """Gets the mail of this GetDriverResponse.

        E-mail address  # noqa: E501

        :return: The mail of this GetDriverResponse.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """Sets the mail of this GetDriverResponse.

        E-mail address  # noqa: E501

        :param mail: The mail of this GetDriverResponse.
        :type mail: str
        """
        if mail is None:
            raise ValueError("Invalid value for `mail`, must not be `None`")  # noqa: E501

        self._mail = mail
