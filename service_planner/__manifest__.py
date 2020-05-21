# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name":     "Vertical NGO - Service Plan",
    "summary":  "Management of service planning.",
    "version":  "12.0.1.0.0",

    "author":   "Associazione PNLUG - Gruppo Odoo, Odoo Community Association (OCA)",
    "website":  "https://gitlab.com/PNLUG/",
    "license":  "AGPL-3",

    "category": "Logistics",

    "depends": [
        'fleet',
        'maintenance',
        'hr',
        'product',
        # OCA modules
        'web_timeline',
        'web_widget_color',
        'hr_skill',
        ],
    "data": [
        'data/data_service_rule.xml',
        'security/ir.model.access.csv',
        'wizards/service_generate.xml',
        'views/service_menu.xml',
        'views/service_allocate_view.xml',
        'views/service_rule_view.xml',
        'views/service_collector_view.xml',
        'views/service_container_view.xml',
        'views/service_expected_view.xml',
        'views/service_template_view.xml',
        'views/fleet_vehicle_views.xml',
        'views/employee_views.xml',
        ],
    "css": [
        'static/src/css/service_planner.css',
        ],
    'installable': True,
}
