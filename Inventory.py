'''
Kitchen Inventory - a grocery package manager.
================================================================================


Program Goal: Tracking Food Items in an individual's kitchen.

Main Class: Inventory
Inventory will contain a list of food items, separated by subclasses.

Undecided: Subclasses *may* be food categories, *or* location (fridge/pantry)

Secondary class: Refridgerator

Secondary class: Freezer

Secondary class: Pantry

Each item in inventory will be a tuple (item, date of purchase, quantity)

List of Features Planned:
Bought Date
Expiration Date
Barcode (?)
List of "Essential Items" 
    -for each kitchen, if below a set threshold, items will be added to
    a Grocery list



--------------------------------------------------------------------------------
                                PROGRAM WORKFLOW:
--------------------------------------------------------------------------------
inventory == False
On startup checks for existing local text file for users kitchen.
    if it exists, skip start up menu
    inventory = True

Start up menu (SKIPPED IF LOCAL KITCHEN FOUND-> 
while inventory == False:
                Add, Choose, Delete Kitchen

    Add Kitchen-> 
                Asks for user input, then creates kitchen object w that name.

    Choose Kitchen -> 
                Lists Kitchen Names, asks user for kitchen to choose.
                
    Delete Kitchen -> 
                      Asks user for kitchen to delete, finds kitchen, asks for
                      confirmation of deletion.

Kitchen Chosen  -> 
                 Submenu for Kitchen:
                                     Remove Items
                                     Add Items
                                     List Items
                                     Switch Kitchen
                
                Add items -> 
                            Location Menu - > 
                                             Fridge
                                             Freezer
                                             Pantry
                            Location Chosen -> Add Items and Quantity
                                while loop until "f" for finished is entered:
                                Item: *user input*
                                Quantity: *user input*
                Switch Kitchen
                            Opens start up menu.
                                                   




Add Kitchen -> Asks user for name, then creates Kitchen object with that name.
'''

def start_up_menu():
    '''
    Start up menu to create Kitchen, or Choose Kitchen to view/manipulate.
    '''
    while True:
        
    
    
    
    
def menu():
    '''
    Main User menu for manipulating kitchen inventory
    '''
    while True:
        print ("A)\tRemove Items")
        print ("R)\tRemove Items")
        print ("F)\tFind Items")
        print ("L)\tList all Items")
        print ("D)\tDisplay Shopping List")
        print ("Q)\tQuit")
        print ()
    answer = input(str("Enter your choice: ")).upper()
    if len(answer) == 1 and answer in "ARFLQ": # Input validation for menu
          return(answer)

def sub_menu(menu):
    '''
    User menu for manipulating items in each location
    '''
    while True:
        print(f'You are in the {menu} menu')
        print ('1) Add Item')
        print ('2) Remove Item')
    
def main():
  '''
  Main program loop, starts menu function, accesses all other funcitons
  through user input.
  
  NEED TO SETUP WAY FOR PROGRAM TO SAVE SPECIFIC KITCHEN OBJECTS TO FILE:
  FOR NOW ITS INITIALIZING A NEW KITCHEN EVERY TIME.
  
#===============================================================================
  
  '''
  
  kitchen_database = Kitchen() # Initializing house database
  choice = -1 # Placeholder for menu while loop state variable

  while choice != 'Q':  # While user input isn't 'q' or 'Q', keep menu going
        choice = menu()

        if choice == 'A': # If user inputs 'a' or 'A', start addHouse fnctn
            kitchen_database += food_item() # food init runs through food object 
            print()                    # creation, then += adds to the database
            
            # Not perfect, 
          
        elif choice == 'R': # if user inputs 'r' or 'R', start remove_food fnctn
            kitchen_database._remove_from_database()
            print()

        elif choice == 'F': # if user inputs 'f' or 'F', start findhouse fnctn
            result = house_database._findHouse('f')
            if not not result: # if function doesn't return False/if house found
                print(result)  # print house object
            print()

        elif choice == 'L': # if L, print out the house database.
            print()
            print(house_database)
        
        
        elif choice == 'Q':
            print("Program exited.")
            return
        else: print("Invalid Input, Try Again")




class Kitchen(self):
    def __init__(self):
        self.inventory = [self.fridge, self.freezer, self.pantry]
        self.fridge = {}
        self.freezer = {}
        self.pantry = {}
    
    def _addFridge(self):
        
        


    def _addFridge(self):



    
    
        
class Refridgerator(self):
    def __init__(self):