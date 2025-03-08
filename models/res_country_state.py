# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright (c) 2024  - feddad.imad@gmail.com

from odoo import fields, models, api, _

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    city_ids = fields.One2many('res.city', 'state_id', 'Communes', readonly=False)

    code_country = fields.Char(related='country_id.code', store=True)
