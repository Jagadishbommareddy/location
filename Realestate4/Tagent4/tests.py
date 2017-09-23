from django.test import TestCase
from django.test import TestCase
from django.test import Client
from .forms import *
class Setup_Class(TestCase):
    def setUp(self):
        self.propertytype = PropertyType.objects.create(description='buying the lands')
class PropertyType_Form_Test(TestCase):
    def test_PropertyTypeForm_valid(self):
        form = PropertyTypeForm(data={'description':'buying the lands'})
        self.assertTrue(form.is_valid())
    def test_CustomerForm_invalid(self):
        form = PropertyTypeForm(data={'description':''})
        self.assertFalse(form.is_valid())
class Agent_Form_Test(TestCase):
    def setUp(self):
        self.agent = Agent.objects.create(propertytype="self.PropertyType",first_name="user", last_name="customer", age='22', mobile_number=9990002221,phone_number=8885556666, email_id="user@mp.com", education='btech',
                                          company_name='tagontech', specialization='buying lands', experience='5 years', agent_notes='bfdbf jjdsfndmznfd',property_type='self.PropertyType',media_name='uploading images',media_path='documents/')
        def test_AgentForm_valid(self):
            form = AgentForm(data={'propertytype':"self.PropertyType",'first_name':"user", 'last_name':"customer", 'age':'22', 'mobile_number':9990002221,'phone_number':8885556666, 'email_id':"user@mp.com", 'education':'btech',
                                   'company_name':'tagontech', 'specialization':'buyinglands', 'experience':'5 years', 'agent_notes':'bfdbf jjdsfndmznfd', 'property_type':'self.PropertyType', 'media_name':'uploading images','media_path':'documents/'})
            self.assertTrue(form.is_valid())
        def test_AgentForm_invalid(self):
            form = AgentForm(data={'propertytype':"",'first_name': "user#$1", 'last_name': "customer4_", 'age': '', 'mobile_number': '959%343423','phone_number': '7789$98787', 'email_id': "", 'education': 'degree 3rd year',
                        'company_name': '', 'specialization': 'buying lands', 'experience': '','agent_notes': '', 'property_type': '','media_name': 'uploading images','media_path':''})
            self.assertFalse(form.is_valid())
class Location_Form_Test(TestCase):
    def setUp(self):
        self.location = Location.objects.create(agent='self.Agent',city='secunderabad',state='telangana')
        def test_LocationForm_valid(self):
            form = LocationForm(data={'agent':'self.Agent','city':'secunderabad','state':'telangana'})
            self.assertTrue(form.is_valid())
        def test_LocationForm_invalid(self):
            form = LocationForm(data={'agent':'','city':'secun 7bad','state':'telan gana$'})
            self.assertFalse(form.is_valid())
class Address_Form_Test(TestCase):
    def setUp(self):
        self.address = Address.objects.create(agent='self.Agent',address1='ial colony',address2='begumpet',city='secunderabad',state='telangana',landmark='SecondLane',pincode='522001')
        def test_LocationForm_valid(self):
            form = AddressForm(data={'agent':'self.Agent','address1':'ial colony','address2':'begumpet','city':'secunderabad','state':'telangana','landmark':'SecondLane','pincode':'522001'})
            self.assertTrue(form.is_valid())
        def test_AddressForm_invalid(self):
            form = AddressForm(data={'agent':'','address1':'','address2':'','city':'secun 7bad','state':'telan gana$','landmark':'Second 1%Lane','pincode':'522001'})
            self.assertFalse(form.is_valid())
class AgentReferal_Form_Test(TestCase):
    def setUp(self):
        self.agentreferal = AgentReferal.objects.create(agent='self.Agent',name='user')
        def test_AgentReferalForm_valid(self):
            form = AgentReferalForm(data={'agent':'self.Agent','name':'user'})
            self.assertTrue(form.is_valid())
        def test_AgentReferalForm_invalid(self):
            form = AgentReferalForm(data={'agent':'','name':'use1$'})
            self.assertFalse(form.is_valid())