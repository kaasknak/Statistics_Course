from scipy.stats import shapiro,ttest_rel
import pandas as pd

#Function to test normality
def normality(dataIn, name, value):
    testNormal=shapiro(dataIn)
    if testNormal.pvalue>value:
        print("Assumption of normality stands for "+name+".\nUse normal distribution for "+name+".")
        return 1
    else:
        print("Assumption of normality rejected for "+name+".\nDo not use a normal distribution for "+name+".")
        return 0

df=pd.read_csv("glucose.txt", delimiter="\t")

#Calculate difference
df["diff"]=df["Post"]-df["Pre"]

#Test normality
normality(df["Post"], "Post", 0.05)
normality(df["Pre"], "Pre", 0.05)
normality(df["diff"], "diff", 0.05)

#The code will continue with a normal distribution regardless of previous check. If this bothers you feel free to fork the code or to send a pull request that takes this into account.

#Perform t-test to see if two samples are related.
tTest=ttest_rel(df["Pre"], df["Post"])
print("P-value="+str(tTest.pvalue))
if tTest.pvalue>0.05:
    print("H0 stands. 100 mg of sugar does not affect glucose-concentration.")
else:
    print("H0 rejected. 100 mg of sugar does affect glucose-concentration.")
