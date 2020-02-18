# def foo():
#     x = 20

#     def bar():
#         global x
#         x = 25
    
#     print("Before calling bar: ", x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar: ", x)

# foo()
# print("x in main : ", x)

# def outer():
#     x = "local"
    
#     def inner():
#         x = "nonlocal"
#         def inner2():
#             nonlocal x
#             x = "inner2"
#             print("inner 2 : ",x)
            
#         inner2()
#         print("inner:", x)
    
#     inner()
#     print("outer:", x)

# outer()

# def outer():
#     x = "local"
    
#     def inner():
#         nonlocal x
#         def inner2():
#             nonlocal x
#             x = "inner2"
#             print("inner 2 : ",x)
            
#         inner2()
#         print("inner:", x)
    
#     inner()
#     print("outer:", x)

# outer()