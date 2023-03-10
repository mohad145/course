from odoo import api, fields, models,_
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit=['mail.thread','mail.activity.mixin']
    _rec_name='name'

    name = fields.Char(string='Name',tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    ref = fields.Char(string='Reference',default='apple')
    active = fields.Boolean(string='Active',default=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ],string= 'Gender',default='female',tracking=True)
    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today=date.today()
            print("date.today()" , date.today())
            if rec.date_of_birth:
                print("today.year",today.year)
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

