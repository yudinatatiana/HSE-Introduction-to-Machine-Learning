# Software design

## Separation of concerns

#### Exercise: In the above program, identify and describe at least two of the sub-problems which are solved multiple times. (I see at least three or four.)

```python 
x = int(input("Tell me the first number: "))
y = int(input("Tell me the second number: "))
op = input("tell me the operation (add, multiply): ")

if op == "add":
  print("result: ", x+y)
elif op == "multiply":
  print("result: ", x*y)
```

1. The problem I see is that reading, processing and outputting data happens together. 
2. There is absolutely no validation for data entry yet (only numbers).
3. There should be a handling of situations when a person has entered something other than add and multiply.

#### Exercise: Choose one of the sub-problems, write a common solution to that subproblem in the form of a function, and modify the program to use your common solution instead of solving the problem multiple times.

```python
def get_data():
    def get_int(pos):
        temp = ""
        while temp.isdigit() is False:
            temp = input(f"Tell me the {pos} number (integer): ")        
        return int(temp)
    
    def get_op():
        allowed_op = ["add", "multiply"]
        temp = None
        while temp not in allowed_op:
             temp = input("tell me the operation (add, multiply): ")
        return temp        
    
    x = get_int("first")
    y = get_int("second")
    op = get_op()
    return x, y, op

def process(x, y, op):
    if op == "add":
        return x + y
    elif op == "multiply":
        return x * y
    else:
        raise "Operation error"
        
def print_result(result):
    if result is not None:
        print("result: ", result)
    else:
        print("Something went wrong!")
        

def main():
    x, y, op = get_data()
    result = process(x, y, op)
    print_result(result)

if __name__ == '__main__':
    main()
```

```
Tell me the first number (integer): f
Tell me the first number (integer): 1
Tell me the second number (integer): 2
tell me the operation (add, multiply): s
tell me the operation (add, multiply): add
result:  3
```