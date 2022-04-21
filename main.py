# ---Q1---
function = lambda x: (x - 3) / x ** 2
number = int(input("Enter the number: "))
funcList = []
for i in range(1, number + 1, 1):
    funcList.append(function(i))
print(sum(funcList))


# ---Q2---
def recursive_q2(n):
    #This function calculate the equation ((n / (n + 2)) - 10) * recursive_q2(n - 1)
    if n == 0:
        return 1
    else:
        return ((n / (n + 2)) - 10) * recursive_q2(n - 1)


sec_number = int(input("Enter the second number: "))
print(recursive_q2(sec_number))
