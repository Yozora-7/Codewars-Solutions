"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
"""

from datetime import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    	date1 = current_date
    	date2 = expiration_date
    	d1 = datetime.strptime(date1, "%B %d, %Y")
    	d2 = datetime.strptime(date2, "%B %d, %Y")

    	if entered_code is correct_code and d1 <= d2: # cannot use the == operator because python will automatically think that a 0 is equal to False
        		return True
    	else:
      		return False
        
# another example

import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return(datetime.datetime.strptime(current_date,'%B %d, %Y') <= datetime.datetime.strptime(expiration_date,'%B %d, %Y'))
    return False
        
