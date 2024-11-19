x = 3
def fact(x):
    if x == 1:#base case
        return 1
    else:
        return x * fact(x-1)#recursive case
print(fact(x))

#first call
    # 3 * fact(3-1) now it computes fact(2). Waiting for result of fact(2)
#second call
    # 2 * fact(2-1) now it computes fact(1). Waiting for result of fact(1)
#third call 
    # x==1 so return 1. stops recursion
#recursion "unwind"
    # returning from fact(1) returns 1
    # returning from fact(2)
        # was waiting for fact(1). Computes 2 * 1 = 2 and return 2.
    # returning from fact(3)
        # was waiting for fact(2). Computes 3 * 2 = 6 and returns 6
        
    # Result of fact(3) = 6