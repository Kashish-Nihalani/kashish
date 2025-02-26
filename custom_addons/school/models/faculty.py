from odoo import api,models, fields
from datetime import date
import logging
_logger = logging.getLogger("Custom logs:--> ")

class Faculty(models.Model):
    _name = 'school.faculty'
    _description = 'Faculty'

    f_id = fields.Char(string="Faculty ID", readonly=True)
    name = fields.Char(string="Name", required=True)
    doj = fields.Date(string="Date of Joining")
    sub = fields.Char(string="Subject")
    f_std= fields.One2many('std.model', 'c_id',string="Standard")
    @api.model
    def create(self, vals):
        _logger.info("Hello")
        if 'f_id' not in vals:
            vals['f_id'] = self.env['ir.sequence'].next_by_code('school.faculty.sequence')
        return super(Faculty, self).create(vals)
    @api.constrains('doj')
    def _check_doj(self):
        for record in self:
            if record.doj > date.today():
                raise models.ValidationError("The date of birth cannot be in the future!")
