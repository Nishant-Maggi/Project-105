import csv
import math 

with open("deviationtData.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    sum_of_elements = 0
    sum_of_sqrd_difference = 0
    size_of_data = len(file_data)

    for i in file_data:
        number = i[0]
        sum_of_elements += int(number) 
    mean = sum_of_elements/len(file_data)
    
    for i in file_data:
        number = i[0]
        xi_u = int(number) - mean
        sqaured_difference = pow(xi_u, 2)
        sum_of_sqrd_difference += sqaured_difference

    standard_deviation = math.sqrt(sum_of_sqrd_difference/size_of_data)
    print(standard_deviation)    