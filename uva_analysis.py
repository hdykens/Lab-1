#UVA_Analysis Instructions:
#Compare with Peers and Market
#Propose Strategy


#"Peer" is defined by Top 5 Public Ivies as a collective. We are comparing UVA against the other 4 universities.
# "Whole Market" is defined by all the universities, including UVA. We are comparing UVA against the whole market for marketshare purposes. 
# However, for other metrics, we are comparing UVA against everyone else.

#Completed by Hannah Sweazey, Hannah Dykens, and Susanna Huang xD

#SUMMARY:
#Compared to its Public Ivy peers in the Top 50 Foreign Funding Flows, UVA lags behind at  $8.24M for foreign donations.
#UNC has about 3x as much donations, with $23.8M , while UMich, UC Berkeley, UCLA are way out of their donating league in the $200M+ for each university.
#UVA's current international funding mainly comes from health, pharma, and clinical research, specializing in medical contracts.
#Meanwhile, the collective peer universities have donations that are mostly high income countries (e.g. Japan, Germany, and the UK) and have twice as much monetary gifts as opposed to contracts.
#The Data Science school could collab with the Advancement dept strategize on a transition from speccialized clinical porfolio
#to a more diversified global corporate portfolio and ensure that UVA continues to be a prestigious R1 research engine given the current political climate.
#Better yet, we can also call upon Darden, Law School, McIntire, etc for benchmarking and advice on their best practices with getting donations from corporate or indivuals.



###########################################################################################################################
print("========= QUANTITATIVE COMPARATIVE ANALYSIS ========\n")
#from google.colab import drive
#drive.mount('/content/drive')
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df=pd.read_csv("ForeignGifts_edu.csv")
#df = pd.read_csv('/content/drive/My Drive/ForeignGifts_edu.csv')

uva_only= df[df["Institution Name"] == "University of Virginia"]
market_no_uva= df[df["Institution Name"]!= "University of Virginia"]
whole_market=df

top_4_public_ivies = [
    "University of North Carolina - Chapel Hill",
    "University of Michigan - Ann Arbor",
    "University of California, Los Angeles",
    "University of California, Berkeley"
]
top_public_Ivy=df[df["Institution Name"].isin(top_4_public_ivies)]

top_5_public_ivies_for_graph = [
    "University of North Carolina - Chapel Hill",
    "University of Michigan - Ann Arbor",
    "University of California, Los Angeles",
    "University of California, Berkeley",
    "University of Virginia"
]

##########################################################################################################################
#Top 10 UVA/Market- W/O UVA/Peer Gift Amount by Giftor name
uva_top_amt_giftor=uva_only.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
peer_top_amt_giftor=top_public_Ivy.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
market_top_amt_giftor=market_no_uva.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)

print(f"######Top 10 Gift Amount by Giftor for UVA, Peers, and Market#######\n")
print(f"##############UVA:\n")
print(uva_top_amt_giftor)
print(f"##############Peers:\n")
print(peer_top_amt_giftor)
print(f"##############Market:\n")
print(market_top_amt_giftor)


###########################################################################################################################
#Top 10 UVA/Market- W/O UVA/Peer Gift Amount by country
uva_top_amt_country=uva_only.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
market_top_amt_country=market_no_uva.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
peer_top_amt_country=top_public_Ivy.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)

print(f"######Top 10 Gift Amount by Country for UVA, Peers, and Market#######\n")
print(f"##############UVA:\n")
print(uva_top_amt_country)
print(f"##############Peers:\n")
print(peer_top_amt_country)
print(f"##############Market:\n")
print(market_top_amt_country)


#################################################################################################################################
#Top 5 UVA/Market- W/O UVA/Peer Foreign Country Donors:
uva_top_foreign_donors=uva_only["Country of Giftor"].value_counts().head(5)
market_top_foreign_donors=market_no_uva["Country of Giftor"].value_counts().head(5)
peer_top_foreign_donors=top_public_Ivy["Country of Giftor"].value_counts().head(5)

print(f"######Top 5 Foreign Country Donors for UVA, Peers, and Market#######\n")
print(f"##############UVA:\n")
print(uva_top_foreign_donors)
print(f"##############Peers:\n")
print(peer_top_foreign_donors)
print(f"##############Market:\n")
print(market_top_foreign_donors)


############################################################################################################################
#Gift type by UVA, Peer, Market-W/O UVA
uva_top_gift_types = uva_only["Gift Type"].value_counts()
market_top_gift_types=market_no_uva["Gift Type"].value_counts()
peer_top_gift_types=top_public_Ivy["Gift Type"].value_counts()

print(f"###### Gift type by UVA, Peer, Market#########\n")
print(f"##############UVA:\n")
print(uva_top_gift_types)
print(f"##############Peers:\n")
print(peer_top_gift_types)
print(f"##############Market:\n")
print(market_top_gift_types)


##############################################################################################################################
#UVA/Market- W/O UVA/Peer Means
uva_mean=uva_only["Foreign Gift Amount"].mean()
market_mean=market_no_uva["Foreign Gift Amount"].mean()
peer_mean=top_public_Ivy["Foreign Gift Amount"].mean()

print(f"###### UVA/Peer/Market Means#######\n")
print(f"##############UVA:\n")
print(uva_mean)
print(f"##############Peers:\n")
print(peer_mean)
print(f"##############Market:\n")
print(market_mean)


#UVA/Market- W/O UVA/Peer Medians
uva_median=uva_only["Foreign Gift Amount"].median()
market_median=market_no_uva["Foreign Gift Amount"].median()
peer_median=top_public_Ivy["Foreign Gift Amount"].median()

print(f"###### UVA/Peer/Market Medians#######\n")
print(f"##############UVA:\n")
print(uva_median)
print(f"##############Peers:\n")
print(peer_median)
print(f"##############Market:\n")
print(market_median)



#UVA/Market-W/O UVA/Peer Ranges
uva_range=uva_only["Foreign Gift Amount"].max()-uva_only["Foreign Gift Amount"].min()
market_range=market_no_uva["Foreign Gift Amount"].max()-market_no_uva["Foreign Gift Amount"].min()
peer_range=top_public_Ivy["Foreign Gift Amount"].max()-top_public_Ivy["Foreign Gift Amount"].min()

print(f"###### UVA/Peer/Market Ranges#######\n")
print(f"##############UVA:\n")
print(uva_range)
print(f"##############Peers:\n")
print(peer_range)
print(f"##############Market:\n")
print(market_range)


#UVA/Market-W/O UVA/Peer Standard Deviations
uva_std=uva_only['Foreign Gift Amount'].std()
market_std=market_no_uva['Foreign Gift Amount'].std()
peer_std=top_public_Ivy['Foreign Gift Amount'].std()

print(f"###### UVA/Peer/Market Standard Deviations#######\n")
print(f"##############UVA:\n")
print(uva_std)
print(f"##############Peers:\n")
print(peer_std)
print(f"##############Market:\n")
print(market_std)


####################################################
#Unique Countries
uva_unique= uva_only["Country of Giftor"].nunique()
market_unique=market_no_uva["Country of Giftor"].nunique()
peer_unique= top_public_Ivy["Country of Giftor"].nunique()

print(f"###### Unique Countries Donating to UVA/Peer/Market#######\n")
print(f"##############UVA:\n")
print(uva_unique)
print(f"##############Peers:\n")
print(peer_unique)
print(f"##############Market:\n")
print(market_unique)


######################################################
#UVA Share of the Whole Market
uva_market_share=((uva_only["Foreign Gift Amount"].sum()/whole_market["Foreign Gift Amount"].sum()) * 100).round(2)
print(f"###### UVA Share of the Market by Gift Amount#######\n")
print(f"{uva_market_share}%")

######################################################
#Peer share of the Whole Market
peer_market_share=((top_public_Ivy["Foreign Gift Amount"].sum()/whole_market["Foreign Gift Amount"].sum()) * 100).round(2)
print(f"###### Peer Share of the Market by Gift Amount#######\n")
print(f"{peer_market_share}%")



################################


##GRAPH

country = "Country of Giftor"

recipi = "Institution Name"

flow = "Foreign Gift Amount"



# 1. Filter for Top Public Ivies

df_filtered = df[df[recipi].isin(top_5_public_ivies_for_graph )].dropna(subset=[country])


# 2. Group by Country and Institution Name

flows = (

    df_filtered.groupby([country, recipi])[flow]

    .sum()

    .nlargest(50)

    .reset_index()

)



# 3. Build unique labels

labels = list(dict.fromkeys(flows[country].tolist() + flows[recipi].tolist()))



# 4. Construct Sankey diagram

fig = go.Figure(

    go.Sankey(

        node=dict(label=labels, pad=15, thickness=20),

        link=dict(

            source=flows[country].map(labels.index),

            target=flows[recipi].map(labels.index),

            value=flows[flow],

        ),

    )

)



fig.update_layout(

    title_text="Top 50 Foreign Funding Flows to Top Public Ivies by Country",

    font_size=10,

)

fig.show()