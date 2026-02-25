import re

with open('index.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    (
        r"From a statistical analysis perspective, raw survey data often contains errors. Missing values can bias results, and straight-lining indicates a lack of engagement, violating the assumption that the data reflects true variability in the population.",
        r"From a statistical analysis perspective, raw survey data often contains errors.\n\n**Missing Values:** Missing data can bias results computationally (e.g., algorithms cannot process `NaN` values) and theoretically (e.g., the missingness might not be random but systematic). Common criteria for missing data dictate replacing or dropping records with > 10% missing values.\n\n**Straight-lining:** This indicates a lack of respondent engagement, violating the fundamental assumption that survey data reflects true variability in a population. A standard criterion is to measure the variance across a subset of items for each respondent; if the variance is 0 (or very close to 0), the respondent likely selected the exact same answer (e.g., all 3s) for every question."
    ),
    (
        r"An outlier is a data point that differs significantly from other observations. In multivariate analysis, a point might not be an outlier in any single variable but could be anomalous when multiple variables are considered together. Mahalanobis Distance evaluates this using the covariance matrix. If the distance exceeds the critical value of the $\chi^2$ distribution, we exclude the case.",
        r"An outlier is a data point that differs significantly from other observations. In multivariate analysis, assumptions revolve around normality and the absence of extreme deviations across combined variables.\n\n**Mahalanobis Distance ($D^2$):** A multidimensional measure calculating how far a data point is from the center of all variables, adjusting for covariance (how variables correlate with each other).\n\n**Criteria & Assumptions:**\n1. The data follows a multivariate normal distribution.\n2. The critical value for identifying an outlier is determined using the $\chi^2$ distribution, with degrees of freedom equivalent to the number of predictor variables ($df = k$).\n3. Commonly, cases with $p < 0.001$ on the $\chi^2$ distribution are deemed multivariate outliers and should be removed to prevent skewed regressions or factor analyses."
    ),
    (
        r"Many parametric statistical tests assume data is normally distributed. Skewness measures the asymmetry of the distribution. Kurtosis measures the \"tailedness.\" If data is non-normal, non-parametric procedures like bootstrapping are required to make accurate inferences.",
        r"**Assumptions of Parametric Tests:** Many statistical procedures (like standard OLS regression) demand that the residuals of the model or the underlying data follow a normal Gaussian distribution.\n\n**Skewness & Kurtosis:**\n- *Skewness* measures the lack of symmetry (e.g., if responses cluster around \"Strongly Agree\"). A general criterion is that skewness should be between -2 and +2.\n- *Kurtosis* measures the \"tailedness\" (heavy or light tails compared to a normal distribution). The criterion for acceptable kurtosis is generally between -3 and +3 for SEM techniques.\n\n**Consequences:** If the data significantly deviates from normality (i.e., fails tests like Shapiro-Wilk where $p < 0.05$), non-parametric alternatives or bootstrapping (resampling the data thousands of times to establish robust standard errors) must be used."
    ),
    (
        r"Internal consistency measures how closely related a set of items are as a group. We calculate Cronbach’s Alpha ($\alpha$) for this; a value $\ge 0.70$ confirms acceptable reliability, indicating the survey questions measure the same underlying construct.",
        r"**Internal Consistency & Reliability:** This essentially assesses random error in the measurement. If a respondent truthfully has a positive \"Brand Image,\" they should score highly on *all* questions measuring Brand Image.\n\n**Cronbach’s Alpha ($\alpha$):**\nCalculates the average correlation among all items measuring a construct.\n- **Criteria:** $\alpha \ge 0.70$ is generally considered acceptable in exploratory management research, while $\alpha \ge 0.80$ is good, and $\alpha \ge 0.90$ is excellent.\n- **Assumption:** This metric assumes unidimensionality (the items measure one and only one underlying latent variable)."
    ),
    (
        r"Convergent validity shows that items that should be related are indeed related. We look for factor loadings $\ge 0.50$. Additionally, $AVE \ge 0.50$ means that on average, the latent construct explains more than half of the variance of its indicators, reducing measurement error.",
        r"While reliability guarantees consistency, **Validity** ensures we are actually measuring the right concept.\n\n**Convergent Validity:** Demonstrates that indicators of a specific construct converge or share a high proportion of variance in common.\n- **Factor Loadings ($\lambda$):** Should ideally be $\ge 0.70$, meaning over 50% ($\lambda^2 = 0.7^2 = 0.49$) of the variance in the indicator is explained by the construct. However, in exploratory studies, loadings $\ge 0.50$ are sometimes retained.\n- **Average Variance Extracted ($AVE$):** The grand mean of the squared loadings. The strict criterion is $AVE \ge 0.50$, indicating the construct explains more than half the variance of its indicators, meaning the variance explained by the construct is greater than the variance explained by measurement error."
    ),
    (
        r"Even if internally consistent, constructs must measure distinct phenomena. Discriminant validity ensures \"Usability\" isn't accidentally measuring the exact same thing as \"Function\". Under the Fornell-Larcker Criterion, $\sqrt{AVE}$ should be greater than its correlation with any other construct.",
        r"**Discriminant Validity:** Ensures that a construct is genuinely distinct from other constructs in the model, both theoretically and empirically. For instance, respondents should be able to distinguish between an item measuring \"Brand Image\" and an item measuring \"Product Function.\"\n\n**Fornell-Larcker Criterion:**\nA stringent statistical test for discriminant validity.\n- **Criteria:** The square root of the Average Variance Extracted ($\sqrt{AVE}$) for a given construct must be strictly *greater* than its highest correlation with any other construct in the model. If it fails this test, the researcher might need to merge the highly correlated constructs or drop confusing survey items."
    ),
    (
        r"Path analysis allows us to evaluate a system of equations. We calculate multi-step paths (e.g., Brand Image $\rightarrow$ Satisfaction $\rightarrow$ Loyalty). This gives a holistic view of the causal mechanisms driving green product adoption.",
        r"Path analysis allows us to evaluate a system of equations simultaneously. We calculate multi-step directional paths (e.g., Brand Image $\rightarrow$ Satisfaction $\rightarrow$ Loyalty).\n\n**Key Assumptions in Path Modeling:**\n1. **Linearity:** The relationships between constructs are linear.\n2. **No Endogeneity:** Error terms are mutually independent, and no unmeasured variables are skewing the modeled relationships.\n3. **Causal Direction:** The flow of arrows is grounded in strong theoretical reasoning (e.g., logic dictates Brand Image precedes Satisfaction, not vice versa).\n\nThis provides a holistic view of the causal mechanisms driving green product adoption."
    ),
    (
        r"Hypothesis testing uses sample data to decide whether to reject the null hypothesis. We evaluate the t-statistics and p-values ($p$). A relationship is statistically significant if $p < 0.05$ (or $t > 1.96$), proving the construct affects the dependent variable.",
        r"Hypothesis testing uses sample data to decide whether to reject a pre-defined null hypothesis (e.g., $H_0$: \"Brand Image has NO effect on Satisfaction\").\n\n**Statistical Criteria:**\n- **p-value ($p$):** The probability of observing the data if the null hypothesis were true. We reject $H_0$ if $p < 0.05$ (at a 95% confidence level).\n- **t-statistic ($t$):** Measures the size of the difference relative to the variation in sample data. The criterion for significance is typically $t > 1.96$ or $t < -1.96$ for a two-tailed test.\n\nRejecting the null hypothesis yields statistical significance, indicating empirical support for the proposed relationship in the model."
    ),
    (
        r"Variables might be measured on shifted subjective scales. Standardized beta coefficients ($\beta$) convert them to standard deviations. Based on your results, $\beta_{BrandImage} > \beta_{Function}$, indicating Brand Image is the primary driver of the green product's success.",
        r"When variables are measured on different units or simply to ascertain relative importance, **Standardized Beta Coefficients ($\beta$)** are used. They rescale the data so every variable has a mean of 0 and a standard deviation of 1.\n\n**Interpretation & Criteria:**\n- A coefficient of $\beta = 0.45$ means that for every 1 standard deviation increase in the predictor, the dependent variable increases by 0.45 standard deviations.\n- By comparing the absolute magnitude of $\beta$ values, researchers can rank the importance of each predictor. For instance, if $\beta_{BrandImage} = 0.60$ and $\beta_{Function} = 0.20$, Brand Image is undeniably the stronger driver of satisfaction."
    ),
    (
        r"A mediating variable translates the effect of an IV into a DV. Does Brand Image increase Loyalty directly, or only because it first increases Satisfaction? This is tested by analyzing the direct path versus the combined indirect paths.",
        r"**Mediation Analysis:** Explores *how* or *why* a particular observed effect occurs. A mediating variable (Satisfaction) sits between an independent variable (Brand Image) and a dependent variable (Loyalty).\n\n**Types of Mediation:**\n- **Full Mediation:** The IV only affects the DV through the mediator. The direct path becomes insignificant when the mediator is introduced.\n- **Partial Mediation:** The IV influences the DV both directly and indirectly through the mediator.\n\n**Criteria for Significance:** Evaluating the indirect path ($a \times b$) using tools like bootstrapping to generate 95% Confidence Intervals. If the interval does not cross zero, the mediation is significant."
    ),
    (
        r"Significance (p-value) tells us an effect exists. Effect size ($f^2$) tells us the magnitude. It measures the change in $R^2$ when a specific IV is omitted. Values of $0.02, 0.15, \text{and } 0.35$ designate small, medium, and large effects.",
        r"While significance tests (p-values) tell us if an effect *exists*, they don't tell us how *meaningful* it is. \n\n**Cohen's Effect Size ($f^2$):** \nDetermines the practical magnitude of predicting one specific endogenous construct.\nCalculated as: $f^2 = \frac{R^2_{included} - R^2_{excluded}}{1 - R^2_{included}}$\n\n**Criteria:**\nAccording to Cohen (1988), effect sizes distinguish relevance:\n- $f^2 \approx 0.02$: Small (but possibly still actionable)\n- $f^2 \approx 0.15$: Medium\n- $f^2 \approx 0.35$: Large (very strong practically significant effect for the business to leverage)"
    ),
    (
        r"While $R^2$ measures in-sample power, predictive relevance ($Q^2$) assesses out-of-sample prediction capabilities. A common procedure is blindfolding, predicting omitted data points. If $Q^2 > 0$, the model has predictive relevance.",
        r"Models should not only explain retroactively ($R^2$) but predict proactively. **Predictive Relevance ($Q^2$)** specifically assesses how well the model predicts out-of-sample data points.\n\n**Blindfolding (Cross-Validation):**\nAn iterative process. The model systematically deletes points in the data matrix, estimates parameters, and attempts to predict the omitted points based on those parameters.\n\n**Criteria:**\n- If $Q^2 > 0$: The model exhibits predictive relevance for a particular endogenous construct.\n- If $Q^2 \le 0$: The model completely lacks predictive capacity and is overfitted to the training data. For business strategy, negative $Q^2$ makes policy decisions derived from the model dangerous."
    )
]

for i, (old, new) in enumerate(replacements):
    if old in text:
        # replace `\n` in python string properly
        new = new.replace(r"\n", "\n")
        text = text.replace(old, new)
        print(f"Replaced {i + 1}/{len(replacements)}")
    else:
        print(f"Failed to find {i + 1}/{len(replacements)}")

with open('index.qmd', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
