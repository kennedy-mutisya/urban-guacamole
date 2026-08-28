#Turple
#

def my_args(*args):
    print(f"Args type of args{type(args)}")
    print(args)
    print(f"first arg {args[]}")
    print("-------------------")

my_args(30,67,97,100)
my_args("hello", True, 34)

def area_rectangle(length, width):
    area=length*width
    print("-------------------")
    print(f"for area of rectanle width length {length} and width {width} area is {area}")
    print("-------------------")
area_rectangle(20,10)

#function to sum numbers
def sum(a,b):
    ans=a+b

def sum2(*args):
    #tuple
    ans=0
    for n in args:
        print(f"n is {n}")
        ans=ans+n
        print(f"sum is {ans}")
    sum2(29, 49,34,40,69,98)