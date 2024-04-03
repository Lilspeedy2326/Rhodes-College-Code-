def milekilo(x):
    convertrate = 1.60934
    print (x * convertrate)
    
    
    
print("Do you want to enter distance as miles or kilometer? (type m or k): ")
choice=input()
print("how many miles do you want to go?")
distance = float(input())

if choice == 'm' or choice == 'M':
    print("converted to km:", distance*1.6)
    
if choice == 'k' or choice == 'K':
    print ("converted to km", distance*0.6)
           
if choice == 'm' or choice == 'M':
    time = distance/15
    print(time*60)
    
if choice == 'k' or choice == 'K':
    time = distance/15
    print(time*60)
    
A= 1+.15*time
if time<=5:
    B = 2.5*time
else:
    B = 2.5*5 + .12*time
C = 5+.06*time

if A<B and A<C:
    print("use company A")
elif B<A and B<C:
    print("use company B")
elif C<B and C<A:
    print("use company C")
