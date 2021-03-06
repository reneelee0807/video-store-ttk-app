import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as tkscrolled
from videoStoreController import VideoStoreController

videoStore = VideoStoreController()

#  read customer data from the file and insert them into the list box
def readCustomerData():     
    file = open("Customer.txt", "r")
    lines = file.readlines()
    for index, line in enumerate(lines):
        (name, city, payment) = tuple(line.strip().split(','))
        videoStore.addCustomerIntoCustomerList(name, city, payment)
        lstbox_customers.insert(tk.END, name)
    file.close()

#  read video data from the file and insert them into the list box
def readVideoData():     
    file = open("Video.txt", "r")
    lines = file.readlines()
    for index, line in enumerate(lines):
        (title, year, status) = tuple(line.strip().split(','))
        videoStore.addVideoIntoVideoList(title, year, status)
        lstbox_videos.insert(tk.END, title)
    file.close()

# get selected customer name if it is available otherwise display a warning
def getSelectedCustomerName():
    selCustomerIndex = lstbox_customers.curselection()
    if not selCustomerIndex:
        showWarning('Please select a customer')
    else:
        return lstbox_customers.get(selCustomerIndex)

# get selected video name if it is available otherwise display a warning
def getSelectedVideoTitle():
    selVideoIndex = lstbox_videos.curselection()
    if not selVideoIndex:
        showWarning('Please select a movie')
    else:
        return lstbox_videos.get(selVideoIndex)

# handle the video rental if customer and video are selected otherwise display a warning
def rentVideo():
    selectedCustomerName = getSelectedCustomerName()
    selectedVideoTitle = getSelectedVideoTitle()
    if selectedCustomerName and selectedVideoTitle:
        videoIsRented = videoStore.rentVideo(selectedCustomerName, selectedVideoTitle)
        if videoIsRented:
            showInfo(f'{selectedCustomerName} successfully rent {selectedVideoTitle}. Rental Fee $10 is paid')
        else:
            showWarning(f'Sorry, {selectedVideoTitle} has been rented by someone else.')


# handle the video return if customer and video are selected otherwise display a warning
def returnVideo():
    selectedCustomerName = getSelectedCustomerName()
    selectedVideoTitle = getSelectedVideoTitle()
    if selectedCustomerName and selectedVideoTitle:
        videoIsReturned = videoStore.returnVideo(selectedCustomerName, selectedVideoTitle)
        if videoIsReturned:
            showInfo(f'{selectedCustomerName} successfully return {selectedVideoTitle}.')
        else:
            showWarning(f'Sorry, {selectedVideoTitle} was not rented by {selectedCustomerName}')

# display selected customer details
def showCustomerDetail():
    text_customerDetail.delete(1.0,tk.END)
    selectedCustomerName = getSelectedCustomerName()  
    if selectedCustomerName:
        detail = videoStore.getCustomerDetail(selectedCustomerName)
        text_customerDetail.insert(tk.END, detail)

# display selected video details
def showVideoDetail():
    text_videoDetail.delete(1.0,tk.END)
    selectedVideoTitle = getSelectedVideoTitle()
    if selectedVideoTitle:
        detail = videoStore.getVideoDetail(selectedVideoTitle)
        text_videoDetail.insert(tk.END, detail)

def showInfo(message):
    tk.messagebox.showinfo("Info", message)

def showWarning(message):
    tk.messagebox.showwarning("Warning", message)


# root window
root = tk.Tk()
root.geometry('500x600')
root.resizable(width=False, height=False)
root.title('Lincoln Video Rentals')


# read customer and video files when the app is run
root.after_idle(readCustomerData)
root.after_idle(readVideoData)


#add the widgets
frm_customerAndVideoLabel= tk.Frame(relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_customerAndVideoLabel.pack(padx=25, pady=0)

#add the widgets
frm_customerAndVideoList= tk.Frame(relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_customerAndVideoList.pack(padx=25, pady=0)

# add the widgets for rent and return buttons
frm_rentAndReturnBtns= tk.Frame(relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_rentAndReturnBtns.pack(padx=25, pady=5)

# add the widgets for customer details
frm_customerDetail= tk.Frame(relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_customerDetail.pack(padx=25, pady=5)

# add the widgets for customer details
frm_videoDetail= tk.Frame(relief=tk.FLAT, borderwidth=3)
# Pack the frame into the window
frm_videoDetail.pack(padx=25, pady=5)


# Customers label for customers list 
customersSubTotal = tk.Label(master=frm_customerAndVideoLabel,text="Customer")
customersSubTotal.pack(fill='x', padx=10, pady=0,side=tk.LEFT)

# Video label for videos list 
videosSubTotal = tk.Label(master=frm_customerAndVideoLabel, text="Movie")
videosSubTotal.pack(fill='x', padx=95, pady=0,side=tk.LEFT)

# customers list 
lstbox_customers = tk.Listbox(master=frm_customerAndVideoList, exportselection=0, selectmode=tk.BROWSE)
lstbox_customers.pack(fill='x', padx=20, pady=0,side=tk.LEFT)

# videos list
lstbox_videos = tk.Listbox(master=frm_customerAndVideoList, exportselection=0, selectmode=tk.BROWSE)
lstbox_videos.pack(fill='x', padx=20, pady=0,side=tk.LEFT)

# Rent button
rentButton = ttk.Button(master=frm_rentAndReturnBtns,text="Rent",command=rentVideo)
rentButton.pack(fill='x', padx=5, pady=5, side=tk.LEFT)

# Return button
returnButton = ttk.Button(master=frm_rentAndReturnBtns,text="Return",command=returnVideo)
returnButton.pack(fill='x', padx=5, pady=5, side=tk.LEFT)

# Customer detail button
customerDetailButton = ttk.Button(master=frm_customerDetail,text="Customer Detail",command=showCustomerDetail)
customerDetailButton.pack(fill='x', padx=5, pady=5, side=tk.LEFT)

# Customer detail scrollable text box
text_customerDetail = tkscrolled.ScrolledText(master=frm_customerDetail, width=35, height=10, wrap='word')
text_customerDetail.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

# movie detail button
videoDetailButton = ttk.Button(master=frm_videoDetail,text="Movie Detail",command=showVideoDetail)
videoDetailButton.pack(fill='x', padx=5, pady=5, side=tk.LEFT)

# Customer detail scrollable text box
text_videoDetail = tk.Text(master=frm_videoDetail, width=35, height=5)
text_videoDetail.pack(fill='x', padx=20, pady=5,side=tk.LEFT)

root.mainloop()
