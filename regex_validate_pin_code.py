"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

def validate_pin(pin):
    validNums = "0123456789"
    validNumsList = list(validNums)
    pin = list(pin)
    valid = True
    if (len(pin) != 4) and (len(pin) != 6):
        valid = False
    else:
        for digit in pin:
            if digit not in validNumsList:
                valid = False
    return valid 
  
# another example

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
