
from modules.Cisco.IPS_Log_Formats import CiscoIPSLogFormatter
from modules.SonicWALL.SonicWALL_Firewall import SonicWALLLogFormatter
from modules.Juniper.Juniper_Junos_WebApp_Secure import JuniperLogFormatter

def get_log_parser(log_type, log):
    parsers = {
        "1": CiscoIPSLogFormatter,
        "2": SonicWALLLogFormatter,
        "3": JuniperLogFormatter,
    }

    if log_type in parsers:
        return parsers[log_type](log)
    else:
        raise ValueError(f"Unsupported log type: {log_type}")
