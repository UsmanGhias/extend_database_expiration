from odoo import models, fields


class IrConfigParameterInherit(models.Model):
    _inherit = 'ir.config_parameter'

    def extend_database_expiration_date(self):
        expiry_param_id = self.env['ir.config_parameter'].sudo().search([('key', '=', 'database.expiration_date')])
        current_month = fields.Datetime().now().month
        new_expiry_date = fields.Datetime().now().replace(month=current_month + 1)
        time_string = new_expiry_date.strftime('%Y-%m-%d %H:%M:%S')

        if expiry_param_id:
            expiry_param_id.sudo().write({'value': time_string})
        else:
            database_expiry_params = {
                'key': 'database.expiration_date',
                'value': time_string,
            }
            self.env['ir.config_parameter'].sudo().create(database_expiry_params)
