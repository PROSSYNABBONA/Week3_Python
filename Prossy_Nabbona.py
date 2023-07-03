#Advanced topics in python
"""
Regular expressions
Generators and iterators
Decorators
Context managers
Multithreading and multiprocessing

"""
#Regular exprssions
"""
\d:matches any digit 0-9
\w:matches any alphanumeric aharacter(a-z,A-Z,0-9)
\s:matches any white space character(space,tab)
*:matches zero or more occurence of the preceding character or group
.:matches any character except a newline
+:matches one or more occurence of the preceding character or group
?:matches zero or one occurence of the preceding character or group
[ ]:matches any character  within the square brackets
[^ ]:matches any character not within the square brackets
^:matches the start of the line
$:Mathes the end of the line

"""

#Matching and Searching
#regex re.match(), re.search(), re.findall()

#Example1
#Demonstrating regrex | Match First Word,Match group word,Match all numbers
# import re
# text="Hello, my name is Nabbona Prossy.I am a software engineer,with 10 years of experience"

# #Match first Word
# match=re.search(r"\b\w+\b",text)#r is for the regression
# if match:
#     print( "Matches:", match.group())
    
# #Match the numbers
# matches=re.findall(r"\d+", text)
# print("Match:", matches) 

#Example2 Validate email format or email address
# import re
# def validate_email(email):   
#     pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern,email):
#         return True
#     else:
#         return False
    
#     #Example usage
# email1="prossienabbonna20@gmail.com"
# email2="prossienabbonna20@gmailcom"
# print(validate_email(email1))
# print(validate_email(email2))

#Generators and iterators
#'yield' generator
#iterators '__iter__' "__next__" iterator
# def factorial(n):
#     #return factorial number
#     if n==0:
#         yield 1
#     else:
#         # yield n * factorial(n-1)
#         fact=1
        
#         for i  in range(1,n+1):
#          fact *=i
#          yield fact
    
#     for i in range(1, 10):
#         print(factorial(i))


# def factorial(n):
#     if n == 0:
#         yield 1
#     else:
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#             yield fact

# for i in range(1, 10):
#     print(list(factorial(i)))

#Example 3
#genarate function that yilds the square of the numbers from 1 to 10
def squares():
 for i in range(1,10):
     yield i**2
#create an iterator object that yields the square of numbers from 1-10
squares_iterator=squares()
#print the first 5 squares
for i in range(5):
    print(next(squares_iterator))     

#Decorators helps us to modify the 
# behavior of functions or classes without directly changing their soyrce code
#we use @my_decorator
def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
        return inner
    @my_decorator
    def outer_decorator():
        print("This is outer decorator")
        
        outer_decorator()
        
        #Context managers
        #Creating context managers
        """
        When creating context managers using classes, user need to ensure that the class has the methods
        : __enter__() and __exit__().
        The __enter__() returns the resource that needs to be managed and the __exit__() does not return anything
        but performs the cleanup operations. 
        """
        # Python program creating a
# context manager

class ContextManager():
	def __init__(self):
		print('init method called')
		
	def __enter__(self):
		print('enter method called')
		return self
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('exit method called')

with ContextManager() as manager:
	print('with statement block')

"""
File management using context manager
The FileManager class helps in opening a file, writing/reading 
contents, and then closing it.
"""
# Python program showing
# file management using
# context manager

class FileManager():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()

# loading a file
with FileManager('test.txt', 'w') as f:
	f.write('Test')

print(f.closed)
