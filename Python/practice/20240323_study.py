# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

cnt = 0
while principal > 0:
    if 61<= cnt <= 108:
        principal = principal * (1+rate/12) - (payment + 1000)
        total_paid = total_paid + payment + 1000
    else:
        principal = principal * (1+rate/12) - (payment)
        total_paid = total_paid + payment
        
    cnt += 1

    print('Total paid {:,}'.format(round(total_paid, 2)), cnt)