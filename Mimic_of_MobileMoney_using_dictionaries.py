def momo_prompt():
    print('welcome to MTN MobileMoney Services\nplease select an option:')
    for key,value in get_option().items():
        print (f'{key}. {value}')
    USSD = input("please select an option:\n")
    user_value = display_option_for_user(USSD)
    return user_value
    
def get_option():
    momo_prompt = {
        "1" : "Transfer Money",
        "2" : "MomoPay and Bills",
        "3" : "Airtime and Data Bundles",
        "4" : "Allow CashOut",
        "5" : "Financial Services",
        "6" : "My Wallet"
    }
    return momo_prompt

def display_option_for_user(USSD):
    option = get_option()
    if USSD in  option.keys():
        return option[USSD]
    else:
        return (f"invalid option")
    
user_option = momo_prompt()
print(user_option)
    
    
