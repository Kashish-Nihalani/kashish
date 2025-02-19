from odoo import api,fields,models
import logging
_logger = logging.getLogger("Appointments:--> ")
class CreateAppointment(models.TransientModel):
    _name = "create.appointment"
    _description = "Create Appointment"
    roll=fields.Many2one('school.student',string="Roll number")
    app_date=fields.Date(string="Date")
    @api.model
    def create_appointment(self,vals):
        _logger.info("Successfully created appointment.")