# Data Analysis and Visualization with Python

This repository contains a Python script for data analysis and visualization using popular libraries such as Pandas, Matplotlib, and Seaborn. Each line of code is explained below:

1. **Import Python Libraries:** Import essential Python libraries for data analysis and visualization.

2. **Import CSV File:** Read a CSV file ('customers-100000.csv') and store it in a Pandas DataFrame ('df').

3. **Number of Columns and Rows:** Retrieve the dimensions (rows and columns) of the DataFrame using `df.shape`.

4. **Top 5 Rows:** Display the first 5 rows of the DataFrame using `df.head()`.

5. **DataFrame Info:** Provide detailed information about the DataFrame, including data types and missing values, using `df.info()`.

6. **Drop Unrelated/Blank Columns:** Remove the 'Status' and 'unnamed1' columns from the DataFrame using `df.drop()`.

7. **Check for Null Values:** Calculate the sum of null values in each column using `pd.isnull(df).sum()`.

8. **Drop Null Values:** Remove rows with missing values from the DataFrame using `df.dropna()`.

9. **Change Data Type:** Convert the 'Amount' column to an integer data type using `df['Amount'] = df['Amount'].astype('int')`.

10. **Check Data Type:** Check the data type of the 'Email' column using `df['Email'].dtypes`.

11. **DataFrame of All Columns:** Retrieve the list of column names using `df.columns`.

12. **Rename Column:** Rename the 'Marital_Status' column to 'Shaadi' (not applied to the DataFrame) using `df.rename()`.

13. **Describe Data:** Generate summary statistics for numerical columns using `df.describe()`.

14. **Use Describe for Specific Columns:** Generate summary statistics for specific columns using `df[['Email', 'Company', 'Country']].describe()`.

15. **Plot Bar Chart for Gender and Its Count:** Create a bar chart showing the count of each 'Country' value using Seaborn.

16. **Plot Bar Chart for Gender vs. Total Amount:** Create a bar chart showing the total amount vs. gender using Seaborn.

17. **Plot Bar Chart of Gender:** Create a bar chart showing the count of each 'Age Group' value, labeled by counts and differentiated by gender.

18. **Total Amount vs. Age Group:** Create a bar chart showing the total amount vs. 'Age Group'.

19. **Total Number of Orders from Top 10 States:** Create a bar chart showing the total number of orders from the top 10 states.

20. **Total Amount/Sales from Top 10 States:** Create a bar chart showing the total amount/sales from the top 10 states.

21. **Marital Status:** Create a bar chart showing the count of each 'Marital_Status' value, labeled by counts.

22. **Marital Status of Gender:** Create a bar chart showing the sum of 'Amount' for each combination of 'Marital_Status' and 'Gender'.

23. **Occupation:** Create a bar chart showing the count of each 'Occupation' value, labeled by counts.

24. **Total Amount by Occupation:** Create a bar chart showing the total amount for each occupation.

25. **Product Category:** Create a bar chart showing the count of each 'Product_Category' value, labeled by counts.

26. **Total Amount by Product Category:** Create a bar chart showing the total amount for the top 10 product categories.

27. **Total Orders by Product ID:** Create a bar chart showing the total number of orders for the top 10 most sold products.

28. **Top 10 Most Sold Products:** Create a bar chart showing the top 10 most sold products.

 # You can used many files for learning into files directory there are many csv files are located

Feel free to use and modify this code for your own data analysis and visualization projects. If you have any questions or need further assistance, please don't hesitate to ask.
