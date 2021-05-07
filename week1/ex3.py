from scipy.stats import shapiro,ttest_rel
import pandas as pd

df=pd.read_csv("spinach.txt", delimiter="\t")

#Function to test normality
def normality(dataIn, name, value):
    testNormal=shapiro(dataIn)
    if testNormal.pvalue>value:
        print("Assumption of normality stands for "+name+".\nUse normal distribution for "+name+".")
        return 1
    else:
        print("Assumption of normality rejected for "+name+".\nDo not use a normal distribution for "+name+".")
        return 0

#Test normality
normality(df["control"], "control", 0.05)
normality(df["exposed"], "exposed", 0.05)

#The code will continue with a normal distribution regardless of previous check. If this bothers you feel free to fork the code or to send a pull request that takes this into account.

#Perform t-test to see if two samples are related.
tTest=ttest_rel(df["control"], df["exposed"])
print("P-value="+str(tTest.pvalue))
if tTest.pvalue>0.01:
    print("H0 stands. No difference in iron content")
else:
    print("H0 rejected. Difference in iron content.")
