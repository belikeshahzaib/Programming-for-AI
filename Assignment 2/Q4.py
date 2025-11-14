import pandas as pd, json
df1 = pd.read_csv("titanic_cleaned.csv")
df2 = pd.read_csv("ticket_fares.csv")
mergeData = pd.merge(df1,df2, on = "Ticket", how = "left", suffixes=('',"Fare"))
mergeData
#hypothesis 1
mergeData["Age Group"] = pd.cut(mergeData["Age"]
                                ,bins = [0,12,19,59,100]
                                ,labels=["Child", "Teen", "Adults", "Senior"])
survivalbyGroup = mergeData.groupby(["Sex", "Age Group"])["Survived"].mean() * 100
survivalbyGroup
try:
    with open("reports.txt", "a+") as reportFile:
        reportFile.write("-" * 50)
        reportFile.write(f"\nThe Data supports the Women and Children Hypothesis \nProof:")
        reportFile.write(f"\nSurvival Rate by Groups:\n\n {survivalbyGroup}")
        reportFile.write(f"\nFrom the above data we can see that Women and Children have higher survival rate than Mens, Hence it support this Hypothesis")
        reportFile.write(f"\n")
except Exception as e:
    print("Error", str(e))
survivalByCLass = mergeData.groupby("Pclass")["Survived"].mean() * 100
mergeData["FareBin"] = pd.qcut(mergeData["Fare"], q=4, labels=["Low", "Medium", "High", "Very High"])
survivalByFarebin = mergeData.groupby("FareBin")["Survived"].mean()
try:
    with open("reports.txt", "a+") as reportFile1:
        reportFile1.write("-" * 50)
        reportFile1.write(f"\nThe Data Shows that Wealthy have higher survival Rate\nProof:")
        reportFile1.write(f"\nSurvival Rate by Class:\n\n {survivalByCLass}")
        reportFile1.write(f"\nSurvival Rate by Fare:\n\n {survivalByFarebin} ")
        reportFile1.write(f"\nFrom the above data It is clear that Wealthier had Greater Survival Rate\n")
        reportFile1.write("-" * 50)
except Exception as e:
    print("Error", str(e))
