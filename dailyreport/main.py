import dailyreport.datasources.covid19.covid as covid
import jinja2
import os
from jinja2 import Template

covid_data_tuple = covid.get_covid_data()
today_date_str = covid_data_tuple[0]
england_daily_case_df = covid_data_tuple[1]
england_daily_death_df = covid_data_tuple[2]
york_daily_case_df = covid_data_tuple[3]
york_daily_death_df = covid_data_tuple[4]

# print(england_daily_death_df.iloc[0, 0:])
# print(england_daily_case_df.iloc[0]['Daily lab-confirmed cases'])
# print(england_daily_death_df.iloc[0]['Daily change in deaths'])
# print(york_daily_case_df.iloc[0]['Daily lab-confirmed cases'])
# print(york_daily_death_df.iloc[0]['Daily change in deaths'])

try:
	england_daily_case = england_daily_case_df.iloc[0]['Daily lab-confirmed cases']
except IndexError:
	england_daily_case = 0

try:
	england_daily_death = england_daily_death_df.iloc[0]['Daily change in deaths']
except IndexError:
	england_daily_death = 0

try:
	york_daily_case = york_daily_case_df.iloc[0]['Daily lab-confirmed cases']
except IndexError:
	york_daily_case = 0

try:
	york_daily_death = york_daily_death_df.iloc[0]['Daily change in deaths']
except IndexError:
	york_daily_death = 0


try:
	england_total_case = england_daily_case_df.iloc[0]['Cumulative lab-confirmed cases']
except IndexError:
	england_total_case = 0

try:
	england_total_death = england_daily_death_df.iloc[0]['Cumulative deaths']
except IndexError:
	england_total_death = 0

try:
	york_total_case = york_daily_case_df.iloc[0]['Cumulative lab-confirmed cases']
except IndexError:
	york_total_case = 0

try:
	york_total_death = york_daily_death_df.iloc[0]['Cumulative deaths']
except IndexError:
	york_total_death = 0

# print(today_date_str)
#
# print(england_daily_case)
# print(england_daily_death)
# print(york_daily_case)
# print(york_daily_death)
#
# print(england_total_case)
# print(england_total_death)
# print(york_total_case)
# print(york_total_death)

latex_jinja_env = jinja2.Environment(
	block_start_string='\BLOCK{',
	block_end_string='}',
	variable_start_string='\VAR{',
	variable_end_string='}',
	comment_start_string='\#{',
	comment_end_string='}',
	line_statement_prefix='%%',
	line_comment_prefix='%#',
	trim_blocks=True,
	autoescape=False,
	loader=jinja2.FileSystemLoader(os.path.abspath('.'))
)

# Gets the reportTemplate
template = latex_jinja_env.get_template('./latex_templates/reportTemplate.tex')
# Loads the data into the template
document = template.render(gdcases=str(england_daily_case), gtcases=str(england_total_case), gddeaths=str(england_daily_death), gtdeaths=str(england_total_death), ldcases=str(york_daily_case), ltcases=str(york_total_case), lddeaths=str(york_daily_death), ltdeaths=str(york_total_death))
# Write document
with open("dailyReport.tex", "w") as output:
	output.write(document)


