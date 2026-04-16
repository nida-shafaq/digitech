print(" Please Enter 10 numbers")
arr=[]
for i in range(10):
    num=int(input(f"Enter {i+1} number="))
    arr.append(num)
print(arr)
def find_odd(arr):
    odd_arr=[]
    for i in range(len(arr)):
        if arr[i]%2!=0:
            odd_arr.append(arr[i])
       
    return odd_arr

def find_even(arr):
    even_arr=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            even_arr.append(arr[i])
    return even_arr

def find_prime(arr):
    prime_arr = []
    
    for i in range(len(arr)):
        n = arr[i]
        
        if n <= 1:
            continue
        
        is_prime = True   # assume prime
        
        for j in range(2, n):
            if n % j == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_arr.append(n)
    
    return prime_arr
odd=find_odd(arr)
even=find_even(arr)
prime=find_prime(arr)
if len(odd)>=1:
    print("Odd numbers are :")
    print(odd,end=" ")
else:
    print("There is no odd numbers exsist")

if len(even)>=1:
    print("\n")
    print("Even numbers are:")
    print(even,end=" ")
else:
    print("There is no even numbers exsist")

if len(prime)>=1:
    print("\n")
    print("Prime numbers are:")
    print(prime,end=" ")
else:
    print("There is no prime numbers exsist")