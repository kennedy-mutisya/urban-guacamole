# testing kwargs

#list of kwargs
#the list of kwargs

def myKwargs(**kwargs):
    print("kwargs is ", type(kwargs))
    print(kwargs)
    #print("b is", kwargs["b"])

#senario a=23,b=30 =?{a:23,b:30}
myKwargs(a=23,b=30)

#sensrio no 3
#name="samson" email="samson@gmail.com"
#myKwargs({"name":"samson",})
myKwargs(name="samson",email="sam@sang.com", dict={"a":"a"})

def area_rectangle(length,width):
    area=length*width
    print(f"for rectangle with length {length} and width {width} area is {area}")

#option 1 you call it directly with args.
area_rectangle(5,2)# args
width=4
length=39
area_rectangle(width,length)#args
area_rectangle(width=width,length=length)#kwargs
#option3 you width kwargs:<>
area_rectangle(width=10,length=55)
#you have to match the parameter names with arguements
area_rectangle(width=10, length=55)
#area_rectangle(40)