import dailyreport.datasources.covid19.covid as covid

covid_data_tuple = covid.get_covid_data()
england_daily_case_df = covid_data_tuple[0]
england_daily_death_df = covid_data_tuple[1]
york_daily_case_df = covid_data_tuple[2]
york_daily_death_df = covid_data_tuple[3]

