#Lower triangle
def lower_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()

#Upper triangle
def upper_triangle(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("* ", end=" ")
        print()


#Pyramid
def pyramid_triangle(n):
    k = 0
    for i in range(1,n+1):
        for space in range(1,(n-i)+1):
            print(end="  ")
        while k!=(2*i-1):
            print("* ", end="")
            k += 1
        k = 0
        print()

n=int(input("Enter the number of rows: "))   #for how much time of rows print asterik(*) Pattern
lower_triangle(n)
upper_triangle(n)
pyramid_triangle(n)
