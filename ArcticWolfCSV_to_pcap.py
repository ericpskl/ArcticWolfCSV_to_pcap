from scapy.all import *
import base64
import csv
from datetime import datetime

# Path to the Arctic Wolf-generated CSV file 
awcsv=r'C:\AW_Alert_File_All_Events_2023-07-10T07-52-33-2023-07-10T08-52-33.csv'

rows = open(awcsv, 'r', encoding='utf-8')

packets=[]

csvreader = csv.DictReader(rows)
for row in csvreader:
    packet=Ether(base64.b64decode(row['packet.base64']))
    packet.time=(datetime.strptime(row['@timestamp'],'%Y-%m-%dT%H:%M:%S.%f') - datetime(1970, 1, 1)).total_seconds()
    packets.append(packet)

rows.close()

# CSV data is in reverse order, so flip before writing to disk

packets.reverse()

# Export as PCAP.  Change path/filename as appropriate

wrpcap("c:/aw/generated.pcap", packets)    
                   
