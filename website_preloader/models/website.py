from email.policy import default
from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    enable_preloader = fields.Boolean("Website Preloader")

    theme_mode = fields.Selection([
        ('light', "Light Mode"),
        ('dark', "Dark Mode")
    ], string='Theme', help='Please select Theme.', required=True, default='light')
