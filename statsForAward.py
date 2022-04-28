import copy

import pandas as pd

from imports import *


#
#input: a dataframe and a column based upon you want some analysis
#output, simple numbers and statistics on region(country/town/region), sectors(Sector/subsector), category discreption.
def getVariableName(variable):
    variableName =   f'{variable=}'.split('=')[0]

    return  variableName

def createExcel(series, name, writer, index):
    #my fucking god, what have I done here?
    #pretty sure it is not best practice...
    #if we have two columns we want to input/group by, it is being naturally as a list in the argumentsfor groupby
    #but not passed in the name of the spreadsheet. thats why I did thte following:
    if type(name) is not str:
        name = ''.join(name)
    ######    series.to_excel(writer, sheet_name=name)
    series.to_excel(writer, sheet_name=name, index=index)
    creatingPlotsAddingToExcel(series, name, writer)



    #plt.plot(series)
def creatingPlotsAddingToExcel(series, name,writer):
    figureNameBar = '{}bar.png'.format(name)
    #plt.savefig(figureNameBar)
    series.plot.bar()
    workbook = writer.book
    workSheet = writer.sheets[name]
    print('figureNameBar',figureNameBar)
    workSheet.insert_image("G2", figureNameBar)
    # figureNamePie = '{}pie.png'.format(name)
    # series.plot.pie()
    # poutsa.insert_image("P2",figureNamePie)


def allStatsForColumn(df,column, writer, index):
    columnStats = df.groupby(column)[["All Entries","Shortlist","Winner"]].count().sort_values(by ="All Entries", ascending=False)

    createExcel(columnStats, column, writer, index)

def allStatsForColumnByYear(df,column,writer, index):
    columnStats = df.groupby([column,"FestivalYear"])[["All Entries","Shortlist","Winner"]].count()\
        .sort_values(by ="All Entries", ascending=False) #todo: grouper based on function should reset index or not
    createExcel(columnStats, column, writer, index)

def allStatsForColumbGroupedByYear(df,column,writer,index):
    columnStats = df.groupby(["FestivalYear",column])[["All Entries","Shortlist","Winner"]].count()
    createExcel(columnStats,column,writer,index)

def createEntriesSheetsSustainability(dfSust,dfAll,column):
    sustainableEntries = dfSust.groupby(["FestivalYear", column])["Sustainability Entries"].size().groupby(
        "FestivalYear").size()
    allEntries = dfAll.groupby(["FestivalYear", column])["All Entries"].size().groupby("FestivalYear").size()
    listOfEntries = []

    for year in dfSust["FestivalYear"].unique():
        listOfEntries.append(dfSust[dfSust["FestivalYear"] == year][column].unique())

    dfListOfEntries = pd.DataFrame(listOfEntries).transpose().rename(columns={0: "2018", 1: "2019", 2: "2020/2021"})

    entryYearsDf = combineYears(sustainableEntries,allEntries)
    alldfs = [entryYearsDf, dfListOfEntries]

    df = pd.concat(alldfs, ignore_index=True).apply(lambda x: pd.Series(x.dropna().values)).fillna('')
    return df


def createWinningSheetsSustainability(dfSust,dfAll,column):
    #writting winners
    sustWinners = dfSust[dfSust['Sustainablility Winner'].notnull()].groupby(["FestivalYear", column])[
        "Sustainability Entries"].size().groupby("FestivalYear").size()
    allWinners = dfAll[dfAll['Winner'].notnull()].groupby(["FestivalYear", column])["All Entries"].size().groupby("FestivalYear").size()
    listOfWinners = []

    for year in dfSust["FestivalYear"].unique():
        listOfWinners.append(dfSust[(dfSust["FestivalYear"] == year)& (dfSust["Sustainablility Winner"].notnull())][column].unique())

    dfListOfWinners = pd.DataFrame(listOfWinners).transpose().rename(columns={0: "2018", 1: "2019", 2: "2020/2021"})

    entryWinnerYearsDf = combineYears(sustWinners, allWinners)
    allWinnerDfs = [entryWinnerYearsDf, dfListOfWinners]
    df = pd.concat(allWinnerDfs, ignore_index=True).apply(lambda x: pd.Series(x.dropna().values)).fillna('')
    return df

def pivotTableForsustainability(dfSust, column):
    return dfSust.groupby(["FestivalYear", column])["EntryTypeName"].count().reset_index().rename(columns = {"EntryTypeName":"Number"})\
        .pivot_table("Number", column,"FestivalYear")

def allStatsForSustainability(dfSust, dfAll, column, writingFile):
    df = createEntriesSheetsSustainability(dfSust, dfAll, column)
    df.to_excel(writingFile, sheet_name="{} Entries".format(column),index=False)
    df = createWinningSheetsSustainability(dfSust,dfAll,column)
    df.to_excel(writingFile,sheet_name="{} Winners".format(column),index=False)
    df = pivotTableForsustainability(dfSust,column)
    df.to_excel(writingFile,sheet_name="{}Sust pivot Table".format(column))


def removeTags(df):
    return copy.deepcopy(df.drop(["tagname", "TagGroupName","taggroupgroupname"], axis = 1).drop_duplicates())

def createStatsCBTDf(df, dfclear, writingFile):
    allShortlist = df.groupby(["taggroupgroupname", "TagGroupName", "tagname"])["Shortlist"].count()
    all_winners = df.groupby(["taggroupgroupname", "TagGroupName", "tagname"])["Winner"].count()
    all_entries = df.groupby(["taggroupgroupname", "TagGroupName", "tagname"])["All Entries"].count()


    percentageToTotalEntries =df.groupby(["taggroupgroupname", "TagGroupName", "tagname"])["All Entries"].count() \
                             /  len(dfclear)
    percentageToTotalWinners = df[df["Winner"].notnull()].groupby(["taggroupgroupname", "TagGroupName", "tagname"])["Winner"].count() \
                         /len(dfclear[dfclear["Winner"].notnull()])
    percentageToTotalShorts = df[df["Shortlist"]==1].groupby(["taggroupgroupname", "TagGroupName", "tagname"])["Shortlist"].count() \
                             / len(dfclear[dfclear["Shortlist"]==1])


    percentageToTotalWinners = percentageToTotalWinners.fillna(0)
    percentageToTotalShorts = percentageToTotalShorts.fillna(0)
    percentageToTotalEntries = percentageToTotalEntries.fillna(0)

    final = pd.DataFrame({"All Entries": all_entries, "Shortlisted": allShortlist, "All Winners": all_winners,
                          "% Entries": percentageToTotalEntries#.map("{:.1%}".format),
                          ,"% Shortlist": percentageToTotalShorts
                          ,"% Winners": percentageToTotalWinners}
                          )
    #ignore coloring for the time being
    #final = final.style.applymap(styleLarge,props = 'background-color:green').highlight_max(axis=0,props='background-color:darkblue')



    final.reset_index()\
        .style.set_properties(**{'text-align': 'left'})\
        .format({"% Entries":'0:.2f%'.format,"% Shortlist": '{0:.2f%}'.format,"% Winners": '{0:.2f%}'.format})\
        .to_excel(writingFile, index = False)

    workbook = writingFile.book
    # worksheet = writingFile.sheets['Sheet1']
    format =workbook.add_format({'num_format': ':.1%'})


    for column in final:
        column_length = max(final[column].astype(str).map(len).max(), len(column))
        col_idx = final.columns.get_loc(column)
        writingFile.sheets['Sheet1'].set_column(col_idx, col_idx, column_length, format)




    writingFile.save
    return final


def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')


def styleZero(v, props=''):
    if isinstance(v,str):
        v =  float(v.replace('%',''))
    return props if v <= 0 else None

def styleLarge(v,props=''):
    if isinstance(v,str):
        v = float(v.replace('%',''))
    return props if v >= 75 else None


def combineYears(*args):
    df = pd.DataFrame()
    for series in args:
        name = series.name
        df[name] = series
    return  df


#df.groupby(["FestivalYear", "MediaDescription", "sector_name"])["EntryTypeName"].count().reset_index().rename(columns = {"EntryTypeName":"Number"})\
 #   .pivot_table("Number", "MediaDescription","FestivalYear")