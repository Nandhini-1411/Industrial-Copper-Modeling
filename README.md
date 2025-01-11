## Industrial Copper Modeling
This project addresses the challenges faced by the copper industry with skewed and noisy sales and pricing data. It leverages machine learning to predict copper selling prices and classify customer leads (Won or Lost), making it easier to make data-driven decisions.

### Problem Statement
The copper industry deals with sales and pricing data that is often skewed and noisy, which impacts the accuracy of manual predictions. This project aims to solve these problems by building a machine learning solution:
 - Regression model to predict copper selling prices.
 - Classification model to predict whether a customer lead is "Won" or "Lost."

### Data Exploration
 - Missing Values: Handled by removing rows with missing data (1-25 rows out of 180,000).
 - Data Types: Ensured proper data types (dates as datetime, categorical columns as category).
 - Date Issues: Fixed inconsistencies where delivery dates were earlier than order dates by imputing using median lead time.
 - Feature Removal: Dropped columns like material_ref that didn’t add value.
 - Negative Values: Removed rows with negative values to prevent affecting model training.
 - Outlier Treatment: Used the Interquartile Range (IQR) method to cap extreme values.
### Model Building
1.Regression Model (for Selling Price):
  - Tested models: Linear Regression, Decision Tree, Random Forest, and Extra Trees.
  - Fine-tuned the best model using RandomizedSearchCV.
2.Classification Model (for Lead Status):
  - Focused on "Won" or "Lost" statuses.
  - Applied SMOTENC to balance the data.
  - Tested models: Decision Tree, Random Forest, Extra Trees, and Logistic Regression.
    
### Model Evaluation:
Evaluated performance using accuracy score, classification report, and cross-validation.

### Streamlit App:
Built a web app where users can input data to get real-time predictions for either copper selling prices or lead status.

### Technologies Used
  - Python
  - Pandas
  - Scikit-learn
  - Streamlit
  - Pickle
  - Matplotlib/Seaborn (for data visualization)

### Results
  - The machine learning models predict the copper selling price and classify customer leads as 'Won' or 'Lost' with an accuracy of ±15%.
  - The solution simplifies the process of making pricing and lead classification decisions, saving time and improving accuracy.
### Conclusion
This project demonstrates how machine learning can improve decision-making in the copper industry by predicting prices and classifying leads more accurately and efficiently.
