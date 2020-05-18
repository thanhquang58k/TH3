def benefit(t,n,k):
    S=n*(t/100)*k
    print("Tien lai:",S)
    #Tien nhan lai duoc
    S=n+S
    print("So tien nhan lai duoc:",S)
t=int(input("Lai suat theo thang="))
n=int(input("So tien ban dau="))
k=int(input("So thang gui="))
benefit(t,n,k)
