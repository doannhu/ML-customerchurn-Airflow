from typing import Any
from django.test import TestCase
from .models import CustomerChurn
# Create your tests here.

class CustomerChurnTestCase(TestCase):
    def setUp(self) -> None:
        self.obj = CustomerChurn.objects.create(
            state= "AZ",
            account_length=90,
            area_code=415,
            phone_number="387-6103",
            international_plan= "no",
            voice_mail_plan= "no",
            number_vmail_messages= 0,
            total_day_minutes= 179.1,
            total_day_calls=71,
            total_day_charge=30.45,
            total_eve_minutes=190.6,
            total_eve_calls=81,
            total_eve_charge=16.2,
            total_night_minutes=127.7,
            total_night_calls=91,
            total_night_charge=5.75,
            total_intl_minutes=10.6,
            total_intl_calls=7,
            total_intl_charge=2.86,
            customer_service_calls=3,
            churn=False
        )

    def test_model_fields(self):
        self.assertEqual(self.obj.state,"AZ")
        self.assertEqual(self.obj.account_length,90)
        self.assertEqual(self.obj.area_code,415)
        self.assertEqual(self.obj.phone_number,"387-6103")
        self.assertEqual(self.obj.international_plan,"no")
        self.assertEqual(self.obj.voice_mail_plan,"no")
        self.assertEqual(self.obj.number_vmail_messages,0)
        self.assertEqual(self.obj.total_day_minutes,179.1)
        self.assertEqual(self.obj.total_day_calls,71)
        self.assertEqual(self.obj.total_day_charge,30.45)
        self.assertEqual(self.obj.total_eve_minutes,190.6)
        self.assertEqual(self.obj.total_eve_calls,81)
        self.assertEqual(self.obj.total_eve_charge,16.2)
        self.assertEqual(self.obj.total_night_minutes,127.7)
        self.assertEqual(self.obj.total_night_calls,91)
        self.assertEqual(self.obj.total_night_charge,5.75)
        self.assertEqual(self.obj.total_intl_minutes,10.6)
        self.assertEqual(self.obj.total_intl_calls,7)
        self.assertEqual(self.obj.total_intl_charge,2.86)
        self.assertEqual(self.obj.customer_service_calls,3)
        self.assertEqual(self.obj.churn,False)
        
# To test, run docker compose up. Go to django container in docker desktop.
# Open terminal in container. Run python manage.py test