def fun(M,X,Y,Z):
    print("The 1/4th weekly salary is:",(M*X)/(Z*Y))
print("Enter the M,X,Y,Z values:")
(M,X,Y,Z)=map(int,input().split())
fun(M,X,Y,Z)
