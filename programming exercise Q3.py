print("AMNAH ZAREEN 18B-119-CS-A")
print("PROGRAMMING EXERCISE QUESTION-3")

f_term = int(input("Enter the first term :"))
c_diff = int(input("Enter the common difference :"))
nth_term = int(input("Enter the term position :"))

def arithmetic_seq(f_term, c_diff, nth_term):
    print("The first term is " , f_term)
    print("The common difference is " , c_diff)
    print("The term position is " , nth_term)


program = input("Do you want to continue ?:")
while program == "yes":  
    
    nth_term2 = eval(input("Enter the next nth term position :"))
    a_n = f_term + (nth_term-1)*c_diff
    arithmetic_seq(f_term, c_diff, a_n)
    program = input("Do you want to continue ?:")
    
