import re
from rich.console import Console
from rich.table import Table

# Initialize the console for colorful output
console = Console()

class JuniperLogFormatter:
    def __init__(self, log):
        self.log = log
        self.log_dict = {}
        self.date_info = ""
        self.additional_info = ""

    def parse(self):
        # Extracting the date and time at the start of the log
        date_match = re.match(r'^([\w\s:]+)', self.log)
        if date_match:
            self.date_info = date_match.group(1).strip()
            remaining_log = self.log[len(date_match.group(0)):].strip()
        else:
            remaining_log = self.log

        # Extracting additional info up to the first key-value pair
        # This captures all text up to the first key-value pair
        additional_info_match = re.match(r'^(.*?)\s*(?=\w+=|$)', remaining_log)
        if additional_info_match:
            self.additional_info = additional_info_match.group(1).strip()
            remaining_log = remaining_log[len(additional_info_match.group(0)):].strip()

        # Extracting key-value pairs from the remaining log
        key_value_pairs = re.findall(r'(\w+)=(".*?"|\S+)', remaining_log)
        for key, value in key_value_pairs:
            self.log_dict[key] = value.strip('"')

    def display(self):
        # Creating a table with two columns: Field and Value
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field", style="dim", width=30)
        table.add_column("Value", style="bold")

        # Adding date and additional info as the first rows if exist
        if self.date_info:
            table.add_row("Date", self.date_info)
        if self.additional_info:
            table.add_row("Additional Info", self.additional_info)
        
        # Adding the rest of the key-value pairs
        for key, value in self.log_dict.items():
            table.add_row(key, value)

        # Printing the table with rich
        console.print(table)


