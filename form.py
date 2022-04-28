from tkinter import  *
from tkinter import ttk
import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

#window = Tk()
#window.title("test")
#window.geometry("650x600")
#window.configure(background = "cyan")

list_of_Holdings = ['WPP',
'Publicis groupe',
'Interpublic Group',
'Omnicom']
list_of_HC_Networks = [
'BBDO WORLDWIDE',
'MCCANN WORLDGROUP',
'OGILVY',
'TBWA WORLDWIDE',
'DDB WORLDWIDE',
'GREY/AKQA',
'VMLY&R',
'PUBLICIS WORLDWIDE',
'DENTSU',
'WUNDERMAN THOMPSON',
'FCB',
'MULLENLOWE GROUP',
'LEO BURNETT',
'HAVAS CREATIVE',
'SAATCHI & SAATCHI']
list_of_indy =[
'SERVICEPLAN AGENTURGRUPPE',
'EDELMAN',
'WIEDEN + KENNEDY',
'CHEIL WORLDWIDE',
'ACCENTURE INTERACTIVE',
'GOOGLE',
'DELOITTE',
]
list_of_clients = list_of_Holdings + list_of_HC_Networks + list_of_indy
print (type(list_of_clients))
print (list_of_clients[0])

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')



cursor = conn.cursor()
years = [2017, 2018, 2019]
short = [1, 'any']
prize = ['is nut null', 'any']
query2 = """SELECT ED.FestivalYear, ED.Advertiser, ED.short, ED.FestivalCode,ED.EntryTypeName,
      ED.AwardCountCode, ED.CategoryCode,  ed.CategorySubTypeID,
      CD.NetworkCode, cd.NetworkName,	CD.UltimateHoldingCompanyName, cd.GroupCompanyName, cd.Country, cd.GroupCompanyName, cd.coTown,
      ec.MediaDescription, ec.CategoryDescription 
      FROM ArchiveEntryData as ED
      inner Join [ArchiveCompanyData] as CD
      on ED.EntrantCompanyNo = CD.companyNo and ed.Festivalyear = cd.ArchiveYear
      inner join ArchiveEntryCategories as EC
      ON ec.FestivalCode = ed.FestivalCode COLLATE Latin1_General_CI_AI
      AND ec.FestivalYear = ed.FestivalYear
      AND ec.CategoryCode = ed.CategoryCode COLLATE Latin1_General_CI_AI
      AND ec.EntryTypeId = ed.EntryTypeId
      and ed.FestivalYear in {} 
      and ed.FESTIVALCODE IN ('CL', 'LE', 'LI', 'LH')
  --	and ed.AwardCountCode is not null""".format(*years)

df = pd.read_sql(query2, conn)

yearly_numbers = df.groupby("FestivalYear").size()
yearly_shortlisted = df[df["short"] == 1].groupby("FestivalYear").size()
yearly_awards = df[df["AwardCountCode"].notnull()].groupby("FestivalYear").size()


percentage_of_wins = yearly_awards/yearly_numbers
percentage_of_shorts = yearly_shortlisted / yearly_numbers

number_of_entries_per_year_and_town = df.groupby(["FestivalYear", "coTown"]).size()
number_of_short_per_year_and_town = df[df["short"] == 1].groupby(["FestivalYear", "coTown"]).size()
number_of_wins_per_year_and_town = df[df["AwardCountCode"].notnull()].groupby(["FestivalYear", "coTown"]).size()

types_of_wins_per_year =df[df["AwardCountCode"].notnull()].groupby(["FestivalYear","AwardCountCode"]).size()
for year in years:
    types_of_category = df[df["FestivalYear"] == year].groupby(["EntryTypeName"]).size().sort_values(ascending = False)
    print(types_of_category)
