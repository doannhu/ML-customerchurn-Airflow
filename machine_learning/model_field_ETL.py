import re

#remove all non digit and dash in mobile phone
def rmv_non_digit_dashes(phone_numb):
    result = re.sub(r'[^0-9-]', '', phone_numb)
    return result