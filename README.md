# tiktok

### Introduction

Advertising is moving from TV commercials to influencer recommendations, and advertising firms are forced to use new methods to price ad placements. Rather than paying for a few ad spots, brands are now paying for a higher volume of small ad spots on influencer social media profiles. It may seem straightforward to offer brand deals based on an influencer's number of followers, but the truth is that not all followings are created equal. Influencers have different engagement rates. If an influencer has 5 million followers with an engagement rate of 5%, they are less valuable than an influencer with 4 million followers with an engagement rate of 30%.

Our project is attempting to predict TikTok influencers engagement rates using metrics that are publicly available on their profile. If we can create a model that gives us more insight than doing a simple calculation of total likes / followers, it would be extremely useful to brands. An accurate model would allow them to see which influencers would be the most profitable to give a sponsorship to based on their predicted engagement metrics.

### Data Collection and Data Cleaning

We initially tried to get our data through APIs, but found that TikTok does a great job of gatekeeping their data. After hours of trying, we eventually settled on a dataset we found online that had in depth metrics about the top 250 TikTokers as of October 24th 2020. This dataset included more than we would have been able to scrape on our own.

We removed a few columns before continuing the analysis. We removed total_views because public profiles don’t display a user’s total views. We didn’t want to build a model upon something that wasn’t an accessible metric in practice. We also removed “Brand Account” and “LGBTQ” because each metric represented less than 10 people.

### Exploratory Data Analysis

For the exploratory data analysis part of the project we started with a correlation plot of the numerical variables in the data. As suspected we found a positive correlation between engagement and likes, along with a negative correlation between engagement and age since TikTok is a platform primarily dominated by young adults. It was surprising to find a negative correlation between engagement and followers. Perhaps those influencers who are very popular have a large number of followers who are inactive or are fake accounts who don’t interact with posts but exist solely to boost follower numbers.

![Engagement by Numeric Features](/assets/engagement_numeric.png)

The next step was displaying in scatterplots the relationship between engagement and the other numerical variables in the data. From these we saw that the relationships between engagement and the other variables were not particularly strong among any of the predictors. We then turned to viewing the relationship between engagement and the categorical variables in the data. After creating side by side boxplots we found that there did not seem to be a significant difference in engagement based on whether or not an influencer is considered famous. We also observed that the gender of the influencer did not seem to have an affect on engagement level. The final boxplot however, revealed that there seems to be a difference in engagement levels based on the influencers ethnicity. On average it appears that latino and white influencers seem to have the highest engagement level, while influencers of south asian descent seem to have the lowest. We found these results to be surprising and at this time are not able to formulate a reasonable hypothesis as to why this is.

![Engagement by Ethnicity](/assets/engagement_eth.png)

### Method and Results

Predicting engagement with a TikTok creator is a regression task, so we identified 4 models to fit on our data. These were Linear Regression, Elastic Net, Random Forest, and K-Nearest Neighbors. Because our data only have roughly 250 observations, we preferred a cross validation approach to prevent overfitting of any of these models rather than utilizing a train-test split. We built a function to construct several pipelines for each model and conduct a GridSearch with cross validation to identify the best-performing combination of parameters for each. Before fitting each model, the pipelines add interactions and polynomial terms for each feature and scale the features, which is especially important for the Elastic Net and K-Nearest Neighbors models.

We evaluated each model on its cross-validated mean squared error and found that the Elastic Net consistently outperformed any other model. The best parameters for that model were an penalty alpha of 0.25, an l1_ratio of 0.3 (telling us that this model uses more of an L2/Ridge penalty than an L1/Lasso Penalty to shrink coefficients), and only including interaction terms of the features.

![RMSE by model](/assets/rmse.png)

As Elastic Net models give easily interpretable results in the form of coefficients, we have an idea of which elements of a creator’s profile most affect their engagement rate. Ethnicity=White, Country=Mexico and Genre=Comedy had the largest positive effect on engagement and Ethnicity=South Asian, Country=India and Genre=Promotion had the largest negative effect on a given creator’s engagement rates.

![Elastic Net Coefficients](/assets/coefs.png)

Determining the reasons for these coefficients falls outside the scope of this project, but it is important to note that the size and age of the dataset leave much to be desired. A larger, more recent dataset could give stronger insights into the elements of a TikTok creator’s profile that most contribute to their engagement, and could be compared to this dataset to see if improvements have been made towards addressing algorithmic racial bias from the platform.

### Conclusion

Our Elastic Net model was able to produce results with a RMSE of 4.2, meaning that the average difference between our prediction and the true engagement rate is close to 4.2%. The engagement range of our dataset goes from 0% to nearly 40%, so these bounds should be taken with a grain of salt. Still this model has potential use in determining advertising rates, helping creators determine areas to improve their engagement, and in understanding the platform as a whole.

Like any analysis, there are some limitations to our findings. First, we analyzed the top 250 most followed TikTokers in October 2020. Some of the smallest accounts in our dataset had about 8 million followers. We cannot assume that our model could predict engagement rates for TikTok users of any size. Additionally, because we used the top 250 TikTokers, our data represents only the most mainstream accounts. We cannot assume that our model could accurately predict engagement rates for niche accounts who’s followers have a different engagement pattern with their content.
