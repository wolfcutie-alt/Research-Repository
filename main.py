#import
from tkinter import *
from tkinter import messagebox

#Background Code
class Event:
    def __init__(self, event_name, event_type, pohutukawa_point, kauri_point, kowhai_point, rimu_point):
        self.name = event_name
        self.type = event_type
        self.pohutukawa_point = pohutukawa_point
        self.kauri_point = kauri_point
        self.kowhai_point = kowhai_point
        self.rimu_point = rimu_point
        eventObject.append(self)
        eventNames.append(event_name)
        pohutukawaPoint.append(pohutukawa_point)
        kauriPoint.append(kauri_point)
        kowhaiPoint.append(kowhai_point)
        rimuPoint.append(rimu_point)
        
        self.totalPohutukawaPoint = sum(pohutukawaPoint)
        self.totalKauriPoint = sum(kauriPoint)
        self.totalKowhaiPoint = sum(kowhaiPoint)
        self.totalRimuPoint = sum(rimuPoint)
        
        self.winner = max(self.totalPohutukawaPoint, self.totalKauriPoint, self.totalKowhaiPoint, self.totalRimuPoint)

    def printLeaderboard(self):
        return f"The Leaderboard is {self.winner}. Score of 4 Houses: \n 1.Pohutukawa Score: {self.totalPohutukawaPoint},\n 2.Kauri Score: {self.totalKauriPoint},\n 3.Kowhai Score: {self.totalKowhaiPoint},\n 4.Rimu Score: {self.totalRimuPoint}" 

    def type(self):
        if self.type == True:
            self.type = False
        else:
            self.type = True
        return self.type

#Set up Objects and Lists for the program
eventObject = []
eventNames = []
pohutukawaPoint = []
kauriPoint = []
kowhaiPoint = []
rimuPoint = []



event1 = Event("Lampada Games", True, 75, 60, 72, 68)
event2 = Event("House Trivia", False, 66, 68, 74, 73)

#GUI

#GUI functions
def makeSuccessBox():
    messagebox.showinfo("Success,", "Yay you successfully added new event")

def makeFailureBox():
    messagebox.showinfo("Failure", "Unable to added new event: check your input and try again")

#The function below checks if any of the input wrong data type, if yes then the function will return false else it'll return true 
#This function will be used later to check the validity of the user input
def makeNewEvent():
    if nameEntry.get() == "":
        return False
    if pohutukawaPointEntry.get().isdigit() == False: 
        if pohutukawaPointEntry.get().isdigit() > 100:
            return False
    if kauriPointEntry.get().isdigit() == False: 
        if kauriPointEntry.get().isdigit() > 100:
            return False
    if kowhaiPointEntry.get().isdigit() == False:
        if kowhaiPointEntry.get().isdigit() > 100:
            return False
    if rimuPointEntry.get().isdigit() == False: 
        if rimuPointEntry.get().isdigit() > 100:
            return False
    if typeEntry.get() != "Yes" and typeEntry.get() != "No":
        return False
    isSport = True
    if typeEntry.get() == "No":
        isSport = False
    newEvent = Event(nameEntry.get(), isSport, int(pohutukawaPointEntry.get()), int(kauriPointEntry.get()), int(kowhaiPointEntry.get()), int(rimuPointEntry.get()))
    #refreshCarChoiceMenu()
    addNewEventToMenu(newEvent)
    return True

def tryToMakeEvent():
    if makeNewEvent() == False:
        makeFailureBox()
    else:
        makeSuccessBox()

#This function holds the necessary code to display the leaderboard of the house competition
def displayLeaderboard():
    for event in eventObject:
        if selectedEvent.get() == event.name:
            messagebox.showinfo("The Leaderboard is: !", event.printLeaderboard())

def refreshEventChoiceMenu():
    #Go to the eventChoice OptionMenu and delete all of the current options
    eventChoice.children["menu"].delete(0, "end")
    #for every option in the eventNames list, add it to the OptionMenu
    for event in eventNames:
        eventChoice.children["menu"].add_command(label=event, command=lambda: selectedEvent.set(event))

#Add a new event to the eventChoice OptionMenu
def addNewEventToMenu(event):
    #eventChoice.children["menu"].add_command(label=event.name, command=selectedEvent.set(event.name))
    eventChoice.children["menu"].add_command(label=event.name, command=lambda: selectedEvent.set(event.name))

#GUI widgets
root = Tk()
root.title("House Event Calculator")

#Make a place for the user to enter a new event info
nameLabel = Label(root, text="Name: ")
nameLabel.pack()
nameEntry = Entry(root)
nameEntry.pack()

typeLabel = Label(root, text="Enter \"Yes\" if the event is sport or \"No\" if the new event is not sport")
typeLabel.pack()
typeEntry = Entry(root)
typeEntry.pack()

pohutukawaPointLabel = Label(root, text="Pohutukawa Points: ")
pohutukawaPointLabel.pack()
pohutukawaPointEntry = Entry(root)
pohutukawaPointEntry.pack()

kauriPointLabel = Label(root, text="Kauri Points: ")
kauriPointLabel.pack()
kauriPointEntry = Entry(root)
kauriPointEntry.pack()

kowhaiPointLabel = Label(root, text="Kowhai Points: ")
kowhaiPointLabel.pack()
kowhaiPointEntry = Entry(root)
kowhaiPointEntry.pack()

rimuPointLabel = Label(root, text="Rimu Points: ")
rimuPointLabel.pack()
rimuPointEntry = Entry(root)
rimuPointEntry.pack()

addNewEventButton = Button(root, text="Add New Event", command=tryToMakeEvent)
addNewEventButton.pack()

selectedEvent = StringVar()

eventChoice = OptionMenu(root, selectedEvent, *eventNames)
eventChoice.pack()

leaderBoardButton = Button(root, text="The Leaderboard is: ", command=displayLeaderboard)
leaderBoardButton.pack()

#Run the program
root.mainloop()