import requests
import bs4
import tkinter as tk

def get_html_data(url):
    data=requests.get(url)
    return data
def get_covid_data():
    url="https://www.worldometers.info/coronavirus/"
    html_data=get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div=bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
    all_data=""
    for block in info_div:
        text=block.find("h1",class_=None).get_text()
        totalcount=block.find("span",class_=None).get_text()
        all_data=all_data+text+" "+totalcount+"\n"
    return all_data
get_covid_data()
#Getting Country Wise Data Covid Cases#
def get_country_data():
    name=textfield.get()
    url="https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""
    for block in info_div:
        for i in range(3):
            text = info_div[i].find("h1", class_=None).get_text()
        totalcount = info_div[i].find("span", class_=None).get_text()
        all_data = all_data + text + " " + totalcount + "\n"
    mainlabel['text']=all_data

#Reloading The Data From The Server#
def reload():
    newdata=get_covid_data()
    mainlabel['text']=newdata

# Making a GUI(GRAPHICAL USER INTERFACE) using tkinter library #
root=tk.Tk()
root.geometry("800x700")
root.title("Covid-19 Tracker App")
f=("poppins",25,"bold")#Making a function & giving a font-famiily,font-size,font-weight to our GUI#

banner=tk.PhotoImage(file="COVID-Icons-01.png")
bannerlabel=tk.Label(root,image=banner)
bannerlabel.pack()

textfield=tk.Entry(root,width=50)
textfield.pack()

mainlabel=tk.Label(root,text=get_covid_data(),font=f)
mainlabel.pack()

#Making A Get Data Button#
getdatabutton=tk.Button(root,text="Get Data",font=f,relief='solid',command=get_country_data)
getdatabutton.pack()

#Making A Reload Buttons#
reloadbutton=tk.Button(root,text="Reload",font=f,relief='solid',command=reload,)
reloadbutton.pack()

root.mainloop()