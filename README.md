# Daily Report
Daily Report is a python script that collects data from various sources and uses LaTeX to create a PDF summary.

## Getting Started
### Prerequisites
Please make sure that you are using Python 3.7 (64-bit). I recommend that you use a venv for this project. Instructions can be found [here](https://docs.python.org/3/tutorial/venv.html).

### Installing Dependencies
Navigate to the root directory.
```bash
cd DailyReport
```

Install the dependencies in requirements.txt with:
```bash
pip install -r requirements.txt
```
Depending on your system installation of Python you may need to use ```pip3``` instead of ```pip```.

### Data Sources
To add a new data source create a new directory in ```dailyreport/datasources``` and place a python script that fetches data and returns a pandas DataFrame.