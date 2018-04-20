import Flipkart
import snapdeal
import Paytm
#import Amazon
##import Myntra
##import aliexpress


product=input("Enter product name : ")
decision=input("If you want to find by price then press Y else press N")
if(decision == 'Y'):
    budget=input("Enter your budget : ")
    #Flipkart.flipkart(product,budget)
    #Amazon.amazon(product,budget)
    #snapdeal.snapdeal(product, budget)

else:
    discount=int(input("Enter your discount : "))
    #Flipkart.flipkart(product,discount)
    #Amazon.amazon(product, discount)
    #snapdeal.snapdeal(product, discount)
    Paytm.logic(product, 10, discount)

##snapdeal.snapdeal(product,budget)
##Amazon.amazon(product,budget)
##Paytm.logic(10)
#Myntra.logic(1)
##aliexpress.aliexpress(product,budget)
