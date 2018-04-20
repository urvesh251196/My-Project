import Flipkart
##import snapdeal
##import Paytm
##import Amazon
##import Myntra
##import aliexpress

##list=['']

product=raw_input("Enter product name : ")
decision=raw_input("If you want to find by price then press Y else press N")
if(decision == 'Y'):
    budget=input("Enter your budget : ")
    Flipkart.flipkart(product,budget)
else:
    discount=input("Enter your discount : ")
    Flipkart.flipkart(product,discount)


##snapdeal.snapdeal(product,budget)
##Amazon.amazon(product,budget)
##Paytm.logic(10)
#Myntra.logic(1)
##aliexpress.aliexpress(product,budget)
