from odoo import api, fields, models,_

class Hospitalappointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital appointment"
    _inherit=['mail.thread','mail.activity.mixin']
    _rec_name='patient_id'

    patient_id = fields.Many2one('hospital.patient',string='Patient')
    doctor_id = fields.Many2one('res.users',string='Doctor')
    ref = fields.Char(string='Reference')
    appointment_time = fields.Datetime(string='Appointment Time',default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    gender = fields.Selection(related='patient_id.gender',)
    appointment_count = fields.Integer(string='Appointment Count',compute='_compute_appointment_count')
    appointment_id = fields.Many2one('hospital.appointment',string='Appointment')
    presecription = fields.Html(string='Presecription')
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', index=True, default='draft', requried=True,tracking=True)
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref='11111'
        # self.ref=self.patient_id.ref
    def _compute_appointment_count(self):
        self.appointment_count=5


    def action_test(self):
        print('111111')

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'message successfull',
                'type': 'rainbow_man',
            }
        }


