# 📺 Streaming by the Numbers: An Excel-lent Netflix Breakdown

Have you ever wondered what makes Netflix tick?

Is it the rush of new titles every month?  
The rise of international content?  
Or maybe the long list of teen dramas we *didn’t* ask for? 😅

This project was born out of curiosity:  
What exactly does Netflix's content universe look like?  
Is it really just rom-coms and crime thrillers?  
Or is there a deeper trend hiding in plain sight?  

By using formulas, pivot tables, and a healthy dose of curiosity, I explored everything from release timelines and genre trends to content ratings and international reach, all within Excel.

Because sometimes, simplicity tells the best story.

Purpose of this project?  
To prove that storytelling through data doesn’t always need fancy tools. It just needs curiosity, creativity, and a well-made pivot table.

---

## 🧠 Project Summary

**Dataset Used:** [Netflix Titles Dataset (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows)

This Excel-based dashboard analyzes over 5,000 Netflix titles across multiple dimensions:
- Type (Movie or TV Show)
- Release Year & Date Added
- Duration
- Country of Origin
- Ratings (TV-MA, PG, etc.)
- Genre Breakdown
- Title Trends Over Time

📌 **Tools Used:** Excel 2021  
📌 **File Type:** `.xlsx`  
📌 **Sheets:** Dashboard View, Statistical Summary, Cleaned Data

---

## 📊 Visual Storytelling in Action

The final dashboard layout [PDF version](netflix_data_analysis.pdf) here walks you through three core questions:

1. **What's the composition of Netflix's content library?**  
   Movies dominate → by volume, by average duration, and even by global spread.

2. **How has Netflix evolved over time?**  
   We see spikes in content acquisition post-2016 (Global Launch) and seasonal additions during Q1.

3. **Where is this content coming from?**  
   While the US still leads, countries like India, UK, and Canada have strong content footprints—highlighting Netflix’s localization efforts.

---

## 🔍 Deep Dive into Key Insights

### 1. 📈 Title Additions by Year
Netflix’s content library grew aggressively after 2016, likely due to its global rollout. The peak around 2019–2020 correlates with rising competition and pre-pandemic content stocking.

### 2. 🗓️ Content Added by Month
The early-year spikes suggest Netflix plans new releases around January & March, perhaps to kick off quarters or fiscal targets.

### 3. 🌍 Top Countries by Production
While the US dominates, there’s a growing share of international content:
- **India** emerges as a key player
- **UK & Canada** show consistent presence
- Globalization isn't a feature—it’s a *strategy*

### 4. 🕒 Duration Analysis
The average movie lasts about 90 minutes, while most TV shows range from 1 to 3 seasons. The dashboard also highlights outliers with unusually long runtimes.

### 5. 📺 Ratings Breakdown
- Most common rating: **TV-MA**, followed by **TV-14**
- Suggests that mature audiences are Netflix’s biggest target group

### 6. 📚 Genre Distribution
From thrillers to teen dramas, documentaries to horror—Netflix has it all. The chart shows the most tagged genres across movies and TV shows.

---

## 📑 Statistical Summary Sheet

In addition to visuals, a dedicated sheet summarizes the dataset :
- Total number of titles
- Most common genre, rating, and country
- Average movie duration
- Release year trends

Each metric is dynamic—calculated using built-in Excel formulas like `MODE`, `AVERAGEIF`, `MAXIFS`, and more.

---

## 🧰 Why Excel?

Many analysts underestimate the power of Excel. This project proves:
- You can do storytelling without writing code
- Advanced charts (Word Clouds, Timeline Charts) are possible
- Excel can *look* good—if you design with purpose

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
- Visual inspiration: Medium article by Subin An, Excel design tricks, and Netflix branding

---

## 📌 Coming Soon (Stretch Goals)

- Add slicers for interactivity  
- Dynamic dashboard using Excel Tables  
- Convert this into a Power BI interactive dashboard  
- Word cloud using VBA or third-party plugin
