import pandas as pd

def find_multiple_trades(df):
    # Convert 'Trade Date' to datetime
    df['Trade\xa0Date'] = pd.to_datetime(df['Trade\xa0Date'])

    # Then, find the duplicate rows
    df_duplicates = df[df.duplicated(subset=['Ticker', 'Trade\xa0Date'], keep=False)]
    df_duplicates = df_duplicates.sort_values(by='Trade\xa0Date')
    df_duplicates['Insider'] = df_duplicates['Insider Name'] + " - "+df_duplicates['Title'] 
    return df_duplicates

def summarize_multiple_trades(df):
    # Group dataframe by 'Trade Date' and 'Company Name'
    grouped = df.groupby(['Trade\xa0Date', 'Company\xa0Name'])
    
    # Placeholder for the summaries
    summaries = []
    
    for name, group in grouped:
        unique_insiders = group['Insider'].nunique()
        
        # If there is more than one unique 'Insider Name' in the group
        if unique_insiders > 1:
            summary = {
                'Trade Date': name[0],
                'Company Name': name[1],
                'Unique Insider Count': unique_insiders,
                'Insider': list(group['Insider'].unique()),
                'Total Value': group['Value'].sum(),
            }
            summaries.append(summary)
    df = pd.DataFrame(summaries)
    df["Trade Date"] = df["Trade Date"].astype('datetime64[ns]')
    df.sort_values(by='Trade Date', ascending = False, inplace = True) 
    return pd.DataFrame(df)

def clean_value_column(df):
    df['Value'] = df['Value'].replace({'\$': '', ',': '', '\+': ''}, regex=True).astype(float)
    return df