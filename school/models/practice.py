from odoo import models, fields

class Practice(models.Model):
    _name = 'practice'
    _description = 'Practice'

    roll = fields.Integer(string="Roll Number")
    name = fields.Char(string="Name")
    eng = fields.Integer(string="English")
    math = fields.Integer(string="Mathematics")
    sci = fields.Integer(string="Science")
    #country_id =fields.many2one(res.country , string= "Country")