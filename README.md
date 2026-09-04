# Netflix Content Analysis

This project analyzes the Netflix content catalog and visualizes key trends such as:

- Movies vs. TV shows added by year
- Top genres
- Top countries producing content
- Content rating distribution
- Overall movie vs. TV show split

## Files

- `netflix_analysis.py` — Python script that loads the data and creates all charts
- `netflix_titles.csv` — Netflix catalog dataset used for analysis
- `chart1_movies_vs_tv_by_year.png` — Movies vs. TV shows added per year
- `chart2_top_genres.png` — Top 10 genres
- `chart3_top_countries.png` — Top 10 countries producing content
- `chart4_rating_distribution.png` — Rating distribution donut chart
- `chart5_type_split.png` — Overall movie vs. TV show split

## Requirements

Install dependencies with:

```bash
pip install pandas matplotlib seaborn
```

## Run

```bash
python netflix_analysis.py
```

This will generate the chart images in the project folder.

## Dataset

The dataset is based on the public Netflix Titles dataset.
