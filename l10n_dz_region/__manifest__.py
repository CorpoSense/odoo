# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018-Osis (<http://www.osis.dz/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

{
    'name': 'Algeria - Regions',
    'version': '11.0.1.0.0',
    'description': """Adds extra functionality and configuration to Odoo """,
    'summary': 'Regions of Algeria',
    'author': 'version 10.0 d\'Osis, modifié par Ludovic Dessemon, CorpoSense pour Odoo 11.0',
    'website': '',
    'license': 'AGPL-3',
    'category': 'Sales',
    'depends': [
        'sale',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',
        'data/wilaya.xml',
        'data/commune.xml',
	    'views/res_commune.xml'
    ]
}
