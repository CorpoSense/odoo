from odoo.tests import common
# https://www.odoo.com/documentation/11.0/reference/testing.html
from datetime import datetime

# The transaction is rolled back and the cursor is closed after each test
class TestAppointment(common.TransactionCase):

    def setUp(self):
        super(TestAppointment, self).setUp()
        self.HrEmployee = self.env['hr.employee']
    
    def test_create_employee(self):
        """Running Employee test..."""
        
        e1 = self.HrEmployee.create({
            'name':'Amine KARA',
            'first_name':'Amine',
            'matricule':'a34',
            'housewife':False
        })
        
        self.assertEqual(e1.first_name, 'Amine')
