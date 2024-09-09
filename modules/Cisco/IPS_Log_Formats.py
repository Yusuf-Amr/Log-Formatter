import re
from rich.console import Console
from rich.table import Table

console = Console()

class CiscoIPSLogFormatter:
    def __init__(self, log):
        self.log = log
        self.log_dict = {}

    def parse(self):
        # Splitting the log into fields based on commas and removing surrounding quotes
        fields = [field.strip('"') for field in self.log.split(',')]
        
        # Creating dynamic headers based on the number of fields
        headers = [f"Field {i+1}" for i in range(len(fields))]
        
        # Creating a dictionary from headers and fields
        self.log_dict = dict(zip(headers, fields))

    def display(self):
        # Creating  a table with two columns: Field and Value
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field", style="dim", width=30)
        table.add_column("Value", style="bold")

        # Generating the table with the log data
        for key, value in self.log_dict.items():
            table.add_row(key, value)

        # Printing the table with rich library
        console.print(table)
