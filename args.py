"""
use of args and kargs
"""

def magic(*args, **kargs):
  print("unamed args:", args)
  print(" named args:", kargs)

magic(1,2,3,color="blue",size="20")
magic("hello",1,2,3,shape="circle",name="jeff",color="blue",size="20")
