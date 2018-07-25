import pickle, Emp
f=open('emp.dat','wb')
n=int(raw_input("how many employees?"))

for i in range(n):
    id = int(raw_input("enter id"))
    name = raw_input("enter name")
    sal = float(raw_input("enter sal"))
    e=Emp.Emp(id,name,sal)
    pickle.dump(e,f)
f.close()
