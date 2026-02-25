---
title: "Data Science for Management Research"
subtitle: "Case Study: Gogoro Green Product Customer Satisfaction and Loyalty"
format:
  html:
    embed-resources: true
    toc: true
    number-sections: true
jupyter: python3
---

# Introduction to the Course and Scenario

Nowadays, it has been well known that economic growth should be accompanied by the minimization of ecological degradation, as well as attention to social problems. Consequently, an increasing number of companies are working on the development of environmentally friendly products and concepts such as design for green product development, green product design, and green product innovation have come to the forefront.

Prior research has extensively explored consumer motivation for acquiring green products, the profiles of a typical green consumer, and how to orchestrate marketing programs that influence the purchase of green products but there is still little research exploring the customer loyalty of green products. Gogoro is one of the green products which intended to fix the dilemma between the convenience of transportation and ecological degradation in Taiwan. 

The purpose of this study is to take Gogoro as a case to examine the factors that will affect the customer satisfaction and customer loyalty of a green product. A sample of 208 respondents was collected. The results show that function, usability, price, and brand image will affect customer satisfaction significantly. Brand image will affect customer satisfaction most, followed by function. The managerial implication will be discussed based on the results.

# Module 1: Foundations and Study Design

## Section 1: Python Programming Fundamentals

### Objective
To introduce basic Python programming using Visual Studio Code and familiarize students with the data science environment.

### Key Concepts
From a statistical analysis perspective, data needs to be parsed, structured, and manipulated before any modeling can occur. Using Python allows researchers to perform reproducible data manipulations that reduce human error compared to spreadsheet software.

### Python Example Code
```python
import pandas as pd

# Creating a simple dataset of 5 respondents
data = {
    'Respondent_ID': [1, 2, 3, 4, 5],
    'Age': [22, 25, 29, 21, 24],
    'Gogoro_Owner': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
print(df.head())
```

### Student Task
Open Visual Studio Code, create a new file named `StudentName_PythonBasics.py`. Write a short script defining a Python dictionary with three keys (Usability, Price, Function) and 5 fictional numerical values for each. Print the dictionary.

### Evaluation Questions
1. Why is Python advantageous for statistical data manipulation compared to manual entry?
2. What is the role of the pandas library in data analysis?
3. How do you declare a dictionary in Python?
4. What command is used to display output in a Python script?
5. How do you run a Python script inside Visual Studio Code?

## Section 2: Conceptualization & Design

### Objective
To define the research question, independent variables, and dependent variables for the Gogoro case study.

### Key Concepts
In statistical modeling, an Independent Variable (IV) is manipulated or observed to see its effect on the Dependent Variable (DV). The DV is the outcome measured. For the Gogoro case, IVs include function, usability, price, and brand image, while customer satisfaction and loyalty are DVs.

### Python Example Code
```python
# Conceptual mapping of variables
independent_vars = ['Function', 'Usability', 'Price', 'Brand_Image']
dependent_vars = ['Customer_Satisfaction', 'Customer_Loyalty']

total_variables = independent_vars + dependent_vars
print("Variables in our Gogoro study:", total_variables)
print("Number of predictors:", len(independent_vars))
```

### Student Task
Open Visual Studio Code. Create `StudentName_Design.py`. Write a script that lists the variables for a new hypothesis: "Does charging station availability affect usability?". Print the IV and DV for this new hypothesis.

### Evaluation Questions
1. What is an independent variable?
2. What is a dependent variable?
3. In this case study, is Customer Satisfaction an IV or DV?
4. Why is clear conceptualization necessary before statistical testing?
5. How can confusing IVs and DVs impact a regression model?

## Section 3: Data Collection

### Objective
To understand how surveys are used as primary tools for gathering raw data for statistical analysis.

### Key Concepts
Surveys generate categorical or numerical data (like Likert scales) that reflect unobservable psychological constructs like 'brand image'. Statistically, ensuring a sufficient sample size (e.g., 208 respondents) is crucial to have enough power to detect true effects in the population.

### Python Example Code
```python
import numpy as np

# Simulating 208 survey responses for 'Brand Image' on a 1-5 Likert scale
np.random.seed(42)
brand_image_responses = np.random.randint(1, 6, size=208)

print("First 10 survey responses:", brand_image_responses[:10])
print("Total responses collected:", len(brand_image_responses))
```

### Student Task
Create `StudentName_Survey.py` in Visual Studio Code. Simulate 50 survey responses for 'Price_Perception' using an array from 1 to 7. Print the minimum and maximum values of the generated array.

### Evaluation Questions
1. What type of data is typically collected using a Likert scale?
2. Why is sample size important in survey methodology?
3. What does statistical power mean in the context of data collection?
4. What is a construct, and how do surveys help measure it?
5. How can Python be used to simulate survey data for pre-analysis testing?

## Section 4: Data Preparation & Initial Screening

### Objective
To clean raw survey data and calculate descriptive statistics to understand the sample distribution.

### Key Concepts
Before inference, data must be screened. Missing values and outliers can drastically skew standard deviations and means, violating assumptions of generalized linear models. Descriptive statistics summarize the central tendency and dispersion of the Gogoro sample.

### Python Example Code
```python
import pandas as pd
import numpy as np

data = {'Function': [4, 5, np.nan, 4, 5, 20], 'Price': [3, 4, 4, 3, 5, 2]}
df = pd.DataFrame(data)

# Dropping missing values and removing an outlier (>5)
df_clean = df.dropna()
df_clean = df_clean[df_clean['Function'] <= 5]

print("Cleaned Data Descriptive Stats:\n", df_clean.describe())
```

### Student Task
In Visual Studio Code, create `StudentName_Cleaning.py`. Write a script that creates a small dataset with a clear outlier in the 'Usability' column. Write the code to filter out the outlier and print the mean before and after cleaning.

### Evaluation Questions
1. What is an outlier, and how can it affect the mean?
2. Why must missing data be addressed before statistical modeling?
3. Define central tendency.
4. What does standard deviation measure?
5. How does the `describe()` function in pandas assist in initial screening?

# Module 2: Measurement and Scale Validation

## Section 1: Psychometric & Diagnostic Testing Overview

### Objective
To review the concepts of validity and reliability to ensure the survey scales are accurate.

### Key Concepts
Validity tests if a scale measures what it claims to measure (e.g., does our 'Function' scale actually measure functional attributes?). Reliability checks for consistency in responses. Statistically, measurement error must be minimized to ensure the relationships between variables are robust.

### Python Example Code
```python
import pandas as pd

# Creating mock responses for two questions intended to measure the same construct
q1 = [4, 5, 4, 3, 5]
q2 = [4, 4, 4, 2, 5]
consistency_df = pd.DataFrame({'Q1': q1, 'Q2': q2})

correlation = consistency_df['Q1'].corr(consistency_df['Q2'])
print("Correlation between Q1 and Q2:", round(correlation, 2))
```

### Student Task
Create `StudentName_Validity.py` in Visual Studio Code. Generate two lists of 10 identical responses, change one value in the second list, and calculate their correlation. This simulates high reliability.

### Evaluation Questions
1. What is the difference between validity and reliability?
2. Why is measurement error a problem in statistical models?
3. How does high correlation between two questions indicate reliability?
4. Can a survey be reliable but not valid? Explain briefly.
5. In the Gogoro context, how would you face-validate 'Usability'?

## Section 2: Cronbach's Alpha

### Objective
To calculate and interpret Cronbach's alpha as a metric for internal consistency reliability.

### Key Concepts
Cronbach's alpha assesses how closely related a set of items are as a group. A value above 0.70 generally indicates acceptable reliability. Statistically, it is a function of the number of items and the average inter-correlation among the items.

### Python Example Code
```python
import pandas as pd
import numpy as np

def cronbach_alpha(df):
    item_variances = df.var(ddof=1, axis=0)
    total_var = df.sum(axis=1).var(ddof=1)
    n_items = df.shape[1]
    return (n_items / (n_items - 1)) * (1 - (item_variances.sum() / total_var))

mock_data = pd.DataFrame(np.random.randint(3, 6, size=(50, 3)))
print("Cronbach's alpha:", round(cronbach_alpha(mock_data), 3))
```

### Student Task
Create `StudentName_Alpha.py` in Visual Studio Code. Copy the alpha function provided above. Create a DataFrame with 4 columns of random integers (1 to 5) with 100 rows. Calculate and print the Cronbach's alpha.

### Evaluation Questions
1. What does Cronbach's alpha measure?
2. What is generally considered the threshold for an acceptable alpha value?
3. How does the number of items in a survey affect Cronbach's alpha?
4. If an alpha is 0.40, what does this tell you about the survey items?
5. From a statistical perspective, what are we comparing when calculating alpha?

## Section 3: Exploratory Factor Analysis (EFA)

### Objective
To discover the underlying structure of the survey items without predefined constraints.

### Key Concepts
EFA groups variables into underlying constructs (factors) based on shared variance. It uses correlation matrices to identify variables that cluster together. For example, specific survey questions will load heavily onto a single 'Brand Image' factor.

### Python Example Code
```python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

# Simulating 5 variables for 100 respondents
data = pd.DataFrame(np.random.randn(100, 5), columns=['V1', 'V2', 'V3', 'V4', 'V5'])

# Applying PCA as an exploratory tool
pca = PCA(n_components=2)
pca.fit(data)

print("Explained variance ratio by the 2 factors:")
print(pca.explained_variance_ratio_)
```

### Student Task
Create `StudentName_EFA.py` in Visual Studio Code. Generate 3 columns of data with highly correlated values (representing one factor) and print the correlation matrix of this data.

### Evaluation Questions
1. What is the primary goal of Exploratory Factor Analysis?
2. What does a factor loading represent?
3. Why do we look at explained variance in EFA?
4. When would a researcher use EFA rather than CFA?
5. How do Eigenvalues help in deciding how many factors to retain?

## Section 4: Confirmatory Factor Analysis (CFA)

### Objective
To verify if the data fits a specific, theoretically pre-defined measurement model.

### Key Concepts
CFA tests hypotheses about the relationship between observed variables and latent constructs. Unlike EFA, you specify the exact model (e.g., questions 1-3 measure 'Price'). The statistical output provides goodness-of-fit indices (like CFI, RMSEA) to judge model adequacy.

### Python Example Code
```python
# Note: In practice, libraries like semopy are used for actual CFA
# Here we print the conceptual structure to be tested

cfa_model = """
  Function =~ Func1 + Func2 + Func3
  Usability =~ Usab1 + Usab2
"""

print("Model Definition for CFA:")
print(cfa_model)
print("Goal: Check if current data fits these predefined paths.")
```

### Student Task
Create `StudentName_CFA.py` in Visual Studio Code. Define a Python string containing a conceptual measurement model mapping 'Brand_Image' to three variables (BI1, BI2, BI3). Print the string.

### Evaluation Questions
1. How does CFA differ fundamentally from EFA?
2. What is a latent variable in the context of CFA?
3. What is a goodness-of-fit index?
4. Why is CFA important before running a Structural Equation Model?
5. If the model fit in CFA is poor, what should the researcher do next?

# Module 3: Hypothesis Testing and Inferential Statistics

## Section 1: Inferential Statistics & ANOVA

### Objective
To make inferences about the population and compare means across different groups.

### Key Concepts
ANOVA (Analysis of Variance) partitions total variance into variance between groups and variance within groups. An F-test evaluates if the group means are significantly different. It could be used to see if satisfaction differs by age groups of Gogoro users.

### Python Example Code
```python
import scipy.stats as stats

# Satisfaction scores for 3 groups based on income
group1 = [4, 5, 4, 3, 4]
group2 = [5, 5, 4, 5, 5]
group3 = [3, 2, 3, 4, 3]

f_stat, p_val = stats.f_oneway(group1, group2, group3)
print("ANOVA F-statistic:", round(f_stat, 2))
print("P-value:", round(p_val, 3))
```

### Student Task
Create `StudentName_ANOVA.py` in Visual Studio Code. Create two lists of 'Usability' scores for Male and Female respondents. Use `scipy.stats.ttest_ind` to perform an independent t-test (a specific case of ANOVA) and print the p-value.

### Evaluation Questions
1. What is the purpose of inferential statistics?
2. What null hypothesis does an ANOVA test evaluate?
3. How do we interpret the p-value in hypothesis testing?
4. What is the difference between within-group and between-group variance?
5. In what scenario of the Gogoro test case would you use an ANOVA?

## Section 2: Ordinary Least Squares (OLS) Regression

### Objective
To predict an outcome (customer satisfaction) based on multiple continuous predictors.

### Key Concepts
OLS estimates the relationship by minimizing the sum of the squared differences between observed and predicted values. The regression coefficients indicate the strength and direction of the effect. Brand image heavily influences satisfaction based on the case.

### Python Example Code
```python
import pandas as pd
import statsmodels.api as sm

# Mock variables
df = pd.DataFrame({
    'BrandImage': [4, 5, 3, 4, 5],
    'Function': [3, 4, 3, 4, 4],
    'Satisfaction': [4, 5, 3, 4, 5]
})

X = df[['BrandImage', 'Function']]
X = sm.add_constant(X)
y = df['Satisfaction']

model = sm.OLS(y, X).fit()
print(model.summary().tables[1])
```

### Student Task
Create `StudentName_OLS.py` in Visual Studio Code. Run a simple regression predicting 'Loyalty' from 'Satisfaction' using random numeric arrays. Print the coefficient of Satisfaction.

### Evaluation Questions
1. What does OLS strive to minimize?
2. How do you interpret an R-squared value?
3. What does the coefficient of an independent variable tell us?
4. Why must we check for multicollinearity in regression?
5. What does the y-intercept represent in the model?

## Section 3: Logistic Regression

### Objective
To predict binary outcomes, such as whether a customer will repurchase a Gogoro or not.

### Key Concepts
When the dependent variable is binary (e.g., Yes/No), linear regression violates assumptions like homoscedasticity. Logistic regression applies the logit transformation to constrain probabilities between 0 and 1, analyzing the log odds of the outcome.

### Python Example Code
```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# X = Satisfaction scores, y = Repurchase (1=Yes, 0=No)
X = np.array([[3], [4], [2], [5], [4]])
y = np.array([0, 1, 0, 1, 1])

log_reg = LogisticRegression()
log_reg.fit(X, y)

print("Coefficient:", log_reg.coef_[0])
print("Predicted probabilities:", log_reg.predict_proba(X)[:, 1])
```

### Student Task
Create `StudentName_Logistics.py` in Visual Studio Code. Modify the example to include two independent variables (Satisfaction and Price Perception). Fit the logistic regression model and print the predicted classes.

### Evaluation Questions
1. When should logistic regression be used instead of OLS?
2. What are log odds?
3. What is the range of predicted values in a logistic regression model?
4. Give an example of a binary dependent variable in management research.
5. In logistic regression, what replaces R-squared as a measure of fit?

## Section 4: Structural Equation Modeling (SEM)

### Objective
To test complex theoretical relationships, verifying how multiple independent and mediating variables interact simultaneously.

### Key Concepts
SEM combines path analysis and CFA. It allows testing multiple interrelated dependence relationships in a single comprehensive model while estimating measurement error. It is used to test if Satisfaction mediates the path between Brand Image and Loyalty.

### Python Example Code
```python
# High-level representation of SEM syntax typical in Python/semopy
sem_model = """
  # Measurement Model
  Brand =~ B1 + B2
  Satisfaction =~ S1 + S2
  Loyalty =~ L1 + L2
  
  # Structural Model
  Satisfaction ~ Brand
  Loyalty ~ Satisfaction + Brand
"""
print("SEM Model Specification:")
print(sem_model)
```

### Student Task
Create `StudentName_SEM.py` in Visual Studio Code. Write a script that defines a string indicating a structural model where 'Function' and 'Price' predict 'Satisfaction'. Print the string.

### Evaluation Questions
1. What two components typically make up an SEM?
2. What is a mediation effect?
3. Why is SEM preferred over multiple separate OLS regressions for complex models?
4. Can SEM establish definitive causality? Why or why not?
5. What are the key fit indices to report when assessing an SEM model?

# Module 4: Specialized and Advanced Analytics

## Section 1: Time Series Analysis

### Objective
To analyze data collected over chronological sequences to forecast future loyalty or sales trends.

### Key Concepts
Time series data points are non-independent due to temporal alignment. Analysis methods separate trends, seasonality, and cyclic behaviors. Autocorrelation is a key concept, showing how heavily a variable's current value is influenced by its past.

### Python Example Code
```python
import pandas as pd
import numpy as np

# Monthly Gogoro satisfaction scores over 6 months
dates = pd.date_range('2023-01-01', periods=6, freq='M')
scores = [3.8, 3.9, 4.0, 4.2, 4.1, 4.3]

ts_df = pd.DataFrame({'Satisfaction': scores}, index=dates)
print(ts_df)
print("\nScore Difference period-to-period:")
print(ts_df.diff().dropna())
```

### Student Task
Create `StudentName_Time.py` in Visual Studio Code. Create a pandas Series mapping user numbers over 5 years. Calculate and print the percentage change using Python.

### Evaluation Questions
1. Definitionally, how does time series data differ from cross-sectional survey data?
2. What is autocorrelation?
3. What does it mean if a time series has a 'trend'?
4. What does 'seasonality' refer to in management research data?
5. Why are standard regression tools inappropriate for raw time series forecasting?

## Section 2: Clustering Analysis

### Objective
To group similar customers based on unobserved patterns, using an unsupervised learning approach.

### Key Concepts
Clustering maximizes intra-group similarities and inter-group differences without predefined labels (unsupervised). Algorithms like K-means rely on calculating distances (e.g., Euclidean distance) between data points to form green consumer segments.

### Python Example Code
```python
from sklearn.cluster import KMeans
import numpy as np

# Data representing [Age, Income_Scale]
customers = np.array([[22, 3], [24, 4], [45, 8], [50, 9], [23, 3]])

# Apply K-Means
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(customers)

print("Cluster assignments:", kmeans.labels_)
print("Cluster centers:\n", kmeans.cluster_centers_)
```

### Student Task
Create `StudentName_Cluster.py` in Visual Studio Code. Build an array of 6 elements measuring [Function_Score, Price_Score]. Use K-Means to divide them into 3 clusters and print the cluster assignments.

### Evaluation Questions
1. What does it mean that clustering is an 'unsupervised' method?
2. How does the K-Means algorithm conceptually work?
3. How can customer segmentation benefit from clustering?
4. What is Euclidean distance?
5. What happens if you run K-Means but specify 'n_clusters' incorrectly?

## Section 3: Classification Analysis

### Objective
To categorize new survey respondents into predefined classes using supervised learning.

### Key Concepts
Classification uses a labeled dataset to train a model that predicts categories. Algorithms assess boundaries between classes in multi-dimensional space. We can predict if a new respondent will be a "Promoter" or "Detractor" based on function and price variables.

### Python Example Code
```python
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Features: Function, Price. Labels: 0=Detractor, 1=Promoter
X = np.array([[2, 4], [4, 2], [5, 3], [1, 5]])
y = np.array([0, 1, 1, 0])

clf = DecisionTreeClassifier()
clf.fit(X, y)

new_customer = np.array([[4, 4]])
print("Prediction for new customer (4,4):", clf.predict(new_customer))
```

### Student Task
Create `StudentName_Classification.py` in Visual Studio Code. Follow the example to train a decision tree classifier, but modify it to use 3 input features. Predict the class of a new data point and print the result.

### Evaluation Questions
1. How does supervised learning differ from unsupervised learning?
2. Give an example of a classification problem in green product marketing.
3. What is a Decision Tree conceptual basis?
4. Why do we separate data into a training set and a testing set in classification?
5. How can overfitting hurt a classification model's accuracy on new data?

## Section 4: Topic Modeling

### Objective
To extract latent themes or topics from open-ended survey text data.

### Key Concepts
Topic modeling utilizes algorithms like Latent Dirichlet Allocation (LDA) to track the co-occurrence of words. Statistically, it treats documents as mixtures of topics and topics as mixtures of words, allowing us to find out what consumers discuss when reviewing Gogoro.

### Python Example Code
```python
from sklearn.feature_extraction.text import CountVectorizer

reviews = ["Gogoro is eco-friendly", "battery life is great", "eco-friendly transportation"]

# Convert text to a matrix of token counts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("Term Matrix:\n", X.toarray())
```

### Student Task
Create `StudentName_Topic.py` in Visual Studio Code. Create a list of 3 short text feedback sentences about Gogoro's Price. Use the `CountVectorizer` to generate and print the Document-Term Matrix.

### Evaluation Questions
1. What are the inputs to a topic modeling algorithm?
2. How does text analysis benefit management research compared to scaled questions?
3. What is a Document-Term Matrix?
4. Why is step such as removing "stop words" (e.g., 'is', 'the') necessary before modeling?
5. Briefly describe how a 'topic' is represented mathematically in these algorithms.
