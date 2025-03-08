# Part of Odoo. See LICENSE file for full copyright and licensing details.

import contextlib
import logging
import requests
from lxml import etree
from markupsafe import Markup
from hashlib import md5
from urllib import parse
from collections import defaultdict

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

ADDRESS_FIELDS = ('street', 'city', 'state_id', 'country_id')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _address_fields(self):
        """Returns the list of address fields that are synced from the parent."""
        return list(ADDRESS_FIELDS)

    def _prepare_display_address(self, without_company=False):
        # get the information that will be injected into the display format
        # get the address format
        address_format = self._get_address_format()
        print('11-------------', address_format)
        print('11-------------', self.street)
        args = defaultdict(str, {
            'street': self.street,
            'city': self.city_id.name,
            'state_code': self.state_id.code or '',
            'state_name': self.state_id.name or '',
            'country_code': self.country_id.code or '',
            'country_name': self._get_country_name(),
            'company_name': self.commercial_company_name or '',
        })
        print('args------------', args)
        for field in self._formatting_address_fields():
            print('args[field]-------------', args[field])
            print('self[field]-------------', self[field])
            args[field] = self[field] or ''
        if without_company:
            args['company_name'] = ''
        elif self.commercial_company_name:
            address_format = '%(company_name)s\n' + address_format

        print('address_format------------', address_format)
        print('args------------', args)
        return address_format, args