class parent_class: #define the parent class
    def getdata( self , value) : 
        self . data = value
    def display( self ) : 
        print (self . data)
class child_class(parent_class) : #inherits from parent_class
    def display( self ) :
        print (self . data)
x=parent_class() #instance of parent_class
y=child_class() #instance of child_class
x. getdata('I am parent class')
y. getdata ('I am child class')
x. display () 
y. display ()

