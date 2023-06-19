import scraper
import pandas as pd

print("Main Script...")


#paramaters for openinsider table
post = "screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&ispres=1&iscoo=1&iscfo=1&isvp=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1"


#scrape web 
df = scraper.scrape(post)

#output results as csv
df.to_csv(r'output.csv', index=False)

# Convert 'Trade Date' to datetime
df['Trade\xa0Date'] = pd.to_datetime(df['Trade\xa0Date'])

# Then, find the duplicate rows
df_duplicates = df[df.duplicated(subset=['Ticker', 'Trade\xa0Date'], keep=False)]
df_duplicates = df_duplicates.sort_values(by='Trade\xa0Date')

#export to csv
df_duplicates.to_csv(r'outputNew.csv', index=False)
