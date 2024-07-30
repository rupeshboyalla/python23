import re
import csv
# reading given tsv file
with open("/Users/rupesh.boyalla/Documents/my_git/python23/leetcode/arrays/SURF_labels.tsv", 'r') as myfile:
    with open("/Users/rupesh.boyalla/Documents/my_git/python23/leetcode/arrays/SURF_labels.csv", 'w') as csv_file:
        for line in myfile:
            # Replace every tab with comma
            fileContent = re.sub("\t", ",", line)
            temp = fileContent.split(',')
            if len(temp) > 3:
                # Writing into csv file
                csv_file.write(fileContent)

        # output

# output
print("Successfully made csv file")