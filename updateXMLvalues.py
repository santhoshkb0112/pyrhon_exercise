import xml.etree.ElementTree as ET
import json
from datetime import date, timedelta
import csv
import time
import os

# problem 1

def update_xml(X, Y):
    xml_tree = ET.parse('test_payload1.xml')
    xml_root = xml_tree.getroot()

    depart_text = xml_root.find('REQUEST').find('TP').find('DEPART').text
    depart_date = date(int(depart_text[:4]), int(depart_text[4:6]), int(depart_text[6:]))
    new_depart_date = depart_date + timedelta(days=X)
    final_depart_date = str(new_depart_date).replace("-", "")

    xml_root.find('REQUEST').find('TP').find('DEPART').text = final_depart_date

    return_text = xml_root.find('REQUEST').find('TP').find('RETURN').text
    return_date = date(int(return_text[:4]), int(return_text[4:6]), int(return_text[6:]))
    new_return_date = return_date + timedelta(days=Y)
    final_return_date = str(new_return_date).replace("-", "")

    xml_root.find('REQUEST').find('TP').find('RETURN').text = final_return_date

    xml_tree.write("new_payload.xml")


# Problem 2
def delete(element_to_delete):
    objects = json.load(open("test_payload.json"))

    if element_to_delete in objects.keys():
        del objects[element_to_delete]
    else:
        for key in objects.keys():
            if isinstance(objects[key], dict):
                if element_to_delete in objects[key].keys():
                    del objects[key][element_to_delete]
                    break

    open("new_payload.json", "w").write(json.dumps(objects, indent=2, separators=(',',':')))


# problem 3

def retrive_nonzero_log():
    # Output - printed with a meaningful statement
    with open('Jmeter_log1.csv') as test_csvfile:
        csv_reader = csv.reader(test_csvfile, delimiter=',')

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
                pass
            else:
                line_count += 1
                if row[3] != '200':
                    PSTtimestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(row[0])/1000))
                    print(f'Line {line_count} has non-zero respone code: {row[3]} - and response message:  {row[4]} with a failure message: {row[8]} , label is {row[2]}, at time {PSTtimestamp} ')
                    line_count +=1





delete('appdate')

update_xml(1,2)

retrive_nonzero_log()
