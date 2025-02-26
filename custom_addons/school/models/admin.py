from odoo import models, fields, api
class Admin(models.Model):
    _name = 'school.admin'
    _description = 'Admin'

    a_id = fields.Char(string="Admin ID", readonly=True)
    name = fields.Char(string="Name", required=True)
    doj = fields.Date(string="Date of Joining")
    des = fields.Char(string="Designation")
    gen=fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")

    @api.model
    def create(self, vals):
        if 'a_id' not in vals:
            vals['a_id'] = self.env['ir.sequence'].next_by_code('school.admin.sequence')
        return super(Admin, self).create(vals)

class StdModel(models.Model):
    _name = 'std.model'
    _description = 'Standard'
    _rec_name = 'sub_code'

    c_id = fields.Char(string="Faculty ID")
    sub_code = fields.Char(string="Subject Code")
    c_name = fields.Selection([('1', '9'), ('2', '10'), ('3', '11'), ('4', '12')], string="Class Name")
    c_sub = fields.Selection([
        ('1', 'Maths'), ('2', 'Science'), ('3', 'English'),
        ('4', 'Accounts'), ('5', 'Statistics'), ('6', 'Economics'),
        ('7', 'Chemistry'), ('8', 'Biology'), ('9', 'Physics')
    ], string="Subject")
