from math import sqrt
from mimetypes import init
import matplotlib.pyplot as plt
import numpy as np
import cmath
import os
def VectorInitializer():
    global x,y,z
    flags=True
    while flags==True:
        flags=False
        x=input("Enter the x component of your vector:")
        try:
            x=float(x)
        except:
            x=input("Your X component must be an integer value only.Press anykey to re-enter")
            flags=True
    flags=True
    while flags==True:
        flags=False
        y=input("Enter the y component of your vector:")
        try:
            y=float(y)
        except:
            y=input("Your Y component must be an integer value only.Press anykey to re-enter")
            flags=True
    flags=True
    while flags==True:
        flags=False
        z=input("Enter the z component of your vector:")
        try:
            z=float(z)
        except:
            z=input("Your Z component must be an integer value only.Press anykey to re-enter")
            flags=True

    
class vectors:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def printvector(self):
        print("your unit vector is:",str(x)+"i+ "+str(y)+"j+ "+str(z)+"k")

    
    def addvector(self,v1,sign):
        global addedx,addedy,addedz
        if sign=="a":
            addedx=float(self.x)+float(v1.x)
            addedy=float(self.y)+float(v1.y)
            addedz=float(self.z)+float(v1.z)
        elif sign=="s":
            addedx=float(self.x)-float(v1.x)
            addedy=float(self.y)-float(v1.y)
            addedz=float(self.z)-float(v1.z)
        print("your final vector is:",addedx,"i",addedy,"j",addedz,"k")

    def vectordotp(self,v1):
        global resultvector
        resultvector=((float(self.x)*float(v1.x))+(float(self.y)*float(v1.y))+(float(self.z)*float(v1.z)))
        print("Result:",resultvector)
        return resultvector
    def magnitude(self):
        result=(self.x*self.x)+(self.y+self.y)+(self.z*self.z)
        result=round(sqrt(result),3)
        print("Magnitude of the vector: ",str(x)+"i+ "+str(y)+"j+ "+str(z)+"k"," is",result)

    def vectorcrossp(self,v2):
        dotproductresultx=((self.y*v2.z)-(self.z*v2.y))
        dotproductresulty=((self.z*v2.x)-(self.x*v2.z))
        dotproductresultz=((self.x*v2.y)-(self.y*v2.x))

        print("your final vector is:",dotproductresultx,"i",dotproductresulty,"j",dotproductresultz,"k")

def matrixinitializer():
   mymatrix=[]
   row=[]
   rows=int(input("How many rows does your matrix have?"))
   columns=int(input("How many columns does your matrix have"))
   count=1
   for i in range(0,rows):
        for j in range(0,columns):
            elem=input("enter the next element:")
            row.append(elem)
        print(row)
        mymatrix.append(row)
        row=[]
   print("Your matrix is as such:\n",mymatrix)
   return(mymatrix,rows,columns)

class matrices:
    def __init__(self,mymatrix,rows,columns):
        self.matrix=mymatrix
        self.myrow=rows
        self.mycol=columns

    def addmatrix(self,sign,matrix):
        flag=False
        finalmatrix=[]
        rows=[]
        if matrix.myrow==self.myrow and matrix.mycol==self.mycol:
            flag=True
            print("is possible.")
        else:
            print("order doesn't match is not possible.")
           
        if flag==True:
            if sign=="addition":
                for r in range(0,self.myrow):
                    for c in range(0,self.mycol):
                        elem=float(self.matrix[r][c])+ float(matrix.matrix[r][c])
                        rows.append(elem)
                    finalmatrix.append(rows)
                    rows=[]
            else:
                 for r in range(0,self.myrow):
                    for c in range(0,self.mycol):
                        elem=float(self.matrix[r][c])- float(matrix.matrix[r][c])
                        rows.append(elem)
                    finalmatrix.append(rows)
                    rows=[]
        print("Your result matrix =")
        print(finalmatrix)

    def multiplymatrix(self,m2):
            row=[]
            newmat=[]
            elem=0
            flag=False
            if self.mycol==m2.myrow:
                print("Operation possible.")
                flag=True
            else:
                print("order does not match. Operation not possible.")
            count=0
            row=[]
            if flag==True:
                        for f in range(0,self.myrow):#for the number of rows this matrix
                            for col in range(0,m2.mycol):#multiply the row with the columns second matrix has
                                for nelements in range(0,self.mycol):#iterating for number of elements in initial matrix row
                                    # print("element no",nelements)
                                    # print("multiplying ",self.matrix[f][nelements],"with ",m2.matrix[nelements][col])
                                    elem=elem+(int(self.matrix[f][nelements])*int(m2.matrix[nelements][col]))
                                row.append(elem)
                                elem=0
                            newmat.append(row)
                            row=[]
            print("your final matrix:")
            print(newmat)
            return newmat

def validating_graphs():
    # print("Enter the equation of a quadratic graph in the equation: Y= ax^2+ bx + c")
    # a=input("a:")
    # b=input("b:")
    # c=input("c:")
    option=input("Which one of the following resembles your quadratic equation?\n1. Y=ax^2 + bx + c \n2. Y=a(x-r1)(x-r2)\n3. a(x-h)^2+k\nOption:")
    flag=0
    while flag==0:
        try:
            option=int(option)
        except:
            print("please re-enter")
            option=input("Which one of the following resembles your quadratic equation?\n1. Y=ax^2 + bx + c \n2. Y=a(x-r1)(x-r2)\n3. a(x-h)^2+k\nOption:")
            flag=0
        else:
            flag=1
    option=int(option)
    if option==1:
        print("Enter the equation of a quadratic graph in the equation: Y= ax^2+ bx + c")
        a=input("a:")
        b=input("b:")
        c=input("c:")
        print ("Your equation is:\nY="+a+"x^2 + ",b+"x + "+c)
    elif option==2:
        print("Enter the equation of a quadratic graph in the equation: Y=a(x-r1)(x-r2)")
        a=input("a:")
        b=input("r1:")
        c=input("r2:")
        print ("Your equation is:\nY="+a+"(x-"+ b+")(x-"+c+")")
    elif option==3:
        print("Enter the equation of a quadratic graph in the equation: Y=a(x-h)^2+k")
        a=input("a:")
        b=input("h:")
        c=input("K:")
        print ("Your equation is:\nY="+a+"(x-"+ b+")^2+"+c)
    else:
        print("invalid input,for now the type of graph is unrecognized by us.")
        option=a=b=c=-1
    return option,a,b,c
        

class graphs:
    def __init__(self,opt,a,b,c):
        self.type=opt
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)

    def graph_it(self):
        x = np.linspace(-10,10,100)
        if self.type==1:
            y=(self.a*(x**2))+(self.b*x)+self.c
        elif self.type==2:
            y=self.a*(x-self.b)*(x-self.c)
        elif self.type==3:
            y=(self.a*(x-(self.b**2)))+self.c
        fig = plt.figure(figsize = (5, 5))
        plt.grid()
        plt.plot(x, y)
        plt.show()

def menu():
       print("========== gravectrix =========\n~ A calculator for vectors and matrices ~\n (that also helps you plot your graphs!)  " )
       func=0
       while func<1 or func>3:
            func=int(input("What do you want to work with?\n1. Matrices\n2. Vectors\n3. Graphs\n"))
       os.system('cls')
       if func==1:
           print("==== Matrix Calculator ====")
           print("\nEnter details for the first matrix:")
           m1,m1rows,m1col=matrixinitializer()
           print("\nEnter details for the second matrix:")
           m2,m2rows,m2col=matrixinitializer()
           mym1=matrices(m1,m1rows,m1col)
           mym2=matrices(m2,m2rows,m2col)

           print("Great! What do we do now?")
           subopt=int(input("---- Options ----\n1. Addition\n2. Subtraction \n3. Multiplication "))
           while subopt<1 or subopt>3:
                subopt=int(input("---- Options ----\n1. Addition\n2. Subtraction \n3. Multiplication "))
           if subopt==1:
               sign="addition"
               mym1.addmatrix(sign,mym2)
           elif subopt==2:
               sign="subtraction"
               mym1.addmatrix(sign,mym2)
           elif subopt==3:
               mym1.multiplymatrix(mym2)
       elif func==2:
            print("==== Vector Calculator ====")
            print("enter data for the base first vector:")
            print("")
            VectorInitializer()
            myvector1=vectors(x,y,z)
            myvector1.printvector()
            # elif num==2:
            #     print("enter data for the first vector:")
            #     print("")
            #     VectorInitializer()
            #     myvector1=vectors(x,y,z)
            #     myvector1.printvector()
            #     print("")
            #     print("enter data for the second vector:")
            #     print("")
            #     VectorInitializer()
            #     myvector2=vectors(x,y,z)
            #     myvector2.printvector()
            print("Great! What do we do now?")
            subopt=int(input("---- Options ----\n1. Addition\n2. Subtraction \n3. Dot Product\n4. Cross Product\n5. Magnitude\n "))
            while subopt<1 or subopt>5:
                subopt=int(input("---- Options ----\n1. Addition\n2. Subtraction \n3. Dot Product\n4. Cross Product\n5. Magnitude\n "))

            if subopt==1:
                print("")
                print("enter data for the second vector:")
                print("")
                sign="a"
                VectorInitializer()
                myvector2=vectors(x,y,z)
                myvector2.printvector()
                myvector1.addvector(myvector2,sign)
            elif subopt==2:
                print("")
                print("enter data for the second vector:")
                print("")
                sign="s"
                VectorInitializer()
                myvector2=vectors(x,y,z)
                myvector2.printvector()
                myvector1.addvector(myvector2,sign)
            elif subopt==3:
                print("")
                print("enter data for the second vector:")
                print("")
                VectorInitializer()
                myvector2=vectors(x,y,z)
                myvector2.printvector()
                myvector1.vectordotp(myvector2)

            elif subopt==4:
                print("")
                print("enter data for the second vector:")
                print("")
                VectorInitializer()
                myvector2=vectors(x,y,z)
                myvector2.printvector()
                myvector1.vectorcrossp(myvector2)

            elif subopt==5:
                myvector1.magnitude()

       elif func==3:
           print("==== Graphing Calculator ==== ")
           opt,a,b,c=validating_graphs()
           if opt !=-1:
                mygraph=graphs(opt,a,b,c)
                mygraph.graph_it()
       
contin=1
while contin==1:
    menu()
    contin=int(input("do you want to continue? press 0 to terminate and 1 to continue."))
    while contin!=0 and contin!=1:
        contin=int(input("Press 0 to exit and 1 to continue."))

