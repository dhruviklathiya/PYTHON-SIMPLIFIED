# **kwargs => key word arguments
def function_demo (**kwargs):
    print(kwargs)

function_demo(hey=1,hi=3)
    # Note that hey & hi are not pre-defined variable their instance are being created at the very moment when function is called

# What is order of passing and receiving arguments
    # simple parameter
    # *args
    # default parameter
    # **kwargs

def all_4_para(name,*args,something = 'Default parameter',**kwargs):
    print(name)
    print(args)
    print(something)
    print(kwargs)

all_4_para("DCODER",1,2,3,4,5,hey=1,hi=3)