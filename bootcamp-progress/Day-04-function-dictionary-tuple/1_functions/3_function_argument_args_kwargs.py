#######    *args means normal arguments    ######
def sum_all(*args):
    total = 0

    print("args = ",args)
    for arg in args:
        total += arg
    return total

sum_tuple = sum_all(2,4848,2772,36,39,399,38)
print("Sum of the numbers in tuple: ",sum_tuple)

########     **kwargs means keyword arguments   #########
#####################   efficient method  #######################################
def company_credential(**kwargs):
    print("######  Company Credential Information  ###########")
    print("kwargs = ",kwargs)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

def company_info(**kwargs):
    print("###  COMPANY INFO ###")
    print("kwargs = ", kwargs)
    for item in kwargs.items():
        print(f"{item}: ")

def company_keys(**kwargs):
    print("##### keys  #######")
    print("kwargs = ", kwargs)
    for i in kwargs.keys():
        print(f"{i}")

def company_values(**kwargs):
    print("##### Company Values ########")
    print("kwargs = ", kwargs)
    for i in kwargs.values():
        print(f"{i}")

company_info(ticker = "AAPL", CEO = "Tim Cock", revenue = "200 billion", pe = 20, pb = 10.2)
company_credential(ticker = "AAPL", CEO = "Tim Cock", revenue = "200 billion", pe = 20, pb = 10.2)
company_keys(ticker = "AAPL", CEO = "Tim Cock", revenue = "200 billion", pe = 20, pb = 10.2)
company_values(ticker = "AAPL", CEO = "Tim Cock", revenue = "200 billion", pe = 20, pb = 10.2)

# def company_info(**kwargs):
#     if 'ticker' in kwargs:
#         print("Ticker: ", kwargs['ticker'])
#     if "CEO" in kwargs:
#         print("CEO: ", kwargs['CEO'])
#     if "revenue" in kwargs:
#         print("Revenue: ", kwargs['revenue'])

# kwargs = {
#     "ticker": "AAPL",
#     "CEO": "Tim Cook",
#     "revenue": "200 billion",
#     "pe": 20
# }

#####################  another method   #####################
# def company_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# company_info(ticker="AAPL", CEO="Tim Cook", revenue="200 billion", pe=20)





