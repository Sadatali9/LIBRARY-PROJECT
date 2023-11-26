#LIBRARY PROJECT/ SADAT ALI/ FA23-BCT-034
#function to add books
def add_book(LIBRARY):
 print("ENTER THE DETAILS OF BOOK YOU WANT TO ADD :")
 BOOK=[]
 BOOK.insert(0,input("ENTER THE TITLE OF THE BOOK:"))
 BOOK.insert(1,input("ENTER THE NAME OF AUTHOR :"))
 BOOK.insert(2,input("ENTER THE PUBLICATION YEAR OF THE BOOK:"))
 BOOK.insert(3,"STATUS:AVAILABLE")
 print("YOUR HAS BEEN ADDED TO LIBRARY")
 LIBRARY.extend(BOOK)
 return LIBRARY
#function to show the content of library
def display_library(LIBRARY):
    #for x in LIBRARY:
      print(LIBRARY)
 
#BOOK COUNTING
def count_books(LIBRARY):
  print("THE NUMBER OF BOOKS IN LIBRARY IS :")
  print(len(LIBRARY)) 

#BOOK SEARCH FUNCTION
def search_books(LIBRARY):
  KW=input("ENTER THE KEYWORD OR INFORMATION ABOUT THE BOOK")
  for i in range(len(LIBRARY)):
    y=LIBRARY[i]
    i=0
    for i in range(3):
      if KW==y[i] :
        print("RESULT:")
        print(y)
        
#Rrturning book function
def return_book(LIBRARY):
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
def check_out_book(LIBRARY):
  KW=input("ENTER THE TITLE OR AUTHER OR PUB.YEAR OF THE BOOK YOU WANT TO CHECK OUT:")
  for i in range(len(LIBRARY)):
    y=LIBRARY[i]
    i=0
    for i in range(3):
      if KW==y[i] :
        print(y[0],"  HAS BEEN CHECKED OUT..")
      y[3]=["STATUS:CHECKED OUT"]
    else:
        print("STATUS: CHECK OUT (BOOKS has been checked out)")
        break
  return LIBRARY
def main():    
#BOOK INVENTRY
 LIBRARY=[]
 # for testing
#we are entering data in library list to check the working of program
 LIBRARY=[["A COLD HEART","JHON","1963","STATUS:AVAILABLE"],["A DEATH","WILLIAM","1962","STATUS:CHECKED OUT"]]
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
  LIBRARY = add_book(LIBRARY)
  print("DO YOU WANT TO GO BACK TO MANUE ")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="0" :
    main()
 if num ==  "2":
  LIBRARY = display_library(LIBRARY)
  print("DO YOU WANT TO GO BACK TO MANUE ")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="0" :
    main()
 if num == "3" :
  LIBRARY = count_books(LIBRARY)
  print("DO YOU WANT TO GO BACK TO MANUE ")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="0" :
    main()
 if num == "4" :
  LIBRARY = search_books(LIBRARY)
  print("DO YOU WANT TO GO BACK TO MANUE ")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="0" :
    main()
 if num =="5":
  LIBRARY = check_out_book(LIBRARY)
  print("DO YOU WANT TO GO BACK TO MANUE ")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="0" :
    main()
 if num == "6" :
  LIBRARY = return_book(LIBRARY)
  print("DO YOU WANT TO GO BACK TO MANUE ")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="0" :
    main()
#statements to repeat main TO DO ANOTHER FUNCTION if user wants to do
n="0"
while n=="0" :
  main()
  print("DO YOU WANT TO DO ANOTHER FUNCTION?")
  n=input("ENTER 0 FOR YES AND 1 FOR NO....")
  if n=="1" :
     break 
  