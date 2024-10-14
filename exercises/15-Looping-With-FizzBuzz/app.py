def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(100):
        if i % 3 == 0 and i % 5 ==0:
            print("fizzBuzz")
        elif i % 3 == 0: 
            print("fizz")
        elif i % 5 == 0:
           print("buzz")
        
        else:
            print(i)

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
