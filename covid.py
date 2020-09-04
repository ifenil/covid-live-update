import requests
import bs4 
import tkinter as tk




def get_html_data(url):
	 data = requests.get(url)
	 return data

def get_corona_detail_india():
	url = "https://www.mohfw.gov.in/"
	html_data = get_html_data(url)
	bs = bs4.BeautifulSoup(html_data.text,'html.parser')
	all_detail=""
	info_div=bs.find_all("span",class_="mob-show")
	for block in info_div:
		if block.get_text() is not None:
			all_detail=all_detail+block.get_text()+"\n"
	return all_detail        

def refresh():
	redata=get_corona_detail_india()
	mainlabel['text']=redata

root=tk.Tk()

root.geometry("400x500")
root.iconbitmap("corona.jpg")						
root.title("corona data of india")
f=("poppins",20,"bold")


mainlabel=tk.Label(root,text=get_corona_detail_india(),font=f,relief='solid')
mainlabel.pack()

button=tk.Button(root,font=f,text='Refresh',command=refresh())
button.pack()

root.mainloop()