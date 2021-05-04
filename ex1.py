from scipy.stats import shapiro,ttest_rel
import pandas as pd

df=pd.read_csv("glucose.txt", delimiter="\t")

#Calculate difference
df["diff"]=df["Post"]-df["Pre"]

#Test normality
testRes=shapiro(df["diff"])
if testRes.pvalue>0.05:
    print("Assumption of normality stands.\Use normal distribution.")
else:
    print("Assumption of normality rejected.")

#The code will continue with a normal distribution regardless of previous check. If this bothers you feel free to fork the code or to send a pull request that takes this into account.

#Perform t-test to see if two samples are related.
tTest=ttest_rel(df["Pre"], df["Post"])
if tTest.pvalue>0.05:
    print("H0 stands. 100 mg of sugar does not affect glucose-concentration.")
else:
    print("H0 rejected. 100 mg of sugar does affect glucose-concentration.")
