
def args_kwargs(*args, **kwargs):
    print("-------------")
    print("all args", args)
    print("all kwargs", kwargs)
    print("--------------")

#error
#args_kwargs(a=2, b=30, 45, 39)
args_kwargs(45,39,a=2,b=30)