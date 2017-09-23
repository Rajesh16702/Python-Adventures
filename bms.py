from bs4 import BeautifulSoup
import requests
import time
from tkinter import messagebox


def check():
	doc = requests.get("https://in.bookmyshow.com/buytickets/spyder-hyderabad/movie-hyd-ET00055827-MT/20170927")
	soup = BeautifulSoup(doc.text,"html.parser")
	data = soup.find(id='venuelist')
	return data.text

if __name__ == "__main__":
	for i in range(1000):
		old = " "
		new = " "
		old = check()
		time.sleep(6)
		new = check()
		if old == new:
			print("It's the same Bro!!")
		else:
			if "PVR: Inorbit, Cyberabad" in new :
				messagebox.showinfo("Book Tickets", "Hurry Up!!")
				print("Book Bro!!")

