import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""
  print(os.getcwd())

  # Call the function to create the file 
  create_file(filename)
  print(filename)

  # Open the file
  print(filename)
  with open("filename", "r") as csv_file:
      pass
    # Read the rows of the file into a dictionary
   # new_file = csv.dictreader(csv_file)
    # Process each item of the dictionary
   # for line in dictreader:
      #return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
 # return return_string
#
#Call the function
print(contents_of_file("flowers.csv"))
