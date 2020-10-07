![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Data Cleaning and Manipulation with Pandas

First I divided the process in Acquisition -> Wrangling -> Analysis and Visualization.
Then with excel I gave a quick look to the data set to evaluate how I will begin the process of cleaning.

I created a python notebook to advance step by step first defining the acquisition function, then started with the cleaning.
For the cleaning part I implemented different methods for each column since every column has different data.
In general the NaN values of each column I filled it with 0 values for integer columns and with 'Unknown' for object columns.
For the non empty values I replaced the extra symbols of the text with no space, also I striped the spaces of the begining and end of the strings.

For the columns that had more information thatn the requested like Activity, Species and Name columns I made some annonym functions combined with regular expresions to get the information I wanted for each value (for further details check the python notebook).

Once the data base was cleaned I stored it as 'Attacks Clean.csv' on the output folder.

For the Analysis and Visualization I used histograms, barcharts, pie chart and line plots to analyze diffrent information with the cleand data like: the common age of attacked people, attacks by gender, the fattality of the attack and much more. All of these files stroed as well in the output folder.

I also created a pipeline2.py file so it can be executed if the attacks.csv file is updated.