from bs4 import BeautifulSoup
from requests import get

Bp = BeautifulSoup(get("https://www.time.ir/").content, "html.parser")

class Datefa:
	def __init__(self, beautisoup = Bp):
		self.beup = beautisoup

	def TodayFull(self):
		return self.beup.find(id = "ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsiNumeral").text
	
	def TodayFullCar(self):
		return self.beup.find(id = "ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsi").text
		
	def Dateint(self):
		todayfull = self.TodayFull()
		return todayfull.split("/")
	
	def Datecar(self):
		todayfullcar = self.TodayFullCar()
		return todayfullcar.split(" ")
		
	def TodayCar(self):
	   if self.Datecar()[0] == 'پنج':
	       return  self.Datecar()[0] + self.Datecar()[1]
	       
	   if self.Datecar()[0] == 'چهارشنبه':
	       return  'چهارشنبه'
	   
	   if self.Datecar()[0] == 'سه':
	       return self.Datecar()[0] + self.Datecar()[1]
	   
	   if self.Datecar()[0] == 'دو':
	       return self.Datecar()[0] + self.Datecar()[1]
	   
	   if self.Datecar()[0] == 'یک':
	       return self.Datecar()[0] + self.Datecar()[1]
	   
	   if self.Datecar()[0] == 'شنبه':
	       return self.Datecar()[0]
	   
	   if self.Datecar()[0] == 'جمعه':
	   	return self.Datecar()[0]
	   	
	def Dateyear(self):
		return self.Dateint()[0]
	
	def Datemonth(self):
		return self.Dateint()[1]
	
	def Dateday(self):
		return self.Dateint()[2]
	
	def Monthcar(self):
		return self.Datecar()[4]