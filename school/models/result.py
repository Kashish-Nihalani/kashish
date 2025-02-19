from odoo import api, fields, models

class StudentResult(models.Model):
    _name = 'school.student.result'
    _description = 'School Student Result'
    _rec_name = 'roll'

    roll = fields.Many2one('school.student', string="Student", required=True)
    name = fields.Char(string="name")
    sub = fields.Many2one('std.model', string="Subject")
    marks = fields.Float(string="Marks", required=True)
    grade = fields.Char( compute='_compute_grade', string="Grade")


    def _compute_grade(self):
        for rec in self:
            if rec.marks >= 90:
                rec.grade = "A"
            elif rec.marks >= 80:
                rec.grade = "B"
            elif rec.marks >= 70:
                rec.grade = "C"
            elif rec.marks >= 60:
                rec.grade = "D"
            else:
                rec.grade = "F"