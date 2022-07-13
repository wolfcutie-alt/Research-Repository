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

    def printHousewinner(self):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        while self.pohutukawa_point:
            sum1 += self.pohutukawa_point
        while self.kauri_point:
            sum2 += self.kauri_point
        while self.kowhai_point:
            sum3 += self.kowhai_point
        while self.rimu_point:
            sum4 += self.rimu_point
        return max(sum1, sum2, sum3, sum4)

    def type(self):
        if self.type == True:
            self.type = False
        else:
            self.type = True
        return self.type

#Set up Objects and Lists for the program
eventObject = []
eventNames = []

event1 = Event("Lampada Games", True, 75, 60, 72, 68)
event2 = Event("House Trivia", False, 66, 68, 74, 73)
#GUI

#GUI functions
def makeSuccessBox():
    messagebox.showinfo("Success,", "Yay you successfully added new event")

def makeFailureBox():
    messagebox.showinfo("Failure", "Unable to added new event: check your input and try again")

def makeNewEvent():
    if nameEntry.get() == "":
        return False
    if pohutukawaPointEntry.get().isdigit() == False:
        return False
    if kauriPointEntry.get().isdigit() == False:
        return False
    if kowhaiPointEntry.get().isdigit() == False:
        return False
    if rimuPointEntry.get().isdigit() == False:
        return False
    if typeEntry.get() != "Yes" and typeEntry.get() != "No":
        return False
    isSport = True
    if typeEntry.get() == "No":
        isSport = False
    Event(nameEntry.get(), isSport, int(pohutukawaPointEntry.get()), int(kauriPointEntry.get()), int(kowhaiPointEntry.get()), int(rimuPointEntry.get()))
    return True
def tryToMakeEvent():
    if makeNewEvent() == False:
        makeFailureBox()
    else:
        makeSuccessBox()

def displayEventInfo():
    for event in eventObject:
        if selectedEvent.get() == event.name:
            messagebox.showinfo("The leaderboard of the house competition is: !", event.printHousewinner())

#GUI widgets
root = Tk()

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

eventInfoButton = Button(root, text="Print Event Info", command=displayEventInfo)
eventInfoButton.pack()

#Run the program
root.mainloop()