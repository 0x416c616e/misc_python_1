#!/usr/bin/env python3
'''
Assume that price is an integer variable whose value is the price 
(in US currency) in cents of an item. Write a statement that prints
the value of price in the form "X dollars and Y cents" on a line by 
itself. So, if the value of price was 4321, your code would print 
"43 dollars and 21 cents". If the value was 501 it would print 
"5 dollars and 1 cents". If the value was 99 your code would print 
"0 dollars 99 cents".


This was the original Java code I wrote back in the day, now I'm converting it to python: 
public class REVELcost {
    public static void main(String[] args) {
        int price;
        price = 4321;
        System.out.printf("%d dollars and %d cents", price / 100, price % 100);
        
    }
}
'''

numberOfPennies = int(input("How many pennies do you have? "))
priceDollars = numberOfPennies // 100 #floor division
priceCents = numberOfPennies % 100 #modulus
print("you have {0} dollars and {1} cents in pennies.".format(priceDollars, priceCents))