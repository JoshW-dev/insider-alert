import scraper
import clean
import pandas as pd
import os

print("Main Script...")


#paramaters for openinsider table
#All Officers, trading $25k min, own chng% <50%
post = "screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=&och=50&sic1=-1&sicl=100&sich=9999&isofficer=1&iscob=1&isceo=1&ispres=1&iscoo=1&iscfo=1&isgc=1&isvp=1&isdirector=1&istenpercent=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=500&page=1"


#scrape web 
df = scraper.scrape(post)
#look for multiple trades on single day
df_duplicates = clean.find_multiple_trades(df)
#clean value col
df_duplicates = clean.clean_value_column(df_duplicates)
#df_duplicates.to_csv(r'csv/output.csv', index=False)

summary = clean.summarize_multiple_trades(df_duplicates)
#save to files
my_dir = os.path.dirname(__file__)
summary_filepath = os.path.join(my_dir, "summary.csv")
summary.to_csv(summary_filepath, index=False)

print(summary)
