import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Load the Foreign Gifts data.
df = pd.read_csv('ForeignGifts_edu.csv')
#print(df.head())

# 2. Describe the differences between different classes of gift types.

print("----- Gift Type Counts -----")
#print(df.dtypes)
print(df["Gift Type"].value_counts())

print("----- Gift Type Missing Values -----")
print(df["Gift Type"].isna().sum())

print("----- Gift Type Unique Values -----")
print(df["Gift Type"].unique())

print("----- Gift Type Hist -----")
plt.hist(df["Gift Type"], bins=20)
plt.xlabel("Gift Type")
plt.ylabel("Frequency")
plt.title("Distribution of Gift Types")
plt.show()

# 3. Answer the following questions:
print("1. Which country gives the most money in total?\n") 
# Qatar gives the most money with a total of 2,706,240,869


print(df.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(1), "\n")

print("2. Which country initiates the most gifts by count?\n")
# England gave the most individual gifts with a count of 3,655


print(df.groupby("Country of Giftor").size().sort_values(ascending=False).head(1), "\n")

print("3. Which country gives the largest gifts on average?\n")
# Bermuda gives the largest gifts with an average of 7.688837e+06



print(df.groupby("Country of Giftor")["Foreign Gift Amount"].mean().sort_values(ascending=False).head(1), "\n")

# bermuda = df[(df['Country of Giftor'] == "BERMUDA")]
# print(bermuda[["Foreign Gift Amount"]].sort_values(by="Foreign Gift Amount", ascending=False))

print("4. Which institution receives the most money in total?\n")
# Carnegie Mellon received the most money at $1,477,922,504



#print(df.dtypes)
print(df.groupby("Institution Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(1), "\n")

print("5. Which institution receives the greatest number of gifts by count?")
print("Build a plot of the top 20 institutions by the amount or number of gifts they have received using either seaborn or plotly. \n")
# University of California, Los Angeles (UCLA) has received the highest count of gifts



top_20 = df.groupby("Institution Name").size().sort_values(ascending=False).head(20)
top = top_20.head(1)
print(top)
plt.barh(top_20.index, top_20.values)
plt.xlabel("Number of Gifts")
plt.ylabel("Institution Name")
plt.title("Top 20 Institutions by Number of Gifts Received")
plt.tick_params(axis='y', labelsize=5)
plt.show()

print("6. What is the average amount each university receives? Median amount? If they are different why?")
# Mean amount is $52,202,878.98, median amount is $6,486,791.5

print("Plot a histogram of the amounts received by each university, and then label the median and the mean as vertical lines.\n")
beef=df.groupby(["Institution Name"], as_index=False).sum().sort_values(by="Foreign Gift Amount", ascending=False)
mean_amt = beef["Foreign Gift Amount"].mean()
median_amt = beef["Foreign Gift Amount"].median()
print("Mean:", mean_amt)
print("Median:", median_amt)

#gift_amt = df.groupby("Institution Name")["Foreign Gift Amount"].sum()
plt.hist(x = "Foreign Gift Amount", data = df)
plt.xticks(rotation=90)
plt.tick_params(axis='x', labelsize=1)
#plt.ylim(0,2000)
plt.axvline(mean_amt, color='g', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(median_amt, color='r', linestyle='dashed', linewidth=1, label='Median')
plt.legend()
plt.xlabel("Foreign Gift Amount")
plt.ylabel("Number of Institutions")
plt.title("Amounts Received by Each Institution")
plt.show()

print("Mean: \n", df.groupby("Institution Name")["Foreign Gift Amount"].mean().sort_values(ascending=False).head(5), "\n")
print("Median: \n", df.groupby("Institution Name")["Foreign Gift Amount"].median().sort_values(ascending=False).head(5), "\n")


gift_mean = df.groupby("Institution Name")["Foreign Gift Amount"].mean().sort_values(ascending=False)
gift_median = df.groupby("Institution Name")["Foreign Gift Amount"].median().sort_values(ascending=False)

print("The mean is more susceptible to outliers while the median is more robust as it just references the middle value.\n")
print("7. What is the largest flow of a single country to a single institution?\n")
print("First, use `pd.crosstab` to look at the relationship between outcoming gifts from countries and incoming gifts to institutions.\n ")
# Qatar has gifted the highest monetary amount to Cornell University (1.02 million)



#print(df.groupby(["Country of Giftor", "Institution Name"]).sum().sort_values(by="Foreign Gift Amount", ascending=False).head(5), "\n")
countries = pd.crosstab(df["Institution Name"], df["Country of Giftor"],margins = True).sort_values(by="All", ascending=False)

print(countries)

import plotly.graph_objects as go

giftor = 'Country of Giftor'
recipi = 'Institution Name'
flow = 'Foreign Gift Amount'
N = 20

flows = (
    df.groupby([giftor, 
                recipi])
      [flow]
      .sum()
      .nlargest(N)
      .reset_index()
)

labels = (
    flows[giftor].tolist()
    + flows[recipi].tolist()
)

labels = list(dict.fromkeys(labels))

fig = go.Figure(
    go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=flows[giftor]
                        .map(labels.index),
            target=flows[recipi]
                        .map(labels.index),
            value=flows[flow]
        )
    )
)

fig.show()

print("The biggest flow of a single country to a single institution is from Qatar to Cornell.")
country_gift = df.groupby(["Country of Giftor", "Institution Name"]).sum().sort_values(by="Foreign Gift Amount", ascending=False)
print(country_gift[["Foreign Gift Amount"]].sort_values(by="Foreign Gift Amount", ascending=False).head(1), "\n")

print("8. Which are the top giftors to US academic institutions?\n")
# The Qatar Foundation has gifted the highest three amounts to U.S institutions.



# print(df.dtypes)
# print(df["State"].unique())
# print(df["Institution Name"].unique())
print(df.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10), "\n")