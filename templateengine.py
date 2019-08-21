import csv
import string
import os

class MyTemplate(string.Template):
    delimiter = '##'

def templatedata(filename):
    with open(filename, 'r') as my_template:
        TemplateData = my_template.read()
        #print('Template loaded:')
        # Pass 'data' to string.Template object data_template.
        data_template = MyTemplate(TemplateData)
    return data_template

# Open the input CSV file and pass to dictionary 'input_file'


def parseandreplace(csv_file,template_data,os_path):
    with open(csv_file) as data_file:
        input_data = csv.DictReader(data_file)
        for row in input_data:
            # Create filenames for the output HTML files
            filename = os.path.join(os_path, row['HOST_NAME'] + '.config')
            # for Debug - Print filenames for visual cue.
            # print(filename)
            # Create output Config file.
            with open(filename, 'w') as output_file:
                # Run string.Template substitution on data_template
                # using data from 'row' as source and write to
                # 'output_file'.

                output_file.write(templatedata(template_data).substitute(row))
                # Print the number of files created as a cue program has finished.
        output = str(input_data.line_num - 1)
    return output

