def calculatePay():
    
    # This first line is provided for you
    rte = input("Enter Rate: ")
    hrs = input("Enter Hours: ")
    fhrs = float(hrs)
    frte = float(rte)
    if fhrs > 40 :
        reg = frte * fhrs
        otp = (fhrs - 40.0) * (frte * 0.5)
        pay = reg + otp 
    else:
        pay = fhrs * frte
    print("Pay:",pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()