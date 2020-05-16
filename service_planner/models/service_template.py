# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ServiceTemplate(models.Model):
    """
    Model of a service with definition of the required components
    """

    # model
    _name = 'service.template'
    _description = 'Model of a service'

    # fields
    # name
    name = fields.Char('Name', required=True)
    # container service reference
    service_container_ids = fields.Many2many('service.container',
                                             string='Container service')

    # standard duration
    duration = fields.Integer('Duration', required=True, default=1)
    # duration uom
    duration_uom_id = fields.Many2one('uom.uom',
                                      string='Unit of Measure')

    # expected vehicles
    exp_vehicle_ids = fields.Many2many('expected.vhcl_type',
                                       string='Vehicles')
    # expected skills
    exp_skill_ids = fields.Many2many('expected.skill',
                                     string='Operator Skills')
    # expected equipment category
    exp_eqp_cat_ids = fields.Many2many('expected.eqpmnt_cat',
                                       string='Equipment Category')

    # product reference used to valorize
    product_id = fields.Many2one('product.product',
                                 string='Product reference')

    # identification color
    base_color = fields.Char('Color')
