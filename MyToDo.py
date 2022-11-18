import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
import datetime
import pandas.io.common
import customtkinter

class Root(tk.Tk):
    def __init__(self):
        super(Root,self).__init__()
 
        self.title("DailyTask")
        self.minsize(1366,768)
        self.resizable(False, False)
        
        self.current_date = datetime.datetime.now()
        self.year = self.current_date.year
        self.month = self.current_date.month
        self.day = self.current_date.day
        try:
            self.MyToDoList = pd.read_csv("MyToDo.csv")
        except pd.errors.EmptyDataError:
            self.MyToDoList = pd.DataFrame({'date': '{0}-{1}-{2}'.format(self.year, 
                                                        self.month, self.day)}, index=[0])
            self.MyToDoList.to_csv("MyToDo.csv", index=False)
        print(self.MyToDoList)
        self.MyToDoColumns = list(self.MyToDoList.columns)
        
        #self.second_frame = self.CreateNewCanvasFrame(self)
        
    def CreateNewCanvasFrame(self, root):
        self.my_canvas = tk.Canvas(root, bg="black")
        
        my_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self. my_canvas.configure(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))
        
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        second_frame = tk.Frame(self.my_canvas, bg="black")
        
        self.my_canvas.create_window((0,0), window=second_frame, anchor="nw", tags="my_tag")
        
        self.my_canvas.itemconfigure("my_tag", width=1366)
        
        return second_frame
    
    def AddButtons(self, root):
        topFrame = self.CreateNewCanvasFrame(root)
        self.ButtonToAddTasks(topFrame)
        self.ButtonToDeleteTasks(topFrame)
        self.ButtonToUpdateTasks(topFrame)
        self.ButtonToAnalyse(topFrame)
        self.ButtonForLastDaysData(topFrame)
        self.TodaysDate(topFrame)
        
        self.ShowTheList(topFrame, True)
        
    
    def ButtonToAddTasks(self, root):
        B = customtkinter.CTkButton(master=root, text="Add New Tasks", command=lambda:self.OpenNewWindowForTasks(root))
        B.place(relx = 0.95,
                 rely = 0.0,
                 anchor ='ne')
        
    def ButtonToDeleteTasks(self, root):
        B =customtkinter.CTkButton(master=root, text="Delete Tasks", command=lambda:self.OpenNewWindowForDeletingTasks(root))
        B.place(relx = 0.80,
                  rely = 0.0,
                  anchor ='ne')

    def ButtonToUpdateTasks(self, root):
        B = customtkinter.CTkButton(root, text="Update Tasks", command=lambda:self.OpenNewWindowForUpdatingTasks(root))
        B.place(relx = 0.65,
                  rely = 0.0,
                  anchor ='ne')

    def ButtonToAnalyse(self, root):
        B = customtkinter.CTkButton(master=root, text="Analyse Me", command=lambda:self.OpenNewWindowAnalysing(root))
        B.place(relx = 0.50,
                  rely = 0.0,
                  anchor ='ne')
        
    def ButtonForLastDaysData(self, root):
        B = customtkinter.CTkButton(master=root, text="Update Last Day Data", command=lambda:self.UpdateLastDayData(root))
        B.place(relx = 0.35,
                      rely = 0.0,
                      anchor ='ne')
        
    def UpdateLastDayData(self, root):
        newWindow = tk.Toplevel(root)
        newWindow.title("Last Day Data")
        newWindow.geometry("600x600")
        newWindow.resizable(False, False)
        
        second_frame = self.CreateNewCanvasForAnalysingUpdatingAndDeleting(newWindow, 600)
        try:
            row = self.MyToDoList.iloc[-2, :].dropna()
            tk.Label(second_frame, text="Date : {}".format(row[0]), font=("Times New Roman bold", 16)).pack()
            column_names = row.index
            
            chekcBoxVariableList, checkBoxList = [], []
            for i in range(1, len(row)):
                ct = [random.randrange(256) for x in range(3)]
                brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
                ct_hex = "%02x%02x%02x" % tuple(ct)
                bg_colour = '#' + "".join(ct_hex)

                taskLabel = tk.Label(second_frame,
                                  text=column_names[i],
                                 fg='White' if brightness < 120 else 'Black', 
                                    bg=bg_colour,
                                    font=("Arial", 15))

                taskLabel.pack(fill="both")
                chekcBoxVariableList.append(tk.IntVar())
                checkBox = tk.Checkbutton(second_frame, variable=chekcBoxVariableList[i-1], command=lambda e=i: SentSelection(e))
                if row[i] == 1:
                    checkBox.select()

                checkBox.pack(side=tk.TOP, expand=1, pady=(0, 25))
                checkBoxList.append(checkBox)
            
        except IndexError as e:
            tk.Label(second_frame, text="You have not entered a data last day!", font=("Times New Roman bold", 16)).pack()
            
        def SentSelection(e):
            newSelectionList = {'date': row[0]}
            for i, k in zip(chekcBoxVariableList, column_names[1:]):
                newSelectionList[k] = i.get()

            print("new : ", newSelectionList)
            self.MyToDoList.iloc[-2, :] = newSelectionList
            self.MyToDoList.to_csv("MyToDo.csv", index=False)
        
    def OpenNewWindowAnalysing(self, root):
        newWindow = tk.Toplevel(root)
        newWindow.title("Analysis")
        newWindow.geometry("600x600")
        newWindow.resizable(False, False)
        
        second_frame = self.CreateNewCanvasForAnalysingUpdatingAndDeleting(newWindow, 600, True)
        second_frame.config(bg="green")
        
        dfRowCount = self.MyToDoList.shape[0]
        print(dfRowCount)
        print(len(self.MyToDoColumns))
        
        if dfRowCount == 1:
            tk.Label(second_frame, text="You have no data!", font=("Times New Roman bold", 16), bg="green", fg="yellow").pack()
            return
        
        self.AnalyseLastDay(second_frame)
        
        if dfRowCount <= 15:
            self.AnalyseFifteenAndThirtyBoth(second_frame, dfRowCount)
            
        elif 15 < dfRowCount <= 30:
            self.AnalyseFifteenLowerThirty(second_frame, dfRowCount)
            
        else:
            self.AnalyseThirtyUpperThirty(second_frame, dfRowCount)
            
    def AnalyseLastDay(self, second_frame):
        lastDayData = self.MyToDoList.iloc[-2, :]
        lastDayCompletedDict = {}
        print("\n")
        for i in range(len(lastDayData[lastDayData == 1])):
            lastDayCompletedDict[lastDayData[lastDayData == 1].keys()[i]] = 1
            
        tk.Label(second_frame, text="-----Your last day data-----", font=("Times New Roman bold", 16), fg="#9ACD32", bg="green").pack()
        oneDayLabel = tk.Label(second_frame, text="You have completed {}/{} tasks yesterday.".format(len(lastDayCompletedDict), 
                            len(self.MyToDoColumns) - lastDayData.isna().sum() - 1), font=("Times New Roman", 13), fg="green", bg="yellow")
        oneDayLabel.pack(fill="both")
    
    def AnalyseFifteenAndThirtyBoth(self, second_frame, dfRowCount):
        tk.Label(second_frame, text="-----Your Data of Last Fifteen Days-----", font=("Times New Roman bold", 16), fg="#9ACD32", bg="green").pack()
        rowStr, addedTaskCountText="", ""
        lastDayAddedTaskCount = 0
        for i in range(dfRowCount-1):
            row = self.MyToDoList.iloc[i, :]

            thatDayCompletedDict = {}
            todayTaskCount = len(self.MyToDoColumns) - row.isna().sum() - 1
            for j in range(len(row[row == 1])):
                thatDayCompletedDict[row[row == 1].keys()[j]] = 1

            rowStr += "You have completed {}/{} tasks {} days ago. ({})\n".format(len(thatDayCompletedDict), 
                        todayTaskCount, dfRowCount - (i + 1), row['date'])
            addedTaskCountText += "You have added {} tasks {} days ago. ({})\n".format(todayTaskCount - lastDayAddedTaskCount, 
                                                                            dfRowCount - (i + 1), row['date'])
            lastDayAddedTaskCount = todayTaskCount
        fifteenDaysLabel = tk.Label(second_frame, text=rowStr, font=("Times New Roman", 13), fg="green", bg="yellow")
        fifteenDaysLabel.pack(fill="both")
        
        tk.Label(second_frame, text="\n", bg="green").pack(fill="both")
        
        addedTasksPerDaysLabel = tk.Label(second_frame, text=addedTaskCountText, font=("Times New Roman", 13), fg="green", bg="yellow")
        addedTasksPerDaysLabel.pack(fill="both")
        
        tk.Label(second_frame, text="-----Your Data of Last Thirty Days-----", font=("Times New Roman bold", 16), fg="#9ACD32", bg="green").pack()
        
        thirtyDaysLabel = tk.Label(second_frame, text=rowStr, font=("Times New Roman", 13), fg="green", bg="yellow")
        thirtyDaysLabel.pack(fill="both")
        
        tk.Label(second_frame, text="\n", bg="green").pack(fill="both")
        
        addedTasksPerDaysLabelThirty = tk.Label(second_frame, text=addedTaskCountText, font=("Times New Roman", 13), fg="green", bg="yellow")
        addedTasksPerDaysLabelThirty.pack(fill="both")
    
    def AnalyseFifteenLowerThirty(self, second_frame, dfRowCount):
        self.AnalyseFifteen(second_frame, dfRowCount)
        
        tk.Label(second_frame, text="-----Your Data of Last Thirty Days-----", font=("Times New Roman bold", 16), fg="#9ACD32", bg="green").pack()
        
        rowStr, addedTaskCountText="", ""
        lastDayAddedTaskCount = 0
        for i in range(dfRowCount-1):
            row = self.MyToDoList.iloc[i, :]

            thatDayCompletedDict = {}
            todayTaskCount = len(self.MyToDoColumns) - row.isna().sum() - 1
            for j in range(len(row[row == 1])):
                thatDayCompletedDict[row[row == 1].keys()[j]] = 1

            rowStr += "You have completed {}/{} tasks {} days ago. ({})\n".format(len(thatDayCompletedDict), 
                        todayTaskCount, dfRowCount - (i + 1), row['date'])
            addedTaskCountText += "You have added {} tasks {} days ago. ({})\n".format(todayTaskCount - lastDayAddedTaskCount, 
                                                                            dfRowCount - (i + 1), row['date'])
            lastDayAddedTaskCount = todayTaskCount
        thirtyDaysLabel = tk.Label(second_frame, text=rowStr, font=("Times New Roman", 13), fg="green", bg="yellow")
        thirtyDaysLabel.pack(fill="both")
        
        tk.Label(second_frame, text="\n", bg="green").pack(fill="both")
        
        addedTasksPerDaysLabelThirty = tk.Label(second_frame, text=addedTaskCountText, font=("Times New Roman", 13), fg="green", bg="yellow")
        addedTasksPerDaysLabelThirty.pack(fill="both")
        
    def AnalyseFifteen(self, second_frame, dfRowCount):
        tk.Label(second_frame, text="-----Your Data of Last Fifteen Days-----", font=("Times New Roman bold", 16), fg="#9ACD32", bg="green").pack()
        rowStr, addedTaskCountText="", ""
        lastDayAddedTaskCount = 0
        for i in range(16, 1, -1):
            row = self.MyToDoList.iloc[-i, :]
            
            thatDayCompletedDict = {}
            todayTaskCount = len(self.MyToDoColumns) - row.isna().sum() - 1
            for j in range(len(row[row == 1])):
                thatDayCompletedDict[row[row == 1].keys()[j]] = 1

            rowStr += "You have completed {}/{} tasks {} days ago. ({})\n".format(len(thatDayCompletedDict), 
                        todayTaskCount,  i-1, row['date'])
            addedTaskCountText += "You have added {} tasks {} days ago. ({})\n".format(todayTaskCount - lastDayAddedTaskCount, 
                                                                            i-1, row['date'])
            lastDayAddedTaskCount = todayTaskCount
        fifteenDaysLabel = tk.Label(second_frame, text=rowStr, font=("Times New Roman", 13), fg="green", bg="yellow")
        fifteenDaysLabel.pack(fill="both")
        
        tk.Label(second_frame, text="\n", bg="green").pack(fill="both")
        
        addedTasksPerDaysLabel = tk.Label(second_frame, text=addedTaskCountText, font=("Times New Roman", 13), fg="green", bg="yellow")
        addedTasksPerDaysLabel.pack(fill="both")
        
    def AnalyseThirtyUpperThirty(self, second_frame, dfRowCount):
        self.AnalyseFifteen(second_frame, dfRowCount)
        
        tk.Label(second_frame, text="-----Your Data of Last Thirty Days-----", font=("Times New Roman bold", 16), fg="#9ACD32", bg="green").pack()
        rowStr, addedTaskCountText="", ""
        lastDayAddedTaskCount = 0
        for i in range(31, 1, -1):
            row = self.MyToDoList.iloc[-i, :]
            thatDayCompletedDict = {}
            todayTaskCount = len(self.MyToDoColumns) - row.isna().sum() - 1
            for j in range(len(row[row == 1])):
                thatDayCompletedDict[row[row == 1].keys()[j]] = 1

            rowStr += "You have completed {}/{} tasks {} days ago. ({})\n".format(len(thatDayCompletedDict), 
                        todayTaskCount,  i-1, row['date'])
            addedTaskCountText += "You have added {} tasks {} days ago. ({})\n".format(todayTaskCount - lastDayAddedTaskCount, 
                                                                            i-1, row['date'])
            lastDayAddedTaskCount = todayTaskCount
        fifteenDaysLabel = tk.Label(second_frame, text=rowStr, font=("Times New Roman", 13), fg="green", bg="yellow")
        fifteenDaysLabel.pack(fill="both")
        
        tk.Label(second_frame, text="\n", bg="green").pack(fill="both")
        
        addedTasksPerDaysLabel = tk.Label(second_frame, text=addedTaskCountText, font=("Times New Roman", 13), fg="green", bg="yellow")
        addedTasksPerDaysLabel.pack(fill="both")
        
    def OpenNewWindowForUpdatingTasks(self, root):
        newWindow = tk.Toplevel(root)
        newWindow.title("Update Tasks")
        newWindow.geometry("400x400")
        newWindow.resizable(False, False)
        
        second_frame = self.CreateNewCanvasForAnalysingUpdatingAndDeleting(newWindow, 400)
        
        labelHeader = tk.Label(second_frame, text= "Select the tasks you want to update", font=("Arial bold", 12))
        labelHeader.pack(pady=(10, 10))
        
        if self.CheckIfDataNull(): 
            tk.Label(second_frame, text="You have no data! Please add data first.", font=("Arial bold", 14)).pack()
            return
        
        def UpdateTasks(e):
            columnName = self.MyToDoColumns[e]
            
            self.MyToDoList.rename(columns={columnName: entryList[e-1].get()}, inplace=True)
            self.MyToDoList.to_csv("MyToDo.csv", index=False)
            
            root.bind('<Configure>', self.reset_scrollregion)
            
            self.ShowTheList(root, False, True)
            newWindow.destroy()
            
            return self.OpenNewWindowForUpdatingTasks(root)
        
        entryList = []
        for i in range(1, len(self.MyToDoColumns)):
            ct = [random.randrange(256) for x in range(3)]
            brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
            ct_hex = "%02x%02x%02x" % tuple(ct)
            bg_colour = '#' + "".join(ct_hex)
            
            taskLabel = tk.Label(second_frame,
                              text=self.MyToDoColumns[i],
                             fg='White' if brightness < 120 else 'Black', 
                                bg=bg_colour,
                                font=("Arial", 15))
            #taskLabel.place(x = 10, y = 0 + i*30, width=150, height=25)
            taskLabel.pack(fill="both", expand=1)
            
            updateEntry = tk.Entry(second_frame)
            #updateEntry.place(x = 250, y = 0 + i*30)
            updateEntry.pack(expand=1)
            entryList.append(updateEntry)
            
            updateButton = customtkinter.CTkButton(master=second_frame, text="Update " + str(i), command=lambda e=i: UpdateTasks(e))
            #updateButton.place(x = 300, y = 0 + i*30)
            updateButton.pack(side=tk.TOP, expand=1, pady=(0, 25))
        
    def OpenNewWindowForDeletingTasks(self, root):
        newWindow = tk.Toplevel(root)
        newWindow.title("Delete Tasks")
        newWindow.geometry("400x400")
        newWindow.resizable(False, False)
        
        second_frame = self.CreateNewCanvasForAnalysingUpdatingAndDeleting(newWindow, 400)
        
        labelHeader = tk.Label(second_frame, text= "Select the tasks you want to delete", font=("Arial bold", 12))
        labelHeader.pack(pady=(10, 10))

        if self.CheckIfDataNull(): 
            tk.Label(second_frame, text="You have no data! Please add data first.", font=("Arial bold", 14)).pack()
            return
        
        def DeleteTasks(e):
            columnName = self.MyToDoColumns[e]
            del self.MyToDoColumns[e]
            
            self.MyToDoList = self.MyToDoList.drop([columnName], axis=1)
            self.MyToDoList.to_csv("MyToDo.csv", index=False)
            
            root.bind('<Configure>', self.reset_scrollregion)
            
            self.ShowTheList(root, False, True)
            newWindow.destroy()
            
            return self.OpenNewWindowForDeletingTasks(root)
        
        for i in range(1, len(self.MyToDoColumns)):
            ct = [random.randrange(256) for x in range(3)]
            brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
            ct_hex = "%02x%02x%02x" % tuple(ct)
            bg_colour = '#' + "".join(ct_hex)
            
            taskLabel = tk.Label(second_frame,
                              text=self.MyToDoColumns[i],
                             fg='White' if brightness < 120 else 'Black', 
                                bg=bg_colour,
                                font=("Arial", 15))
            #taskLabel.place(x = 10, y = 0 + i*30, width=150, height=25)
            taskLabel.pack(fill="both", expand=1)
        
            
            deleteButton = customtkinter.CTkButton(master=second_frame, text="Delete " + str(i), command=lambda e=i: DeleteTasks(e))
            deleteButton.pack(side=tk.TOP, expand=1, pady=(0, 25))

    def CheckIfDataNull(self):
        return len(self.MyToDoColumns) == 1

    def CreateNewCanvasForAnalysingUpdatingAndDeleting(self, newWindow, width, comingFromAnalyse=False):
        
        my_canvas = tk.Canvas(newWindow)
        if comingFromAnalyse:
            my_canvas.configure(bg="green")
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        my_scrollbar = tk.Scrollbar(newWindow, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = tk.Frame(my_canvas)

        my_canvas.create_window((0,0), window=second_frame, anchor="nw", tags="my_tag")
        
        my_canvas.itemconfigure("my_tag", width=width)
        return second_frame
        
    def OpenNewWindowForTasks(self, root):
        newWindow = tk.Toplevel(root, bg="black")
        newWindow.title("Add New Tasks")
        newWindow.geometry("300x300")
        newWindow.resizable(False, False)

        label = tk.Label(newWindow,
              text ="How many tasks do you want to add?", bg="black", fg="white", font=("Arial", 13))
        label.pack()
        
        entryTaskNumber = tk.Entry(newWindow)
        entryTaskNumber.pack()
        
        enterEntryButton = customtkinter.CTkButton(master=newWindow, text="Enter", command=lambda:self.AddNewTasks(root, newWindow, entryTaskNumber, enterEntryButton, label))
       # enterEntryButton.bind("<Button>", lambda e: self.AddNewTasks(root, newWindow, entryTaskNumber, enterEntryButton, label))
        enterEntryButton.pack()
    
    def AddNewTasks(self, root, newWindow, entryTaskNumber, enterEntryButton, label):
        countNumber = entryTaskNumber.get()
        
        try: 
            countNumber = int(countNumber)
            entryTaskNumber.pack_forget()
            enterEntryButton.pack_forget()
            label.pack_forget()
            
        except ValueError:
            messagebox.showerror('String Error!', 'Error: This value can not be converted to an Integer!')
            return newWindow.destroy()
        
        if countNumber <= 0:
            messagebox.showerror('Wrong Number!', 'Error: This value can not be lower than or equal to zero!!')
            return newWindow.destroy()
        
        labelTaskName = tk.Label(newWindow,
              text ="Enter 1. task name", bg="black", fg="white", font=("Arial", 13))
        labelTaskName.pack()
        
        entryTaskName = tk.Entry(newWindow)
        entryTaskName.pack()
        
        buttonClickedCount = 0
        
        def SetGlobalVariable():
            global buttonClickedCount
            buttonClickedCount = 0
        
        def ChangeLabelValue():
            global buttonClickedCount
            
            if buttonClickedCount < countNumber:
                writtenTask = entryTaskName.get()
                entryTaskName.delete(0, tk.END)
                
                if writtenTask not in self.MyToDoColumns:
                    self.MyToDoColumns.append(writtenTask)
                    newColumn = []
                    for i in range(len(self.MyToDoList.index) - 1):
                        newColumn.append("NaN")
                    newColumn.append(0)
                    self.MyToDoList[writtenTask] = newColumn
                    print(self.MyToDoList)
                    self.MyToDoList.to_csv("MyToDo.csv", index=False)
                else:
                    messagebox.showerror("You've already added!", 
                                         "Error: You have already added this task!")
                    root.bind('<Configure>', self.reset_scrollregion)
                    return self.ShowTheList(root, False, True)
                print(self.MyToDoColumns)
                buttonClickedCount += 1 
                
            if buttonClickedCount == countNumber:
                root.bind('<Configure>', self.reset_scrollregion)
                self.ShowTheList(root, False, True)
                return newWindow.destroy()
            
            labelTaskName.config(text="Enter {}. task name".format(buttonClickedCount + 1), bg="black", fg="white", font=("Arial", 13))
            
        SetGlobalVariable()
        
        enterTaskNameButton = customtkinter.CTkButton(master=newWindow, text="Add", command=lambda:ChangeLabelValue())
        enterTaskNameButton.pack()
        
    def ShowTheList(self, root, createdFirstTime, remakeList=False):
        headerLabel = tk.Label(root, text= "My Tasks For Today", font=("Arial", 25), bg="black", fg="white")
        #headerLabel.place(x=300, y=75, anchor='center')
        headerLabel.pack(side="top", pady=(35, 5))
        if createdFirstTime:
            lastdate = self.MyToDoList['date'].iloc[-1]
            if not self.CheckIfTomorrowBegins(self.day, lastdate.split("-")[-1]) and not (self.MyToDoList['date'] == "{}-{}-{}".format(self.year, self.month, self.day)).any(): 
                newDate = "{}-{}-{}".format(self.year, self.month, self.day)
                newDateList = {'date': newDate}
                for i in self.MyToDoList.columns[1:]:
                    newDateList[i] = 0
                
                self.MyToDoList = self.MyToDoList.append(newDateList, ignore_index=True)
                self.MyToDoColumns = list(self.MyToDoList.columns)
                self.MyToDoList.to_csv("MyToDo.csv", index=False)
            self.ListWidgets(root)
                
        elif remakeList:
            for widget in root.winfo_children():
               # print(str(widget))
                if (str(widget).startswith(".!canvas.!frame.!checkbutton") or str(widget).startswith(".!canvas.!frame.!label")) and (str(widget) != ".!canvas.!frame.!label" and str(widget) != ".!canvas.!frame.!label2"):
                    widget.destroy()
            self.MyToDoColumns = list(self.MyToDoList.columns)
            self.ListWidgets(root)
            
            
    def ListWidgets(self, root):
        if self.CheckIfDataNull(): 
            tk.Label(root, text="You have no data! Please add data first", font=("Arial bold", 16), bg="black", fg="#1f6aa5").pack()
            return       
        getTodaysValues = self.MyToDoList.iloc[-1]
        createTodaysDict = {i : getTodaysValues[i] for i in getTodaysValues.index}
            
        def SentSelection(e):
            newSelectionList = {'date': getTodaysValues[0]}
            for i, k in zip(chekcBoxVariableList, self.MyToDoList.columns[1:]):
                newSelectionList[k] = i.get()

            print("new : ", newSelectionList)
            self.MyToDoList.iloc[-1, :] = newSelectionList
            self.MyToDoColumns = list(newSelectionList.keys())
            self.MyToDoList.to_csv("MyToDo.csv", index=False)
                
        
        checkBoxList = []
        chekcBoxVariableList = []
        print(self.MyToDoColumns)
        for i in range(1, len(self.MyToDoColumns)):
            bg_colour = "#41c55f"
            taskLabel = tk.Label(root,
                              text=self.MyToDoColumns[i],
                             fg='white', 
                                bg="#1f6aa5",
                                font=("Arial", 15))
            #taskLabel.place(x = 30, y = 110 + i*30, width=450, height=25)
            taskLabel.pack(fill="both")
            chekcBoxVariableList.append(tk.IntVar())
            checkBox = tk.Checkbutton(root, variable=chekcBoxVariableList[i-1], command=lambda e=i: SentSelection(e))
            if self.MyToDoList.iloc[-1, i] == 1:
                checkBox.select()
            #checkBox.place(x = 500, y = 110 + i*30)
            checkBox.pack(side=tk.TOP, expand=1, pady=(0, 25))
            checkBoxList.append(checkBox)
            
    def TodaysDate(self, root):
        hour = self.current_date.hour
        minute = self.current_date.minute
        
        dateLabel = tk.Label(root, text="Today's Date is: {0}-{1}-{2} {3}-{4}".format(self.year, self.month, 
                                                    self.day, hour, minute), font=("Arial", 13), fg="white", bg="black")
        dateLabel.place(relx = 0.20,
                  rely = 0.0,
                  anchor ='ne')

    def CheckIfTomorrowBegins(self, day, lastday):
        return day == int(lastday)

    def reset_scrollregion(self, event):
        self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all"))
                                 

root = Root()
root.AddButtons(root)
root.mainloop()