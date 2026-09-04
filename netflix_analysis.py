"""
Netflix Content Analysis
-------------------------
A data visualization project exploring trends in Netflix's movie & TV show catalog.
Dataset: netflix_titles.csv (Netflix Movies and TV Shows, public dataset)
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 150

# ----------------------------------------------------------------------
# 1. LOAD & CLEAN DATA
# ----------------------------------------------------------------------
df = pd.read_csv("netflix_titles.csv")

print("Shape:", df.shape)
print(df.isna().sum())

# Drop rows with no country/date_added where needed per-chart (don't blanket drop)
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
df["year_added"] = df["date_added"].dt.year

# ----------------------------------------------------------------------
# CHART 1: Movies vs TV Shows added per year
# ----------------------------------------------------------------------
by_year_type = (
    df.dropna(subset=["year_added"])
    .groupby(["year_added", "type"])
    .size()
    .reset_index(name="count")
)
by_year_type = by_year_type[by_year_type["year_added"] >= 2010]

plt.figure(figsize=(9, 5))
sns.lineplot(data=by_year_type, x="year_added", y="count", hue="type", marker="o", linewidth=2.5)
plt.title("Netflix Content Added Per Year: Movies vs TV Shows", fontsize=13, weight="bold")
plt.xlabel("Year Added to Netflix")
plt.ylabel("Number of Titles")
plt.legend(title="Type")
plt.tight_layout()
plt.savefig("chart1_movies_vs_tv_by_year.png")
plt.close()

# ----------------------------------------------------------------------
# CHART 2: Top 10 Genres
# ----------------------------------------------------------------------
genres = df["listed_in"].dropna().str.split(", ").explode()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(9, 5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="viridis")
plt.title("Top 10 Genres on Netflix", fontsize=13, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("chart2_top_genres.png")
plt.close()

# ----------------------------------------------------------------------
# CHART 3: Top 10 Countries Producing Content
# ----------------------------------------------------------------------
countries = df["country"].dropna().str.split(", ").explode()
top_countries = countries.value_counts().head(10)

plt.figure(figsize=(9, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="mako")
plt.title("Top 10 Countries Producing Netflix Content", fontsize=13, weight="bold")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("chart3_top_countries.png")
plt.close()

# ----------------------------------------------------------------------
# CHART 4: Content Rating Distribution (donut chart)
# ----------------------------------------------------------------------
rating_counts = df["rating"].value_counts().head(8)

plt.figure(figsize=(7, 7))
colors = sns.color_palette("Set2", len(rating_counts))
plt.pie(
    rating_counts.values,
    labels=rating_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor="white"),
)
plt.title("Netflix Content Rating Distribution (Top 8)", fontsize=13, weight="bold")
plt.tight_layout()
plt.savefig("chart4_rating_distribution.png")
plt.close()

# ----------------------------------------------------------------------
# CHART 5: Overall Movies vs TV Shows split
# ----------------------------------------------------------------------
type_counts = df["type"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    type_counts.values,
    labels=type_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#e50914", "#221f1f"],
    wedgeprops=dict(width=0.4, edgecolor="white"),
    textprops=dict(color="black"),
)
plt.title("Movies vs TV Shows on Netflix (Overall)", fontsize=13, weight="bold")
plt.tight_layout()
plt.savefig("chart5_type_split.png")
plt.close()

print("\nAll charts saved.")

# ----------------------------------------------------------------------
# PRINT KEY INSIGHTS
# ----------------------------------------------------------------------
print("\n--- KEY NUMBERS FOR REPORT ---")
print("Total titles:", len(df))
print("Movies:", type_counts.get("Movie", 0), " TV Shows:", type_counts.get("TV Show", 0))
print("Top genre:", top_genres.index[0], top_genres.iloc[0])
print("Top country:", top_countries.index[0], top_countries.iloc[0])
print("Top rating:", rating_counts.index[0], rating_counts.iloc[0])
peak_year = by_year_type.groupby("year_added")["count"].sum().idxmax()
print("Peak content-adding year:", peak_year)
