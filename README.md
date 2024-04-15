# 1. Consumer-Finance project overview

In this project I work with data from the 2022 Survey of Consumer Finance for the United State of America. I will be identifying and grouping households that are struggling to get credit then I will build a model to segment this household into subgroups.

The project can be used for Marketing or Customer Segmntation or Social Stratification.


# 2. Data Source
I downloaded the data from [Survey of Consumer Finances (SCF) website](https://www.federalreserve.gov/econres/scfindex.htm).  The data is in a csv file, I used pandas to read it into a dataframe, which is a good format to perform analysis.
The data has 22975 observations with 356 features. However, after subsetting the data I am left with 3839 observations(instances). Most features are numeric.

This is an unsupervised machine learning project.

The data dictionary can be found [here](https://sda.berkeley.edu/sdaweb/docs/scfcomb2022/DOC/hcbkx01.htm#1.HEADING)

**The dataset has 356 features, I will not be listing them here. Please see the data dictionary above for more information on the data**

# 3.Data Preprocessing and Feature engineering:

1. I subset the data to households that have been rejected for credit and households that are fears they will be rejected for credit.
2. I selected high variance features for the model

# 4. Analysis

###Looking at the age group distribution.

![Age Group](images\age_group.jpg)

The chart above shows that most of the people who fears being rejected for credits are young. The most prevalent group being the people who are between 35 and 44 years old, followed by people who are under the age of 35. 

![Income category](images\income.jpg)

Comparing income categories accross credit fearful and non-credit fearful groups. It is clear that credit fearful group is much common in lower income category group.

Based on the dataset, it is prevalent that among the people who have responded that they were indeed worried about being approved for credit after being denied credit in the past.

A plurality of young and low-income had the highest number of respondents. It seems like young people tends to make less money and rely more heavily on credit to get their lives off the ground, so having been denied credit makes them more anxious about the future.

![Incone category](images\education.jpg)

A much higher propotion of credit-fearful respondents have a high school diploma while university degrees are more common among the non-credit fearful group. 