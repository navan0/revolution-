def factorial(n):
   if n == 1 :
         return n
   else:
         return (n*factorial(n-1))
 num=int(input("enter number:"))
 print("Factorial:")
 print(factorial(n))