# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run #LIBRARY PROJECT/ SADAT ALI/ FA23-BCT-034
#library inventry
LIBRARY=[["A COLD HEART","JHON","1963","STATUS:AVAILABLE"],["A DEATH","WILLIAM","1962","STATUS:CHECKED OUT"]]
#function to add books
def add_book():
 print("ENTER THE DETAILS OF BOOK YOU WANT TO ADD :")
 BOOK=[]
 BOOK.insert(0,input("ENTER THE TITLE OF THE BOOK:"))
 BOOK.insert(1,input("ENTER THE NAME OF AUTHOR :"))
 BOOK.insert(2,input("ENTER THE PUBLICATION YEAR OF THE BOOK:"))
 BOOK.insert(3,["STATUS:AVAILABLE"])
 print("YOUR HAS BEEN ADDED TO LIBRARY")
 LIBRARY.append(BOOK)
 return LIBRARY
#function to show the content of library
def display_library():
    #for x in LIBRARY:
      print(LIBRARY)
 
#BOOK COUNTING
def count_books():
  print("THE NUMBER OF BOOKS IN LIBRARY IS :")
  print(len(LIBRARY)) 

#BOOK SEARCH FUNCTION
def search_books():
  KW=input("ENTER THE KEYWORD OR INFORMATION ABOUT THE BOOK")
  for i in range(len(LIBRARY)):
    y=LIBRARY[i]
    i=0
    for i in range(3):
      if KW==y[i] :
        print("RESULT:")
        print(y)
        
#Rrturning book function
def return_book():
  KW=input("ENTER THE TITLE OR AUTHER OR PUB.YEAR OF THE BOOK YOU WANT TO RETURN:")
  for i in range(len(LIBRARY)):
    y=LIBRARY[i]
    i=0
    for i in range(3):
      if KW==y[i] :
        print(y[0],"  HAS BEEN RETURNED..")
      y[3]=["STATUS:RETURNED"]
  return LIBRARY

#checking out book function
def check_out_book():
  KW=input("ENTER THE TITLE OR AUTHER OR PUB.YEAR OF THE BOOK YOU WANT TO CHECK OUT:")
  for i in range(len(LIBRARY)):
    y=LIBRARY[i]
    i=0
    for i in range(3):
      if KW==y[i] :
        print(y[0],"  HAS BEEN CHECKED OUT..")
        y[3]=["STATUS:CHECKED OUT"]  
    return LIBRARY
def main():    
#BOOK INVENTRY
 #LIBRARY=[]
 # for testing
#we are entering data in library list to check the working of program
 
 print("WELCOME TO THE LIBRARY") 
 print('''                              ...HERE IS THE MANUE ...
       
      1. TO ADD A NEW BOOK
      2. TO DISPLAY THE ALL BOOKS AND CONTENTS OF LIBRARY
      3. TO COUNT THE NUMBER OF BOOKS OF LIBRARY
      4. TO SEARCH THE BOOK
      5. TO CHECK OUT THE BOOK 
      6. TO RETURN THE BOOK
       ''')
 num = input("ENTER THE  RESPECTED NUMBER OF FUNCTION YOU WANT TO PERFORM (1_6)")
 if num =="1":
   add_book()
 if num ==  "2":
   display_library()
   
 if num == "3" :
   count_books()
   
 if num == "4" :
  search_books()
  
 if num =="5":
  check_out_book()
 
 if num == "6" :
  LIBRARY = return_book()

#statements to repeat main TO DO ANOTHER FUNCTION if user wants to do
n="0"
while n=="0" :
  main()
  print("DO YOU WANT TO DO ANOTHER FUNCTION?")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="1" :
     break 
  
