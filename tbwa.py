from imports import *
from queries import TBWAQuery
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')

# years = [2017, 2018, 2019]
# short = [1, 'any']
# prize = ['is nut null', 'any']


df = pd.read_sql(TBWAQuery, conn)
# raw numbers:
# counting none as false
df["Shortlist"].fillna(False)
df["Shortlist"] = df["Shortlist"].replace([None], False, regex=True)

average_short_total = df[df["Shortlist"]]["MediaDescription"].count() / df["MediaDescription"].count()
average_conversion_total = df["Winner"].count() / df["MediaDescription"].count()

print("average short total:", average_short_total)
print("average conversion total:", average_conversion_total)

dfTBWA = df[df["NetworkName"] == 'TBWA WORLDWIDE']

average_short_TBWA = dfTBWA[dfTBWA["Shortlist"]]["MediaDescription"].count() / dfTBWA["MediaDescription"].count()
average_conversion_TBWA = dfTBWA["Winner"].count() / dfTBWA["MediaDescription"].count()

print("tbwa short percentage:", average_short_TBWA)
print("tbwa conversion percentage:", average_conversion_TBWA)

average_short_total20202021 = df[(df["Shortlist"]) & (df["FestivalYear"] >= 2020)]["MediaDescription"].count() / \
                              df[df["FestivalYear"] >= 2020]["MediaDescription"].count()
average_conversion_total20202021 = df[df["FestivalYear"] >= 2020]["Winner"].count() / \
                                   df[df["FestivalYear"] >= 2020]["MediaDescription"].count()
print("Average shortlist Conversion rates for 2020 onwards", "{:.3%}".format(average_short_total20202021))
print("Average award Conversion rates for 2020 onwards", "{:.3%}".format(average_conversion_total20202021))

average_short_TBWA20202021 = dfTBWA[(dfTBWA["Shortlist"]) & (dfTBWA["FestivalYear"] >= 2020)]["MediaDescription"].count() / \
                             dfTBWA[df["FestivalYear"] >= 2020]["MediaDescription"].count()
average_conversion_TBWA20202021 = dfTBWA[dfTBWA["FestivalYear"] >= 2020]["Winner"].count() / \
                                  dfTBWA[dfTBWA["FestivalYear"] >= 2020]["MediaDescription"].count()
print("Average TBWA shortlist Conversion rates for 2020 onwards", "{:.3%}".format(average_short_TBWA20202021))
print("Average TBWA award Conversion rates for 2020 onwards", "{:.3%}".format(average_conversion_TBWA20202021))

short_rates_per_year_TBWA = dfTBWA[dfTBWA["Shortlist"]].groupby(["FestivalYear"]).count()["Shortlist"] \
                            / dfTBWA.groupby(["FestivalYear"]).count()["MediaDescription"]
conversion_rates_per_year_TBWA = dfTBWA.groupby(["FestivalYear"]).count()["Winner"] \
                                 / dfTBWA.groupby(["FestivalYear"]).count()["MediaDescription"]

print("short_rates_per_year_TBWA", short_rates_per_year_TBWA)
print("conversion_rates_per_year_TBWA", conversion_rates_per_year_TBWA)

dfTBWA['AwardedOrNot'] = np.where(dfTBWA['Winner'].fillna('') != "", True, False)
dfTBWAGrouped = dfTBWA[["FestivalYear", "CompanyName", "AwardedOrNot"]]

skata = dfTBWAGrouped.groupby(["FestivalYear", "CompanyName"]).agg(['unique'])
skatoulakia = skata["AwardedOrNot"].reset_index()
skatoulakia = skatoulakia.rename(columns={"unique": "AgencyWonAwardYear"})

for index, value in skatoulakia["AgencyWonAwardYear"].items():
    if np.array_equal(value, [False]):
        skatoulakia["AgencyWonAwardYear"][index] = False
    else:
        skatoulakia["AgencyWonAwardYear"][index] = True

skatoulakia.groupby(["FestivalYear", "AgencyWonAwardYear"]).size()

skatoulakia[skatoulakia["AgencyWonAwardYear"] == False].groupby(["FestivalYear", "AgencyWonAwardYear"]).size() / \
skatoulakia[skatoulakia["AgencyWonAwardYear"] == False].groupby(["FestivalYear", "AgencyWonAwardYear"]).size()

successfulOffices = []
for index, row in skatoulakia.iterrows():
    if row["AgencyWonAwardYear"]:
        successfulOffices.append([row["FestivalYear"], row["CompanyName"]])

dfSucessfulOffices = pd.DataFrame(successfulOffices, columns=['FestivalYear', 'CompanyName'])