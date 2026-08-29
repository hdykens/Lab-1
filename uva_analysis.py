#UVA_Analysis
#Compare with Peers and Market
# Propose Strategy
#"Peer" is defined by Top 5 Public Ivies

#SUMMARY:
#Compared to its Public Ivy peers, UVA is really lagging behind at  $22.2M for foreign donations.
#UNC hasdouble the amount with $41.3M , while UMich and UC Berkeley are way out of their donating league with $280M+.
#UVA's current international funding mainly comes from health, pharma, and clinical research in low income countries, specializing in medical contracts.
#UVA needs to start targeting corporate donors from high income countries (e.g. Japan, Germany, and the UK) and get monetary gifts as opposed to contracts.
#The Data Science school could collab with the Advancement dept to transition and come up with strategy to transition a specilized clinical porfolio 
#to a more diversified global corporate portfolio and ensure that UVA continues to be a prestigious R1 research engine.
#Better yet, we can collab with Darden, Law School, McIntire, etc for connections.

#delete this later-->With UVA building something everyday and the current government budget cuts, UVA better to start hustling and chase them dollas from corporate donors. LOL



###########################################################################################################################
print("========= QUANTITATIVE COMPARATIVE ANALYSIS ========\n")
#from google.colab import drive
#drive.mount('/content/drive')
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go 

df = pd.read_csv('ForeignGifts_edu.csv')

uva_only= df[df["Institution Name"] == "University of Virginia"] 
whole_market= df[df["Institution Name"]!= "University of Virginia"] 

top_4_public_ivies = [
    "University of North Carolina - Chapel Hill",
    "University of Michigan - Ann Arbor",
    "University of California, Los Angeles",
    "University of California, Berkeley"
]
top_public_Ivy=df[df["Institution Name"].isin(top_4_public_ivies)]


##########################################################################################################################
#Top 10 UVA/Market/Peer Gift Amount by Giftor name
uva_top_amt_giftor=uva_only.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
peer_top_amt_giftor=top_public_Ivy.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
market_top_amt_giftor=whole_market.groupby("Giftor Name")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)

print(f"######Top 10 Gift Amount by Giftor for UVA, Peers, and Market#######\n")
print(f"##############UVA:\n")
print(uva_top_amt_giftor)
print(f"##############Peers:\n")
print(peer_top_amt_giftor)
print(f"##############Market:\n")
print(market_top_amt_giftor)


###########################################################################################################################
#Top 10 UVA/Market/Peer Gift Amount by country
uva_top_amt_country=uva_only.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
market_top_amt_country=whole_market.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
peer_top_amt_country=top_public_Ivy.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10) 

print(f"######Top 10 Gift Amount by Country for UVA, Peers, and Market#######\n")
print(f"##############UVA:\n")
print(uva_top_amt_country)
print(f"##############Peers:\n")
print(peer_top_amt_country)
print(f"##############Market:\n")
print(market_top_amt_country)


#################################################################################################################################
#Top 5 UVA/Market/Peer Foreign Country Donors:
uva_top_foreign_donors=uva_only["Country of Giftor"].value_counts().head(5)
market_top_foreign_donors=whole_market["Country of Giftor"].value_counts().head(5)
peer_top_foreign_donors=top_public_Ivy["Country of Giftor"].value_counts().head(5)

print(f"######Top 5 Foreign Country Donors for UVA, Peers, and Market#######\n")
print(f"##############UVA:\n")
print(uva_top_foreign_donors)
print(f"##############Peers:\n")
print(peer_top_foreign_donors)
print(f"##############Market:\n")
print(market_top_foreign_donors)


############################################################################################################################
#Gift type by UVA, Peer, Market
uva_top_gift_types = uva_only["Gift Type"].value_counts()
market_top_gift_types=whole_market["Gift Type"].value_counts()
peer_top_gift_types=top_public_Ivy["Gift Type"].value_counts()

print(f"###### Gift type by UVA, Peer, Market#########\n")
print(f"##############UVA:\n")
print(uva_top_gift_types)
print(f"##############Peers:\n")
print(peer_top_gift_types)
print(f"##############Market:\n")
print(market_top_gift_types)


##############################################################################################################################
#UVA/Market/Peer Means
uva_mean=uva_only["Foreign Gift Amount"].mean()
market_mean=whole_market["Foreign Gift Amount"].mean()
peer_mean=top_public_Ivy["Foreign Gift Amount"].mean()

print(f"###### UVA/Peer/Market Means#######\n")
print(f"##############UVA:\n")
print(uva_mean)
print(f"##############Peers:\n")
print(peer_mean)
print(f"##############Market:\n")
print(market_mean)


#UVA/Market/Peer Medians
uva_median=uva_only["Foreign Gift Amount"].median()
market_median=whole_market["Foreign Gift Amount"].median()
peer_median=top_public_Ivy["Foreign Gift Amount"].median()

print(f"###### UVA/Peer/Market Medians#######\n")
print(f"##############UVA:\n")
print(uva_median)
print(f"##############Peers:\n")
print(peer_median)
print(f"##############Market:\n")
print(market_median)



#UVA/Market/Peer Ranges
uva_range=uva_only["Foreign Gift Amount"].max()-uva_only["Foreign Gift Amount"].min()
market_range=whole_market["Foreign Gift Amount"].max()-whole_market["Foreign Gift Amount"].min()
peer_range=top_public_Ivy["Foreign Gift Amount"].max()-top_public_Ivy["Foreign Gift Amount"].min()

print(f"###### UVA/Peer/Market Ranges#######\n")
print(f"##############UVA:\n")
print(uva_range)
print(f"##############Peers:\n")
print(peer_range)
print(f"##############Market:\n")
print(market_range)


#UVA/Market/Peer Standard Deviations
uva_std=uva_only['Foreign Gift Amount'].std()
market_std=whole_market['Foreign Gift Amount'].std()
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
market_unique=whole_market["Country of Giftor"].nunique()
peer_unique= top_public_Ivy["Country of Giftor"].nunique()

print(f"###### Unique Countries Donating to UVA/Peer/Market#######\n")
print(f"##############UVA:\n")
print(uva_unique)
print(f"##############Peers:\n")
print(peer_unique)
print(f"##############Market:\n")
print(market_unique)


######################################################
#UVA Share of the Market
uva_market_share=((uva_only["Foreign Gift Amount"].sum()/ whole_market["Foreign Gift Amount"].sum()) * 100).round(2)
print(f"###### UVA Share of the Market#######\n")
print(uva_market_share)



###################################################################
##GRAPH

country = "Country of Giftor"

recipi = "Institution Name"

flow = "Foreign Gift Amount"



# 1. Filter for Top Public Ivies

df_filtered = df[df[recipi].isin(top_4_public_ivies)].dropna(subset=[country])


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
