import requests
import pandas as pd
from datetime import datetime, timedelta

covid_daily_case_url = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-cases_latest.csv'
covid_daily_death_url = 'https://coronavirus.data.gov.uk/downloads/csv/coronavirus-deaths_latest.csv'


def get_covid_data():
    total_case_df = pd.read_csv(requests.get(covid_daily_case_url, stream=True).raw)
    total_death_df = pd.read_csv(requests.get(covid_daily_death_url, stream=True).raw)

    # print(total_case_df.iloc[0, 0:])
    # print(total_case_df['Area name'].unique())
    # print(total_death_df.iloc[0, 0:])
    # print(total_death_df['Reporting date'].unique())

    # Create string of today's date in the form YYYY-MM-DD
    #today_date_str = datetime.now().strftime("%Y-%m-%d")
    today_date_str = "2020-07-22"

    # daily_case_df = uk_case_df.loc[uk_case_df['Specimen date'] == today_date_str]
    england_daily_case_df = total_case_df.loc[(total_case_df['Area name'] == 'England') & (total_case_df['Specimen date'] == today_date_str)]
    england_daily_death_df = total_death_df.loc[(total_death_df['Area name'] == 'England') & (total_death_df['Reporting date'] == today_date_str)]

    york_daily_case_df = total_case_df.loc[(total_case_df['Area code'] == 'E06000014') & (total_case_df['Specimen date'] == today_date_str)] # Has both upper tier and lower tier local authorities
    york_daily_death_df = total_death_df.loc[(total_death_df['Area code'] == 'E06000014') & (total_death_df['Reporting date'] == today_date_str)]
    # print(york_daily_case_df.iloc[1, 0:])
    return today_date_str, england_daily_case_df, england_daily_death_df, york_daily_case_df, york_daily_death_df
