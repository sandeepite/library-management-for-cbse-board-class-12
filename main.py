import os
import pickle
import time
width = "150"
height = "50"
os.system("mode con cols="+width+"lines="+height)

######ADD CODE FOR SPECIAL EFFECTS
##
##os.system('COLOR F0')
##
#####end


j=["L","I","B","R","A","R","Y"," "]
for c in range(0,8):
    print "\n"*30
    for k in range(0,c):
        
        print " "*5, j[k],
        
     
    print "\n"*20
    
    time.sleep(0.2)
print
#print "\n"*50
#LOGO
c=0
while True:
    c+=1
    print "*"*4,
    if c>4:
        print "*"*4,
    if c<=2:
        print " "*10,
        print "*"*15,
    if c>2 and c<=4:
        print " "*18,
        print "*"*5,
    if c>4 and c<5:
        print " "*11,
        print "*"*5,
    if c>=5:
        print " "*3,
        print "*"*15,
    if c<3 or c>4:
        print    " "*5,
        print "*"*3,
    if c>=3 and c<5:
        print " "*12,
        print "*"*3,
    if c==4  or c==6 :
        print "*"*5,
    if c==5 :
        print " "*2,
        print "*"*3,
    if c==5:
        print " "*4,
        print "2.0.1.1",
        
    print     
    if c>5:
        
        break
    
#Programming Project Starts Here





class lib:
    def __init__(self):
        self.act=0
        self.bname=" "
        self.code=0 
        
    def intro(self):
        print "#Select Your Choice : "
        print "#1}Borrow","\n","#2}Return"
        print "#3}Available Books","\n","#4}Borrowers List"
        print "#5}Books Status"
        print "#6}Add new books to Library"
        print "#}Press Enter to exit..."

    def add(self):
                    self.bname=raw_input("Enter book Name: ")
                    self.code=input("Enter Code of book:")
    def register(self):
                   self.name=raw_input("Name of borrower:")
                   self.bookname=raw_input("Enter the name of Book:")
                   self.code=input("Enter the book code:")
                   self.date=time.time()
    def stat(self):
                   print "Bookname","\t","Code","\n", self.bookname,"\t"*2,
                   print self.code
                   #print "Book status changed To:UnAvailable...."
                   
    def outdel(self):
                   print "Name","\t","Bookname","\t","Code","\t"
                   #print self.name,"\t"*2 , self.bookname,"\t"*2,self.code,"\t"#,self.date
    def show(self):
                   print "Bookname","\t","Code"   
                   print self.bname,"\t",self.code
    def bshow(self):
                   print "Name","\t","Bookname","\t","Code"
                   print self.name,self.bookname,self.code ##self.date()
    def delrec(self,n):
                   if self.name==n:
                       self.outdel()
                       return 1
                   else:
                       return 0
    def outdelstat(self):
                   print "Book Status:Available Again" ,self.code
    def delstat(self,n):
                  if self.code==n:
                      return 1
                  else:
                      m=self.code
                      self.outdelstat()
                      return 0
                    
  
x=lib()
x.intro()
print "\n"*20
while True:
               act=raw_input("Your choice:")
               if act=="1":
                              #Code To open book list
                              print"Here is the List of All Available books"
                              
                              op=open("list.dat","r")
                              try:
                                             while True:
                                                            x=pickle.load(op)
                                                            x.show()
                              except EOFError:
                                             print "Thats all for now..."
                                             print "::"*90
                                             op.close()

                              #Now For opting to borrow one
                              x.register()
                              bl=open("borrowlist.dat","ab")
                              pickle.dump(x,bl)
                              bl.close()
                              x.stat()
                              bs=open("bookstat.dat","ab")
                              pickle.dump(x,bs)
                              bs.close()                             


               elif act=="2":
                   ##########Return()
                   ##Delete function
                   bl=open("borrowlist.dat","rb")
                   temp=open("temp","wb")
                   n=raw_input("enter the name for Returning:")
                   
                   try:
                       while True:
                            x=pickle.load(bl)
                            m=x.code
                            if x.delrec(n)==0:
                                pickle.dump(x,temp)
                                
                            else:
                                k=m
                                #pass
                   except EOFError:
                       
                       print "k..."
                       print "::"*90
                   bl.close()
                   temp.close()
                   os.remove("borrowlist.dat")
                   os.rename("temp","borrowlist.dat")

                   #Function to remove book
                
                   bs=open("bookstat.dat","rb")
                   temp=open("temp","wb")
                   #m=x.code
                   try:
                       while True:
                            x=pickle.load(bs)
                            if x.delstat(k)==0:
                                pickle.dump(x,temp)
                   except EOFError:
                       print "Removed if in the database Else ignored ....."
                       print "::"*90
                   bs.close()
                   temp.close()
                   os.remove("bookstat.dat")
                   os.rename("temp","bookstat.dat")
                   
                   
               elif act=="3":
                              #x.Av_books()
                              
                              op=open("list.dat","r")
                              try:
                                             while True:
                                                            x=pickle.load(op)
                                                            x.show()
                              except EOFError:
                                             print "Thats all for now..."
                                             print "::"*90

               elif act=="4":
                              #borrowlist()3
                              bop=open("borrowlist.dat","rb")
                              try:
                                             while True:
                                                            x=pickle.load(bop)
                                                            x.bshow()
                              except EOFError:
                                             print "Thats all for now..."
                                             print "::"*90
                                             bop.close()

                              
                              
               elif act=="5": 
                              #x.bookstat()
                              bstat=open("bookstat.dat","rb")
                              try:
                                             while True:
                                                            x=pickle.load(bstat)
                                                            x.stat()
                              except EOFError:
                                             print "Thats all for now..."
                                             print "::"*90
                                             bstat.close()

                                                 
               elif act=="6":
                              #adding Books
                              
                              x=lib()
                              wpf=open("list.dat","ab")
                              while True:
                                             x.add()
                                             pickle.dump(x,wpf)
                                             ans=raw_input("any more? y")
                                             if ans!="y":
                                                            wpf.close()
                                                            break
                                             


               else:
                              print "\n"*50
                              k=[" "*10,"T","h","a","n","k","s"," "," "*20,"for "," "*20," ","C ","o","m","i","n","g"]
                              for c in range(0,18):
                                  print k[c],
                                  time.sleep(0.25)    
                              print 
                              #print "\t"*5,"Thanks for coming"
                              k=[u"\u00a9","r","e","s","e","r","v","e","d",]
                              for c in range(0,9):
                                  print k[c],
                                  time.sleep(0.25)
                              print    
                              k=["c","o","d","e"," "*20,"by"," "*20,"Sharan"]
                              for c in range(0,8):
                                  print k[c],
                                  time.sleep(0.25)
                              break







