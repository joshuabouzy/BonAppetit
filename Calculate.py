def bonAppetit(bill, k, b):
    actual = (sum(bill) - bill[k])/2
    if actual == b:
        print("Bon Appetit")
    else:
        print(int(b - actual))
