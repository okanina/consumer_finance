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


  ![scatterplot](images/scatter.png)

  ![clusters](images/newplot.png)

 The clusters are partially based on **NETWORTH** so my analysis will be based on networth as well.Looking at the 5 clusters on the chart above, the households in cluster 1 have the smallest networth of the 5 clusters, while cluster 4 has the highest networth value. 

Looking at the **DEBT** variable, one might think it would scale as the networth increases, but it doesn't. The lowest amount of debt in propotion to the home value is in cluster 4, even though the value of their homes (shown in green) is high. You can't really tell from this data what's going on, but one possibility might be that the people in cluster 4 have enough money to pay down their debts, likewise cluster 2 also has lower debt value than the home value. However, one might think cluster 2 might not have quite enough money to leverage what they have into additional debts. The people in cluster 3, by contrast, might not need to worry about carrying debt because their net worth is so high.
 
Finally, as this project focuses at the households that are fearful that they might be rejected when applying for credit or were rejected when they applied for the loan. Looking at the relationship between DEBT values and Home values: The value for debt for the people in cluster 1 and 3 is higher than their networth and also high than their home values, suggesting that most of the debt they carry is tied up in their mortgages — if they own a home at all. This may also suggest that as their networth value is lower than their debt value this might suggest that paying an additional debt to what they already have might be difficult for them (this explains their fear or why they were rejected for credit).
Contrast that with the other three clusters: the value of everyone else's debt is lower than the value of their homes and for cluster 2 and 4 their networth value is higher then their debt value.
    
People in cluster 4 might not need to worry because their debt value is low with high networth and asset value. One might think that their fear might stem from the fact that most of their asset comes from non-financial stuff(there isn't enough evidence to draw this conclusion)