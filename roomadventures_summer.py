################################################
#Nia Bourgeois
#April 29, 2021
#Room Adventure
################################################



# The blueprint for a room
class Room(object):
    #THE CONSTRUCTOR
    def __init__(self, name):
        self.name = name    #contains room's name
        self.exits = []     #contains room's exits (north, south etc.)
        self.exitLocations = []     #contains the room found at exit
        self.items = []     #contains observable items in room
        self.itemDescriptions = []  #contains description of observable items
        self.grabbables = []    #contains items in the room that user can grab
        self.useables = []     #contains items that can be opened

        #GETTERS AND SETTERS FOR INTSANCE VARIABLES

        #get & set name
    @property
    def name(self):
        return self._name  #why the underscore?
    @name.setter
    def name(self, value):
        self._name = value

        #get and set exit
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value

        #get & set exitLocations
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

        #get & set items
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value

        #get & set itemsDescription
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

        #get & set grabbables
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

        #get & set useable
    @property
    def useables(self):
        return self._useables
    @useables.setter
    def useables(self,value):
        self._useables = value
        

    #adding an exit to the room
    def addExits(self, exit, room):
        self._exits.append(exit)
        self._exitLocations.append(room)

    #adding items to the room
    def addItems(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)

    #adding grabbable to the room
    def addGrabbables(self, item):
        self._grabbables.append(item)

    #removing a grabbable from the room
    def delGrabbables(self, item):
        self._grabbables.remove(item)

    #adding an useable item to the room
    def addUseables(self, item):
        self._useables.append(item)
        

    #returns description of the room
    def __str__(self):
        s = "You are in {}.\n".format(self.name)    #room name

        s += "You see: "            #items in the room
        for item in self.items:
            s += item + " " #+ openitems
        s += "\n"

        s += "Exits: "              #exits from room
        for exit in self.exits:
            s += exit + " "

        return s

#additional 'rooms'
guard = Room("Guard")

escape = Room("Escape")
#CREATE THE ROOMS
def createRooms():
    global currentRoom   #what does global mean

    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    # ADDITIONAL ROOMS
    r5 = Room("Room 5")
    r6 = Room("Room 6")
    r7 = Room("Room 7")
    r8 = Room("Room 8")
    r9 = Room("Room 9")
    r10 = Room("Room 10")
    r11 = Room("Room 11")
   
    
#ROOM 1
    #add room 1 exits
    r1.addExits("east", r2)
    r1.addExits("south",r3)
    #add grabbable to room 1
    r1.addGrabbables("key")
    #add items to room 1
    r1.addItems("chair","It is made of wicker and no one is sitting on it")
    r1.addItems("table","It is made of oak. A golden key rests on it")
#ROOM 2
    #add room 2 exits
    r2.addExits("west", r1)
    r2.addExits("south",r4)
    r2.addExits("east",r6)
    #add items to room 2
    r2.addItems("rug","it is nice and Indian. It also needs to be vaccumed")
    r2.addItems("fireplace","It is full of ashes")
#ROOM 3
    #add room 3 exits
    r3.addExits("north",r1)
    r3.addExits("east",r4)
    r3.addExits("west",r7)
    #add grabbable to room 3
    r3.addGrabbables("book")
    r3.addGrabbables("bag")
    #add items to room 3
    r3.addItems("bookshelves","They are empty. Go figure. -_-")
    r3.addItems("bag","There is some tape, rope, chloroform, and a towel.")
    r3.addItems("desk", "The bag is resting on it. So is a book.")
#ROOM 4
    #add room 4 exits
    r4.addExits("north",r2)
    r4.addExits("west", r3)
    r4.addExits("south",guard)
    #add grabbables to room 4
    #add items to room 4
    r4.addItems("money_counting_machine"," It is counting a lot of bills.")
    r4.addItems("sign", "There is a sign on the south door that says 'Carl'")
    

#ADDITIONAL ROOMS
#ROOM 5---- GUARD
    

#ROOM 6
    #add room 6 exits
    r6.addExits("west",r2)
    r6.addExits("east",r9)
    r6.addExits("north",guard)
    #add grabbables to room 6
    #**no grabbables**
    #add items to room 6
    r6.addItems("mirror","Mirror is foggy, looks like someone just showered.")
    r6.addItems("toilet","Looks like he also forgot to flush!")
    r6.addItems("sink","The sink is pretty clean")
    r6.addItems("floor","There is a wet trail leading north")
#ROOM 7
    #add room 7 exits (GUARD)
    r7.addExits("west",None)
    r7.addExits("east",r3)
    #no grabbable
    #add items
    r7.addItems("window","Hmm the window is open, wonder what's out the there...")
    r7.addItems("table", "There is a plate with some dead fish on it under the window on the west wall")
    
#ROOM 8----GUARD
    

#ROOM 9
    #add room 9 exits
    r9.addExits("west",r6)
    r9.addExits("east",r10)
    r9.addExits("south",None)
    #add grabbables to room 9
    r9.addGrabbables("code-3421")
    r9.addGrabbables("money")
    r9.addGrabbables("list")
    #add items to room 9
    r9.addItems("safe","Hmm, there's a key hole on the safe...") #have the code inside only after they use the key
    r9.addItems("table","There is a plate with dead fish on it under the window on the south wall")
    r9.addItems("window","The window is open, wonder what's out there...")
    #add usable item
    r9.addUseables("key")
    
#ROOM 10
    #add room 10 exits (has secret exit)
    r10.addExits("west",r9)
    #add grabbable to room 10
    r10.addGrabbables("gold")
    r10.addGrabbables("chest")
    #add item to room 10
    r10.addItems("electronic_lock","*input code to unlock secret exit*")
    r10.addItems("chest", "There is a vintage looking chest, inside it is some gold!")
    r10.addUseables("code-3421")


    #set current room as room 1
    currentRoom = r1





# # # # # # # # # # # # # # # # # # # # # MAIN PROGRAM # # # # # # # # # # # # # # # # # # # # # # # # 

#START THE GAME !!!
inventory = [] #create inventory (its empty... but not for long)
createRooms() #create the rooms

#Get player name
playerName = input("Input player name: ")

#ADD INTSRUCTIONS
print("{}, you've been kidnapped and need to escape the maze before sunrise!".format(playerName))
print("Go through the rooms and collect items to help you in your escape.")
print("Use the actions look, grab, go, or use to explore")
print("But watchout! Some rooms have kidnappers, don't get caught!")
print("Good luck {}!".format(playerName))
print(input("Press enter to begin"))
      

#Play forever! (until palyer quits or dies)
while(True):
    #set statues for situation awareness (room and inventory info)
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    #if current room is none, player is dead --> exit game
    if (currentRoom == None):
        print ("Uh oh! A group of angry alligators are surrounding you! x_x")
        break
    elif (currentRoom == guard):
        print ("Oh no! You've been spotted by a kidnapper! x_x")
        break
    elif(currentRoom == escape):
        print ("Yay! You made it!! :)")
        break

    
    #display status
    print("=============================================================")
    print(status)

#PLAYER INPUT SETTINGS 
    #propmt for player input
    action = input("What to do? ")
    action = action.lower()     #make user input lowercase
    #allow user to leave game with quit, exit, or bye
    if (action == "quit" or action == "exit" or action == "bye"):
        break
    #set a default response for invalid inputs
    response = "ERROR_ _// valid verbs are: go, grab, take, and use"
    #split user input (by spaces) and store words in list
    words = action.split()
    #only two - word inputs
    if len(words) == 2:
        verb = words[0]
        noun = words[1]
        #verb is "go"
        if (verb == "go"):
            response = "Invalid exit." #default response
            for i in range(len(currentRoom.exits)):  #check for valid exits
                if (noun == currentRoom.exits[i]):
                    #exit is valid, change current room
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room changed."
                    break
        #verb is "look" 
        elif (verb == "look"):
            response = "I don't see that item."  #default response
            for i in range(len(currentRoom.items)): #check for valid items
                if (noun == currentRoom.items[i]):
                    #item is found, set response to description
                    response = currentRoom.itemDescriptions[i]
                    break
        #verb is "grab"
        elif (verb == "grab"):
            response = "I don't see that item." #default response
            for grabbable in currentRoom.grabbables:  #check for valid grab.
                if (noun == grabbable):
                    #grabbable is found, add to inventory & remove from room
                    inventory.append(grabbable)
                    currentRoom.delGrabbables(grabbable)
                    response = "Item grabbed"
                    break
        #ADD USE VERB
        elif (verb == "use"):
            response = "Invalid action"
            for useable in currentRoom.useables:
                if (noun == "key"):
                    response = "There's a code-3421. Might want to grab it for later (grab code-3421)"
        
                elif (noun == "code-3421"):
                    response = "A secret exit has opened on the south wall"
                    currentRoom.exits.append("south")
                    currentRoom.exitLocations.append(escape)
                   
                    
                           
                
    #display response
    print("\n{}".format(response))
                    
                
            

