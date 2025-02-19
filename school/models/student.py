from odoo import api, models, fields
from datetime import date

class Student(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _rec_name = 'roll'

    roll = fields.Char(string="Roll Numbers")
    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    std = fields.Integer(string="Standard")
    stu_count = fields.Integer(string="Student Count", compute='_compute_stu_count')
    dob = fields.Date(string="Date of Birth")

    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                today = fields.Date.today()
                record.age = today.year - record.dob.year - (
                            (today.month, today.day) < (record.dob.month, record.dob.day))
            else:
                record.age = 0


    def _compute_stu_count(self):
        for record in self:
            record.stu_count = self.env['school.student.result'].search_count([('roll', '=', record.id)])

    def action_show_result(self):
        tree_view_id = self.env.ref('school.view_result_tree').id
        form_view_id = self.env.ref('school.view_result_form').id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Result',
            'res_model': 'student.result',
            'view_mode': 'tree,form',
            'views': [(tree_view_id, 'tree'), (form_view_id, 'form')],
            'target': 'current',
            'context': {'default_roll': self.id},
            'domain': [('roll', '=', self.id)],
        }

    @api.model
    def create(self, vals):
        if 'roll' not in vals:
            vals['roll'] = self.env['ir.sequence'].next_by_code('school.student.sequence')
        return super(Student, self).create(vals)

    @api.constrains('dob')
    def _check_dob(self):
        for record in self:
            if record.dob > date.today():
                raise models.ValidationError("The date of birth cannot be in the future!")
