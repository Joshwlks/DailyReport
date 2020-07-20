import dailyreport.datasources.covid19.covid as covid
import jinja2
import os
from jinja2 import Template

covid_data_tuple = covid.get_covid_data()
england_daily_case_df = covid_data_tuple[0]
england_daily_death_df = covid_data_tuple[1]
york_daily_case_df = covid_data_tuple[2]
york_daily_death_df = covid_data_tuple[3]

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

#gets the reportTemplate
template = latex_jinja_env.get_template('./latex_templates/reportTemplate.tex')
#loads the data into the template
document = template.render(gdcases = str(england_daily_case_df))
#write document
with open("dailyReport.tex", "w") as output:
    output.write(document)

