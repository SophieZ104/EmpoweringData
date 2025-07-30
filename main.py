# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")

# Isolate Data For Two Countries
indiaBooleanList = lwd["country_name"] == "India" 
indiaDataList = lwd.loc[indiaBooleanList]

senegalBooleanList = lwd["country_name"] == "Senegal"
senegalDataList = lwd.loc[senegalBooleanList]

#Print statements
print("India is a country in southern Asia while Senegal is a country in Western Africa.")

input("Press enter to learn more about the data for these two countries!\n")

print("The data represents households in India and Senegal. In 2015, 67% of India is rural. In 2008, 57% of Senegal is rural")

input("Press enter to learn more context!\n")

print("In 2008, Senegal experienced economic hardship and increasing protests. Hence, due to civil unrest, data collection for Senegalese households became unfeasible beyond 2008. In 2015, India experienced heavy monsoon floods. As a result, many households lost children or child-bearing women, resulting in a dip in household size that year.")

input("What can we do about it?\n")

print("Developed countries like the United States can send foreign aid to Senegal. India should invest in its national weather centers to predict monsoons accurately and timely to reduce casualties.")

input("Press enter to see the graphics!\n")

# Plot Data
plt.scatter(x="year", y="HD_women_size_mean", data=indiaDataList) #Blue
plt.scatter(x="year", y="HD_women_size_mean", data=senegalDataList) #Orange
plt.title("Mean Household Sizes of India and Senegal")
plt.ylim(0,20)
plt.show()
