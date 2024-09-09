# Log Formatter Tool

When working with raw logs, it can be hard to read and make sense of the data quickly. This tool is an example of how to format logs in a more readable way, making it easier to understand them at a glance. I’ve included examples for three types of logs: Cisco, SonicWall, and Juniper. As a security analyst, you can easily customize this tool by adding modules of the log types you work with, helping you analyze logs faster and more efficiently.
## Features

- log formats examples:
  - Cisco logs
  - SonicWall logs
  - Juniper logs
    
- Output logs in a tabular, easy-to-read format

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Yusuf-Amr/Log-Formatter.git

2. Navigate to the project directory:

   ```bash
   cd Log-Formatter

3. Create and activate a virtual environment (Optional):
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt


## Usage

![Formatted Log Example 1](https://github.com/Yusuf-Amr/Log-Formatter/blob/main/Demo%20Images/1.png?raw=true)
*Figure 1: Running the tool and entering the log data*

Once the log is entered, it is parsed and formatted as shown below:

![Formatted Log Example 2](https://github.com/Yusuf-Amr/Log-Formatter/blob/main/Demo%20Images/2.png?raw=true)
*Figure 2: Example of formatted log from SonicWall*

## Raw Log Source

The sample raw logs used in this tool for formatting and visualization can be found at the IBM documentation for various log types. Specifically, the SonicWall sample event messages are available at the following link:

[SonicWall Sample Event Messages - IBM Documentation](https://www.ibm.com/docs/en/dsm?topic=sonicwall-sample-event-messages)




   
