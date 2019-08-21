import csv
import string

class MyTemplate(string.Template):
    delimiter = '##'

# Open template file and pass string to 'TemplateData'.
# items in the heading row of the input CSV file.

with open('test-template.txt', 'r') as my_template:
    TemplateData = my_template.read()
    print('Template loaded:')
    # Pass 'data' to string.Template object data_template.
    data_template = MyTemplate(TemplateData)

# Open the input CSV file and pass to dictionary 'input_file'
with open('Book1.csv') as data_file:
    input_data = csv.DictReader(data_file)

    for row in input_data:
        # Create filenames for the output HTML files
        filename = row['HOST_NAME'] + '.config'
        # Print filenames for visual cue.
        print(filename)
        print(row)
        # Create output Config file.
        with open(filename, 'w') as output_file:
            # Run string.Template substitution on data_template
            # using data from 'row' as source and write to
            # 'output_file'.
            output_file.write(data_template.substitute(row))
# Print the number of files created as a cue program has finished.
print(str(input_data.line_num - 1) + ' files were created.')