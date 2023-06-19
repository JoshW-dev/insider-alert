import scraper
import clean
import pandas as pd

print("Main Script...")


#paramaters for openinsider table
post = "screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&ispres=1&iscoo=1&iscfo=1&isvp=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1"


#scrape web 
df = scraper.scrape(post)
#output results as csv
df.to_csv(r'output.csv', index=False)

df_duplicates = clean.find_multiple_trades(df)
#export to csv
df_duplicates.to_csv(r'outputNew.csv', index=False)

summary = clean.summarize_multiple_trades(df_duplicates)
print(summary)
