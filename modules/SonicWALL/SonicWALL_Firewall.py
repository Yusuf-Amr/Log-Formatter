import re
from rich.console import Console
from rich.table import Table

# Initializing the console 
console = Console()

class SonicWALLLogFormatter:
    def __init__(self, log):
        self.log = log
        self.log_dict = {}

    def parse(self):
        # Using Regex pattern to capture key-value pairs
        key_value_pairs = re.findall(r'(\w+)=(".*?"|\S+)', self.log)
        
        # Extracting key-value pairs from the log
        for key, value in key_value_pairs:
            # Remove surrounding quotes from values
            self.log_dict[key] = value.strip('"')

    def display(self):
        # Creating a table with two columns: Field and Value
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field", style="dim", width=30)
        table.add_column("Value", style="bold")

        # Generating the table with the log data
        for key, value in self.log_dict.items():
            table.add_row(key, value)

        # Printing the table with rich 
        console.print(table)
