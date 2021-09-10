# Task 1
int = int(input("Enter int numb "))
float = float(input("Enter float number "))
string = (input("Enter string "))
bool = bool(input("Enter 0 or 1 "))
print ("int is", int)
print ("float is", float)
print ("string is", string)
print ("bool is", bool)
# Task 2
time = int(input("Enter time in seconds "))
hours = time //3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"{hours} : {minutes} : {seconds}")
# Task 3
num = int(input("Enter number"))
print (num + (num *  11) + (num * 111))
# Task 4
number = int(input("Enter number"))
k = int
answer = 0
while number != 0:
   k = number % 10
   number = number //10
   if k > answer:
       answer = k
print (answer)
# Task 5
v = int(input("Enter viruzcka"))
e = int(input("Enter isderzky"))
if e > v:
    print("ubitok")
if v > e:
    print("pribl")
    prib = v - e
    rent = prib/v
    kolvo = int(input("Enet staff quontty"))
    pfo = prib/kolvo
    print ("Прибыль на одного сотрудника = ", pfo )
    print("Прибыль = ", prib )
    print("рентабильность = ", rent )
# Task 6
a = int(input("Enter a "))
b = int(input("Enter b "))
k = 1
while a < b :
    a = a + (a * 0.1)
    k = k + 1
print(k)



