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


class AdresHal(object):
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
        'straat': 'str',
        'huisnummer': 'int',
        'huisletter': 'str',
        'huisnummertoevoeging': 'str',
        'postcode': 'str',
        'woonplaats': 'str',
        'korte_naam': 'str',
        'nummeraanduiding_identificatie': 'str',
        'openbare_ruimte_identificatie': 'str',
        'woonplaats_identificatie': 'str',
        'adresseerbaar_object_identificatie': 'str',
        'pand_identificaties': 'list[str]',
        'is_nevenadres': 'bool',
        'geconstateerd': 'bool',
        'mogelijk_onjuist': 'AdresMogelijkOnjuist',
        'links': 'AdresLinks',
        'embedded': 'AdresEmbedded'
    }

    attribute_map = {
        'straat': 'straat',
        'huisnummer': 'huisnummer',
        'huisletter': 'huisletter',
        'huisnummertoevoeging': 'huisnummertoevoeging',
        'postcode': 'postcode',
        'woonplaats': 'woonplaats',
        'korte_naam': 'korteNaam',
        'nummeraanduiding_identificatie': 'nummeraanduidingIdentificatie',
        'openbare_ruimte_identificatie': 'openbareRuimteIdentificatie',
        'woonplaats_identificatie': 'woonplaatsIdentificatie',
        'adresseerbaar_object_identificatie': 'adresseerbaarObjectIdentificatie',
        'pand_identificaties': 'pandIdentificaties',
        'is_nevenadres': 'isNevenadres',
        'geconstateerd': 'geconstateerd',
        'mogelijk_onjuist': 'mogelijkOnjuist',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, straat=None, huisnummer=None, huisletter=None, huisnummertoevoeging=None, postcode=None, woonplaats=None, korte_naam=None, nummeraanduiding_identificatie=None, openbare_ruimte_identificatie=None, woonplaats_identificatie=None, adresseerbaar_object_identificatie=None, pand_identificaties=None, is_nevenadres=None, geconstateerd=None, mogelijk_onjuist=None, links=None, embedded=None, local_vars_configuration=None):  # noqa: E501
        """AdresHal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._straat = None
        self._huisnummer = None
        self._huisletter = None
        self._huisnummertoevoeging = None
        self._postcode = None
        self._woonplaats = None
        self._korte_naam = None
        self._nummeraanduiding_identificatie = None
        self._openbare_ruimte_identificatie = None
        self._woonplaats_identificatie = None
        self._adresseerbaar_object_identificatie = None
        self._pand_identificaties = None
        self._is_nevenadres = None
        self._geconstateerd = None
        self._mogelijk_onjuist = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if straat is not None:
            self.straat = straat
        if huisnummer is not None:
            self.huisnummer = huisnummer
        if huisletter is not None:
            self.huisletter = huisletter
        if huisnummertoevoeging is not None:
            self.huisnummertoevoeging = huisnummertoevoeging
        if postcode is not None:
            self.postcode = postcode
        if woonplaats is not None:
            self.woonplaats = woonplaats
        if korte_naam is not None:
            self.korte_naam = korte_naam
        if nummeraanduiding_identificatie is not None:
            self.nummeraanduiding_identificatie = nummeraanduiding_identificatie
        if openbare_ruimte_identificatie is not None:
            self.openbare_ruimte_identificatie = openbare_ruimte_identificatie
        if woonplaats_identificatie is not None:
            self.woonplaats_identificatie = woonplaats_identificatie
        if adresseerbaar_object_identificatie is not None:
            self.adresseerbaar_object_identificatie = adresseerbaar_object_identificatie
        if pand_identificaties is not None:
            self.pand_identificaties = pand_identificaties
        if is_nevenadres is not None:
            self.is_nevenadres = is_nevenadres
        if geconstateerd is not None:
            self.geconstateerd = geconstateerd
        if mogelijk_onjuist is not None:
            self.mogelijk_onjuist = mogelijk_onjuist
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def straat(self):
        """Gets the straat of this AdresHal.  # noqa: E501

        Een naam die door de gemeente aan een openbare ruimte is gegeven.  # noqa: E501

        :return: The straat of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._straat

    @straat.setter
    def straat(self, straat):
        """Sets the straat of this AdresHal.

        Een naam die door de gemeente aan een openbare ruimte is gegeven.  # noqa: E501

        :param straat: The straat of this AdresHal.  # noqa: E501
        :type: str
        """

        self._straat = straat

    @property
    def huisnummer(self):
        """Gets the huisnummer of this AdresHal.  # noqa: E501

        Een nummer dat door de gemeente aan een adresseerbaar object is gegeven.  # noqa: E501

        :return: The huisnummer of this AdresHal.  # noqa: E501
        :rtype: int
        """
        return self._huisnummer

    @huisnummer.setter
    def huisnummer(self, huisnummer):
        """Sets the huisnummer of this AdresHal.

        Een nummer dat door de gemeente aan een adresseerbaar object is gegeven.  # noqa: E501

        :param huisnummer: The huisnummer of this AdresHal.  # noqa: E501
        :type: int
        """

        self._huisnummer = huisnummer

    @property
    def huisletter(self):
        """Gets the huisletter of this AdresHal.  # noqa: E501

        Een toevoeging aan een huisnummer in de vorm van een letter die door de gemeente aan een adresseerbaar object is gegeven.  # noqa: E501

        :return: The huisletter of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._huisletter

    @huisletter.setter
    def huisletter(self, huisletter):
        """Sets the huisletter of this AdresHal.

        Een toevoeging aan een huisnummer in de vorm van een letter die door de gemeente aan een adresseerbaar object is gegeven.  # noqa: E501

        :param huisletter: The huisletter of this AdresHal.  # noqa: E501
        :type: str
        """

        self._huisletter = huisletter

    @property
    def huisnummertoevoeging(self):
        """Gets the huisnummertoevoeging of this AdresHal.  # noqa: E501

        Een toevoeging aan een huisnummer of een combinatie van huisnummer en huisletter die door de gemeente aan een adresseerbaar object is gegeven.  # noqa: E501

        :return: The huisnummertoevoeging of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._huisnummertoevoeging

    @huisnummertoevoeging.setter
    def huisnummertoevoeging(self, huisnummertoevoeging):
        """Sets the huisnummertoevoeging of this AdresHal.

        Een toevoeging aan een huisnummer of een combinatie van huisnummer en huisletter die door de gemeente aan een adresseerbaar object is gegeven.  # noqa: E501

        :param huisnummertoevoeging: The huisnummertoevoeging of this AdresHal.  # noqa: E501
        :type: str
        """

        self._huisnummertoevoeging = huisnummertoevoeging

    @property
    def postcode(self):
        """Gets the postcode of this AdresHal.  # noqa: E501

        De door PostNL vastgestelde code die bij een bepaalde combinatie van een straatnaam en een huisnummer hoort.  # noqa: E501

        :return: The postcode of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this AdresHal.

        De door PostNL vastgestelde code die bij een bepaalde combinatie van een straatnaam en een huisnummer hoort.  # noqa: E501

        :param postcode: The postcode of this AdresHal.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def woonplaats(self):
        """Gets the woonplaats of this AdresHal.  # noqa: E501

        Een woonplaats is een gedeelte van het grondgebied van de gemeente met een naam.  # noqa: E501

        :return: The woonplaats of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._woonplaats

    @woonplaats.setter
    def woonplaats(self, woonplaats):
        """Sets the woonplaats of this AdresHal.

        Een woonplaats is een gedeelte van het grondgebied van de gemeente met een naam.  # noqa: E501

        :param woonplaats: The woonplaats of this AdresHal.  # noqa: E501
        :type: str
        """

        self._woonplaats = woonplaats

    @property
    def korte_naam(self):
        """Gets the korte_naam of this AdresHal.  # noqa: E501

        De officiële openbareruimtenaam of een verkorte versie. Beiden hebben maximaal 24 tekens.  # noqa: E501

        :return: The korte_naam of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._korte_naam

    @korte_naam.setter
    def korte_naam(self, korte_naam):
        """Sets the korte_naam of this AdresHal.

        De officiële openbareruimtenaam of een verkorte versie. Beiden hebben maximaal 24 tekens.  # noqa: E501

        :param korte_naam: The korte_naam of this AdresHal.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                korte_naam is not None and len(korte_naam) > 24):
            raise ValueError("Invalid value for `korte_naam`, length must be less than or equal to `24`")  # noqa: E501

        self._korte_naam = korte_naam

    @property
    def nummeraanduiding_identificatie(self):
        """Gets the nummeraanduiding_identificatie of this AdresHal.  # noqa: E501

        Fungeert ook als identificatie van het adres.  # noqa: E501

        :return: The nummeraanduiding_identificatie of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._nummeraanduiding_identificatie

    @nummeraanduiding_identificatie.setter
    def nummeraanduiding_identificatie(self, nummeraanduiding_identificatie):
        """Sets the nummeraanduiding_identificatie of this AdresHal.

        Fungeert ook als identificatie van het adres.  # noqa: E501

        :param nummeraanduiding_identificatie: The nummeraanduiding_identificatie of this AdresHal.  # noqa: E501
        :type: str
        """

        self._nummeraanduiding_identificatie = nummeraanduiding_identificatie

    @property
    def openbare_ruimte_identificatie(self):
        """Gets the openbare_ruimte_identificatie of this AdresHal.  # noqa: E501


        :return: The openbare_ruimte_identificatie of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._openbare_ruimte_identificatie

    @openbare_ruimte_identificatie.setter
    def openbare_ruimte_identificatie(self, openbare_ruimte_identificatie):
        """Sets the openbare_ruimte_identificatie of this AdresHal.


        :param openbare_ruimte_identificatie: The openbare_ruimte_identificatie of this AdresHal.  # noqa: E501
        :type: str
        """

        self._openbare_ruimte_identificatie = openbare_ruimte_identificatie

    @property
    def woonplaats_identificatie(self):
        """Gets the woonplaats_identificatie of this AdresHal.  # noqa: E501


        :return: The woonplaats_identificatie of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._woonplaats_identificatie

    @woonplaats_identificatie.setter
    def woonplaats_identificatie(self, woonplaats_identificatie):
        """Sets the woonplaats_identificatie of this AdresHal.


        :param woonplaats_identificatie: The woonplaats_identificatie of this AdresHal.  # noqa: E501
        :type: str
        """

        self._woonplaats_identificatie = woonplaats_identificatie

    @property
    def adresseerbaar_object_identificatie(self):
        """Gets the adresseerbaar_object_identificatie of this AdresHal.  # noqa: E501


        :return: The adresseerbaar_object_identificatie of this AdresHal.  # noqa: E501
        :rtype: str
        """
        return self._adresseerbaar_object_identificatie

    @adresseerbaar_object_identificatie.setter
    def adresseerbaar_object_identificatie(self, adresseerbaar_object_identificatie):
        """Sets the adresseerbaar_object_identificatie of this AdresHal.


        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this AdresHal.  # noqa: E501
        :type: str
        """

        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie

    @property
    def pand_identificaties(self):
        """Gets the pand_identificaties of this AdresHal.  # noqa: E501

        Identificatie(s) van het pand of de panden waar het verblijfsobject deel van is.  # noqa: E501

        :return: The pand_identificaties of this AdresHal.  # noqa: E501
        :rtype: list[str]
        """
        return self._pand_identificaties

    @pand_identificaties.setter
    def pand_identificaties(self, pand_identificaties):
        """Sets the pand_identificaties of this AdresHal.

        Identificatie(s) van het pand of de panden waar het verblijfsobject deel van is.  # noqa: E501

        :param pand_identificaties: The pand_identificaties of this AdresHal.  # noqa: E501
        :type: list[str]
        """

        self._pand_identificaties = pand_identificaties

    @property
    def is_nevenadres(self):
        """Gets the is_nevenadres of this AdresHal.  # noqa: E501

        Indicatie dat dit adres een nevenadres is van een adresseerbaar object. Het adres is een hoofdadres als deze indicatie niet wordt meegeleverd.  # noqa: E501

        :return: The is_nevenadres of this AdresHal.  # noqa: E501
        :rtype: bool
        """
        return self._is_nevenadres

    @is_nevenadres.setter
    def is_nevenadres(self, is_nevenadres):
        """Sets the is_nevenadres of this AdresHal.

        Indicatie dat dit adres een nevenadres is van een adresseerbaar object. Het adres is een hoofdadres als deze indicatie niet wordt meegeleverd.  # noqa: E501

        :param is_nevenadres: The is_nevenadres of this AdresHal.  # noqa: E501
        :type: bool
        """

        self._is_nevenadres = is_nevenadres

    @property
    def geconstateerd(self):
        """Gets the geconstateerd of this AdresHal.  # noqa: E501

        Indicatie dat dit adres in de registratie is opgenomen door een feitelijke constatering, zonder dat er sprake was van een brondocument/vergunning. Het adres is mogelijk illegaal.  # noqa: E501

        :return: The geconstateerd of this AdresHal.  # noqa: E501
        :rtype: bool
        """
        return self._geconstateerd

    @geconstateerd.setter
    def geconstateerd(self, geconstateerd):
        """Sets the geconstateerd of this AdresHal.

        Indicatie dat dit adres in de registratie is opgenomen door een feitelijke constatering, zonder dat er sprake was van een brondocument/vergunning. Het adres is mogelijk illegaal.  # noqa: E501

        :param geconstateerd: The geconstateerd of this AdresHal.  # noqa: E501
        :type: bool
        """

        self._geconstateerd = geconstateerd

    @property
    def mogelijk_onjuist(self):
        """Gets the mogelijk_onjuist of this AdresHal.  # noqa: E501


        :return: The mogelijk_onjuist of this AdresHal.  # noqa: E501
        :rtype: AdresMogelijkOnjuist
        """
        return self._mogelijk_onjuist

    @mogelijk_onjuist.setter
    def mogelijk_onjuist(self, mogelijk_onjuist):
        """Sets the mogelijk_onjuist of this AdresHal.


        :param mogelijk_onjuist: The mogelijk_onjuist of this AdresHal.  # noqa: E501
        :type: AdresMogelijkOnjuist
        """

        self._mogelijk_onjuist = mogelijk_onjuist

    @property
    def links(self):
        """Gets the links of this AdresHal.  # noqa: E501


        :return: The links of this AdresHal.  # noqa: E501
        :rtype: AdresLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AdresHal.


        :param links: The links of this AdresHal.  # noqa: E501
        :type: AdresLinks
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this AdresHal.  # noqa: E501


        :return: The embedded of this AdresHal.  # noqa: E501
        :rtype: AdresEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this AdresHal.


        :param embedded: The embedded of this AdresHal.  # noqa: E501
        :type: AdresEmbedded
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
        if not isinstance(other, AdresHal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdresHal):
            return True

        return self.to_dict() != other.to_dict()
