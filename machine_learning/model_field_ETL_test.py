from model_field_ETL import rmv_non_digit_dashes
import unittest

class ModelFieldETLTest(unittest.TestCase):
    def remove_char_test(self):
        phone_number = "abc766-3455"
        phone_number_rmv_char = "766-3455"
        self.assertEquals(phone_number_rmv_char,rmv_non_digit_dashes(phone_number))