#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = int(input("Tell me the first number: "))
y = int(input("Tell me the second number: "))
op = input("tell me the operation (add, multiply): ")

if op == "add":
  print("result: ", x+y)
elif op == "multiply":
  print("result: ", x*y)


# In[18]:


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


# In[ ]:




