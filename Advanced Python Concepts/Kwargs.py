def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks
   for item in kwargs.keys():
       print(f"{item} : {kwargs[item]}")

marks(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)