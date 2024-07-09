


def fibonacci_one(n):
    sum = 0
    b = 1
    while sum <= n:
        yield sum # by placing yield here it uses this value which improves the quality and precisness of fibonacci function to generate the first 0
        a = b
        b = sum
        sum = a + b
       
# this is mostly recommended by chatGPT, and after some debugging i can agree but for a beginner of python programming i believe it i easier to understand the fibonachi_one above 
def fibonacci_two(n):
    a, b = 0, 1
    while a <= n:
        yield a 
        a, b = b, a + b

    
for i in fibonacci_one(832040):
    print(i)