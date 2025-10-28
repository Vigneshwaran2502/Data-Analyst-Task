# Task 6: Exploratory Data Analysis (EDA) of the Global Terrorism Database

This repository contains the completed project for Task 6 of the Data Analyst Internship, focusing on performing an Exploratory Data Analysis (EDA) on the Global Terrorism Database (GTD).

## 📝 Objective

The goal of this task was to load, clean, and analyze the massive `terror.csv` dataset to uncover initial patterns, trends, and insights. This analysis serves as a foundational step for any deeper investigation, demonstrating the ability to handle a large dataset and derive meaning from it.

## 🛠️ Tools Used

* **Python**
* **Jupyter Notebook** (for interactive analysis and reporting)
* **Pandas** (for data loading, cleaning, and manipulation)
* **Matplotlib** & **Seaborn** (for data visualization)

## 📊 EDA Process

1.  **Load Data:** The `terror.csv` file (over 180,000 rows) was loaded into a Pandas DataFrame, using the `ISO-8859-1` encoding to handle special characters.
2.  **Clean Data:**
    * Selected 10 key columns (e.g., `iyear`, `country_txt`, `attacktype1_txt`, `nkill`, `nwound`) from the original 135 columns to simplify the analysis.
    * Renamed columns to be more readable (e.g., `iyear` $\rightarrow$ `Year`).
    * Handled missing values: `nkill` and `nwound` were filled with `0`.
    * Created a new feature, `Casualties`, by adding `Killed` and `Wounded` together.
3.  **Univariate Analysis:** Analyzed single variables to find frequencies.
    * Charted the most common attack types.
    * Charted the most frequently attacked regions.
4.  **Bivariate Analysis:** Analyzed two variables together to find relationships.
    * Plotted total casualties over time (by `Year`).
    * Plotted total casualties by `Region`.

## 💡 Key Findings

The analysis of the notebook reveals several key insights:

* **Most Common Attack Type:** "Bombing/Explosion" is the most frequent method of attack, followed by "Armed Assault."
* **Most Affected Regions:** The "Middle East & North Africa" and "South Asia" are the two most attacked regions.
* **Trend Over Time:** There was a dramatic and sharp increase in total casualties (killed + wounded) starting around 2011 and peaking between 2014-2017.
* **Casualties by Region:** The "Middle East & North Africa" region not only experiences the most attacks but also suffers from the highest number of total casualties.

## 📂 Files in this Repository

1.  **`[Your-Notebook-Name].ipynb` (Deliverable):** The Jupyter Notebook file containing all the Python code, analysis, visualizations, and written insights.
2.  **`terror.csv`:** The raw dataset used for this analysis.

## Output
1. <img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/f10da88d-0832-45e9-a8cd-d5404ebbd664" />
2. <img width="1000" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/cb4b63aa-8c9c-46eb-87d6-f71d8e113c34" />
3.<img width="1200" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/33d5084b-f6cd-44ea-8434-ae18fd10e9a0" />
4.<img width="1000" height="600" alt="Figure_4" src="https://github.com/user-attachments/assets/f680b6aa-366e-4309-b8fb-307f3144b3f0" />

