# coding: utf-8

"""
    Huidige bevragingen API

    Deze API levert actuele gegevens over adressen, adresseerbaar objecten en panden. Actueel betekent in deze API `zonder eindstatus`. De bron voor deze API is de basisregistratie adressen en gebouwen (BAG).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: bag@kadaster.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class WoonplaatsHal(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'identificatie': 'str',
        'domein': 'str',
        'naam': 'str',
        'status': 'StatusWoonplaatsEnum',
        'geconstateerd': 'bool',
        'documentdatum': 'date',
        'documentnummer': 'str',
        'mogelijk_onjuist': 'WoonplaatsMogelijkOnjuist',
        'links': 'WoonplaatsLinks',
        'embedded': 'WoonplaatsEmbedded'
    }

    attribute_map = {
        'identificatie': 'identificatie',
        'domein': 'domein',
        'naam': 'naam',
        'status': 'status',
        'geconstateerd': 'geconstateerd',
        'documentdatum': 'documentdatum',
        'documentnummer': 'documentnummer',
        'mogelijk_onjuist': 'mogelijkOnjuist',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, identificatie=None, domein=None, naam=None, status=None, geconstateerd=None, documentdatum=None, documentnummer=None, mogelijk_onjuist=None, links=None, embedded=None, local_vars_configuration=None):  # noqa: E501
        """WoonplaatsHal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._identificatie = None
        self._domein = None
        self._naam = None
        self._status = None
        self._geconstateerd = None
        self._documentdatum = None
        self._documentnummer = None
        self._mogelijk_onjuist = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if identificatie is not None:
            self.identificatie = identificatie
        if domein is not None:
            self.domein = domein
        if naam is not None:
            self.naam = naam
        if status is not None:
            self.status = status
        if geconstateerd is not None:
            self.geconstateerd = geconstateerd
        if documentdatum is not None:
            self.documentdatum = documentdatum
        if documentnummer is not None:
            self.documentnummer = documentnummer
        if mogelijk_onjuist is not None:
            self.mogelijk_onjuist = mogelijk_onjuist
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def identificatie(self):
        """Gets the identificatie of this WoonplaatsHal.  # noqa: E501


        :return: The identificatie of this WoonplaatsHal.  # noqa: E501
        :rtype: str
        """
        return self._identificatie

    @identificatie.setter
    def identificatie(self, identificatie):
        """Sets the identificatie of this WoonplaatsHal.


        :param identificatie: The identificatie of this WoonplaatsHal.  # noqa: E501
        :type: str
        """

        self._identificatie = identificatie

    @property
    def domein(self):
        """Gets the domein of this WoonplaatsHal.  # noqa: E501

        Het domein waartoe de identificatie behoort.  # noqa: E501

        :return: The domein of this WoonplaatsHal.  # noqa: E501
        :rtype: str
        """
        return self._domein

    @domein.setter
    def domein(self, domein):
        """Sets the domein of this WoonplaatsHal.

        Het domein waartoe de identificatie behoort.  # noqa: E501

        :param domein: The domein of this WoonplaatsHal.  # noqa: E501
        :type: str
        """

        self._domein = domein

    @property
    def naam(self):
        """Gets the naam of this WoonplaatsHal.  # noqa: E501

        De naam van de woonplaats.  # noqa: E501

        :return: The naam of this WoonplaatsHal.  # noqa: E501
        :rtype: str
        """
        return self._naam

    @naam.setter
    def naam(self, naam):
        """Sets the naam of this WoonplaatsHal.

        De naam van de woonplaats.  # noqa: E501

        :param naam: The naam of this WoonplaatsHal.  # noqa: E501
        :type: str
        """

        self._naam = naam

    @property
    def status(self):
        """Gets the status of this WoonplaatsHal.  # noqa: E501


        :return: The status of this WoonplaatsHal.  # noqa: E501
        :rtype: StatusWoonplaatsEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WoonplaatsHal.


        :param status: The status of this WoonplaatsHal.  # noqa: E501
        :type: StatusWoonplaatsEnum
        """

        self._status = status

    @property
    def geconstateerd(self):
        """Gets the geconstateerd of this WoonplaatsHal.  # noqa: E501

        Indicator dat de woonplaats in de registratie is opgenomen door een feitelijke constatering, zonder dat er een brondocument aan ten grondslag ligt. De woonplaats is mogelijk illegaal.  # noqa: E501

        :return: The geconstateerd of this WoonplaatsHal.  # noqa: E501
        :rtype: bool
        """
        return self._geconstateerd

    @geconstateerd.setter
    def geconstateerd(self, geconstateerd):
        """Sets the geconstateerd of this WoonplaatsHal.

        Indicator dat de woonplaats in de registratie is opgenomen door een feitelijke constatering, zonder dat er een brondocument aan ten grondslag ligt. De woonplaats is mogelijk illegaal.  # noqa: E501

        :param geconstateerd: The geconstateerd of this WoonplaatsHal.  # noqa: E501
        :type: bool
        """

        self._geconstateerd = geconstateerd

    @property
    def documentdatum(self):
        """Gets the documentdatum of this WoonplaatsHal.  # noqa: E501

        De vaststellingsdatum van het brondocument dat de basis is voor opname, wijziging of een verwijdering van een object.  # noqa: E501

        :return: The documentdatum of this WoonplaatsHal.  # noqa: E501
        :rtype: date
        """
        return self._documentdatum

    @documentdatum.setter
    def documentdatum(self, documentdatum):
        """Sets the documentdatum of this WoonplaatsHal.

        De vaststellingsdatum van het brondocument dat de basis is voor opname, wijziging of een verwijdering van een object.  # noqa: E501

        :param documentdatum: The documentdatum of this WoonplaatsHal.  # noqa: E501
        :type: date
        """

        self._documentdatum = documentdatum

    @property
    def documentnummer(self):
        """Gets the documentnummer of this WoonplaatsHal.  # noqa: E501

        De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een woonplaats heeft plaatsgevonden, binnen een gemeente. Alle karakters uit de MES-1 karakterset zijn toegstaan.  # noqa: E501

        :return: The documentnummer of this WoonplaatsHal.  # noqa: E501
        :rtype: str
        """
        return self._documentnummer

    @documentnummer.setter
    def documentnummer(self, documentnummer):
        """Sets the documentnummer of this WoonplaatsHal.

        De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een woonplaats heeft plaatsgevonden, binnen een gemeente. Alle karakters uit de MES-1 karakterset zijn toegstaan.  # noqa: E501

        :param documentnummer: The documentnummer of this WoonplaatsHal.  # noqa: E501
        :type: str
        """

        self._documentnummer = documentnummer

    @property
    def mogelijk_onjuist(self):
        """Gets the mogelijk_onjuist of this WoonplaatsHal.  # noqa: E501


        :return: The mogelijk_onjuist of this WoonplaatsHal.  # noqa: E501
        :rtype: WoonplaatsMogelijkOnjuist
        """
        return self._mogelijk_onjuist

    @mogelijk_onjuist.setter
    def mogelijk_onjuist(self, mogelijk_onjuist):
        """Sets the mogelijk_onjuist of this WoonplaatsHal.


        :param mogelijk_onjuist: The mogelijk_onjuist of this WoonplaatsHal.  # noqa: E501
        :type: WoonplaatsMogelijkOnjuist
        """

        self._mogelijk_onjuist = mogelijk_onjuist

    @property
    def links(self):
        """Gets the links of this WoonplaatsHal.  # noqa: E501


        :return: The links of this WoonplaatsHal.  # noqa: E501
        :rtype: WoonplaatsLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this WoonplaatsHal.


        :param links: The links of this WoonplaatsHal.  # noqa: E501
        :type: WoonplaatsLinks
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this WoonplaatsHal.  # noqa: E501


        :return: The embedded of this WoonplaatsHal.  # noqa: E501
        :rtype: WoonplaatsEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this WoonplaatsHal.


        :param embedded: The embedded of this WoonplaatsHal.  # noqa: E501
        :type: WoonplaatsEmbedded
        """

        self._embedded = embedded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WoonplaatsHal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WoonplaatsHal):
            return True

        return self.to_dict() != other.to_dict()
