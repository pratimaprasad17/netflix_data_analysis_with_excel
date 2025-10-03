# 📺 Streaming by the Numbers: An Excel-lent Netflix Breakdown

> _🔍 A data-driven dive into the world of Netflix titles, built entirely in Excel._

### 🧠 Ever wondered what makes Netflix tick?
> Because nothing screams productivity like binge-watching ‘for research’ 🤓🍿

- Is it the **rush of new titles** every month?  
- The rise of **international content** from every corner of the world?  
- Or maybe... the **long list of teen dramas** we *definitely* didn’t ask for? 😅  


### 🔎 What Sparked This Project?

> Curiosity.  
> A spreadsheet.  
> And a dataset that begged to be explored.

I wanted to see what Netflix's content **really** looks like beyond the autoplay thumbnails and trending rows.

- Is it just rom-coms and crime thrillers?  
- What genres dominate which years?  
- Are certain ratings more common?  
- Which countries lead the production game?  

---

## 🧰 Why Excel?
> Because sometimes, the simplest tool tells the most powerful story.

Many analysts underestimate the power of Excel. This project proves:
- You can do storytelling without writing code
- Advanced charts (Word Clouds, Timeline Charts) are possible
- Excel can *look* good, that is, if you design with purpose

### 🎯 The Goal

To prove that **data storytelling doesn’t need fancy tools**.  
It needs curiosity, creativity, and a really well-made pivot table.

> _If you’ve ever doubted Excel’s power for data analysis, this project might just change your mind._

---
## 🧠 Project Summary

> A story told in rows and columns.  
> Over 5,000 Netflix titles, one Excel file, endless insights.

### 📂 **Dataset Used:** [Netflix Titles Dataset (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Netflix’s rise from DVD mail-outs to global streaming giant didn’t just change how we watch — it reshaped content production itself.

This project dives into **Netflix’s complete title library**, using Excel to uncover trends, patterns, and anomalies across:

- 🎬 **Content Type:** Movie vs TV Show  
- 📅 **Release Year** & **Date Added** to platform  
- ⏱️ **Duration Analysis:** From quick bites to epics  
- 🌍 **Country of Origin:** Who’s producing what?  
- 🔞 **Ratings Breakdown:** TV-MA, PG, R... what’s most common?  
- 🎭 **Genre Trends**: Comedy, Drama, Documentary, etc.  
- 📈 **Title Releases Over Time**  


### 🛠️ Tools & Structure

- 📌 **Built With:** Microsoft Excel 2021  
- 📦 **File Type:** `.xlsx`  
- 📑 **Key Sheets:**
  - `📊 Dashboard View` — for clean visuals & summary KPIs  
  - `📈 Statistical Summary` — with formulas & quick metrics  
  - `🧹 Cleaned Data` — refined and ready for analysis  


> _No fancy BI tools. No coding. Just Excel — pushed to its storytelling limit._

---
## 🎯 Who Is This For?

- 📈 **Aspiring Data Analysts** – looking to level up Excel skills using real data  
- 💻 **Non-Coders** – curious about what’s possible without Python or SQL  
- 🧪 **Excel Power Users** – wanting to test their formula, charting, and layout skills  
- 🎬 **Content Nerds** – who want to geek out over Netflix’s global library
---

## 📊 Visual Storytelling in Action

The final dashboard layout covers three core questions:

1. **What's the composition of Netflix's content library?**  
   Movies dominate → by volume, by average duration, and even by global spread.

2. **How has Netflix evolved over time?**  
   We see spikes in content acquisition post-2016 (Global Launch) and seasonal additions during Q1.

3. **Where is this content coming from?**  
   While the US still leads, countries like India, UK, and Canada have strong content footprints → highlighting Netflix’s localization efforts.

### 📈 Visual Sneak Peek
[Netflix Excel Dashboard](netflix_data_analysis.pdf)  
<img width="1518" height="950" alt="image" src="https://github.com/user-attachments/assets/ad5d4449-ec04-4bca-84d1-43dfdbdb68c0" />

---
## 🔍 Deep Dive into Key Insights

### 1. 📈 Title Additions by Year
Netflix’s title count accelerated post-2016, aligning with its global rollout and original content push.
🔹 Peak additions in 2019–2020 suggest pre-pandemic content ramp-up and increased competition.
🔹 Post-2021 saw a slight decline, hinting at either content saturation or strategic shifts.

### 2. 🗓️ Content Added by Month
📌 January and March emerge as peak months for new additions.
This could reflect quarter-based planning cycles or content clustering for audience engagement spikes.

### 3. 🌍 Top Countries by Production
While the United States remains dominant, international creators are steadily rising:

- **🇮🇳 India**: Strong contributor in both films and series, with consistent year-over-year output
- **🇬🇧 United Kingdom**: Continues to deliver high-quality productions, often in collaboration
- **🇨🇦 Canada**: Steady participation in co-productions and regional stories

📌 This underscores Netflix’s shift toward globalized storytelling
> Globalization isn't a feature → it’s a *strategy*

### 4. 🕒 Duration Analysis
- 🎬 Movies: Most fall around 90 minutes, with a bell-curve distribution
- 📺 TV Shows: Typically range between 1–3 seasons, with some outliers
- 📉 Few titles exceed the 180-minute mark or go beyond 5 seasons — highlighting lean content packaging

### 5. 📺 Ratings Breakdown
- 🟣 Most common rating: TV-MA, followed by TV-14
- 📌 Indicates a clear tilt towards mature audience programming
- 📉 Kid-friendly or general audience content makes up a smaller share

### 6. 📚 Genre Distribution
- From thrillers and dramas to stand-up comedy and docuseries, the catalog is rich and wide:
- Drama dominates across both movies and series
- Genres like Horror, Romance, and Documentary also show strong representation
- Many titles feature multiple genres, showcasing content versatility

---

## 📑 Statistical Summary Sheet

In addition to visuals, a dedicated sheet summarizes the dataset :
- Total number of titles
- Most common genre, rating, and country
- Average movie duration
- Release year trends

Each metric is dynamic, calculated using built-in Excel formulas like `MODE`, `AVERAGEIF`, `MAXIFS`, and more.

---

## 📁 File Structure

```bash
📦Netflix-Titles-Excel-Analysis
 ┣ 📊 netflix_titles_data_analysis.xlsx   # Main dashboard with visuals & stats summary
 ┣ 👨‍💻 netflix_timeline_india.py           # Generate netflix timeline
 ┣ 👨‍💻 netflix_word_cloud.py               # Generate word cloud with content description
 ┣ 📄 netfli_data_analysis.pdf            # Final dashboard (print-ready layout)
 ┗ 📖 README.md                           # This document
```

---

## 🎯 What You'll Learn

Whether you're just starting out in data or want to practice storytelling:
- How to use **pivot tables** for fast EDA
- Create impactful **charts in Excel**
- Design a dashboard layout that’s **clean and printable**
- Extract insights from categorical + time-based data

---

## 🙌 Credits

- Dataset: [Netflix Titles on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
---

## 📌 Coming Soon (Stretch Goals)

- Add slicers for interactivity  
- Dynamic dashboard using Excel Tables  
- Convert this into a Power BI interactive dashboard  
- Word cloud using VBA or third-party plugin
