Blinkit Sales Analytics Dashboard

An end-to-end data analytics project analyzing Blinkit sales data using Python, Machine Learning, and Power BI.
The project focuses on business insights, customer behavior analysis, and interactive dashboarding.

📌 Project Overview

This project analyzes Blinkit’s sales data to uncover:

Revenue and order trends

Category and product performance

Customer behavior and retention patterns

The final output is an interactive Power BI dashboard supported by a clean data pipeline and feature engineering in Python.

🛠️ Tools & Technologies

Python: Pandas, NumPy, Matplotlib, Seaborn

Machine Learning: Scikit-learn, XGBoost

Visualization: Power BI, DAX

Development: Jupyter Notebook, VS Code

Version Control: Git & GitHub

📂 Repository Structure
blinkit-sales-analytics/
│
├── data/
│   ├── raw/                  # Original datasets
│   └── processed/            # Cleaned & feature-engineered data
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   └── 05_modeling.ipynb
│
├── powerbi/
│   ├── blinkit_sales_dashboard.pbix
│   └── dashboard_screenshots/
│       ├── page1.png
│       ├── page2.png
│       └── page3.png
│
├── reports/
│   └── business_insights.pdf
│
├── requirements.txt
├── README.md
└── .gitignore

📊 Power BI Dashboard

The Power BI dashboard consists of 3 analytical pages:

🔹 Page 1: Executive Overview

Total Revenue, Orders, Customers, AOV

Revenue trend over time

Category-wise revenue analysis

Dynamic slicers for date and category

🔹 Page 2: Sales & Category Performance

Top-performing product categories

Top 10 products by revenue

Revenue contribution share

Cumulative revenue growth

🔹 Page 3: Customer Insights (ML-Aligned)

Total and repeat customer analysis

Customer spend distribution

Recency vs Spend scatter plot for churn and loyalty identification

RFM-style customer behavior insights

📁 Screenshots are provided in powerbi/dashboard_screenshots/ for quick preview.

🔍 Feature Engineering Highlights

Customer-level features

Total spend per customer

Total orders per customer

Recency (days since last order)

Repeat customer flag

Order & delivery features

Order total

Delivery time (minutes)

Delivery distance

These features were later used for EDA, modeling, and dashboard analysis.

Machine Learning 

Several regression models were tested to predict order value:

Model	RMSE	R²
ElasticNet	✅ Best	0.42
Gradient Boosting	Good	0.40
XGBoost	Good	0.38
Random Forest	Moderate	0.36
Linear Regression	Baseline	0.10

The modeling step was used to compare algorithms and validate feature quality.

💡 Key Business Insights

A small segment of repeat customers contributes a large share of revenue

Certain categories consistently outperform others

Customer recency and spend patterns highlight clear churn-risk segments

Revenue growth shows stabilization, indicating a mature demand phase

🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/avi21-lakra/blinkit-sales-analytics.git
cd blinkit-sales-analytics

2️⃣ Install Python dependencies
pip install -r requirements.txt

3️⃣ Run notebooks

Open notebooks in order using Jupyter or VS Code.

4️⃣ Open Power BI Dashboard

Open:

powerbi/blinkit_sales_dashboard.pbix


in Power BI Desktop.

📈 Future Enhancements

RFM scoring and customer segmentation

Churn prediction model

Power BI Service deployment

Automated data refresh pipeline