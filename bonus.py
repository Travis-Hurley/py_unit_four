def company_money(time,sallery):
    if time>=5:
        money=sallery+(sallery*0.05)
    if time<5:
        money=sallery*1
    return money

def main():
    time = int(input("How long have you worked here?>>"))
    sallery = int(input("What is your annual sallery?>>"))
    money=company_money(time,sallery)
    print("Your sallery is",money)
main()