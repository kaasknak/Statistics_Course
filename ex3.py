from scipy.stats import shapiro,ttest_rel
import pandas as pd

df=pd.read_csv("spinach.txt", delimiter="\t")

#Test normality
testRescontrol=shapiro(df["control"])
testResexposed=shapiro(df["exposed"])
if testRescontrol.pvalue>0.05:
    print("Assumption of normality stands.\nUse normal distribution.")
else:
    print("Assumption of normality rejected.")
if testResexposed.pvalue>0.05:
    print("Assumption of normality stands.\nUse normal distribution.")
else:
    print("Assumption of normality rejected.")

#The code will continue with a normal distribution regardless of previous check. If this bothers you feel free to fork the code or to send a pull request that takes this into account.

#Perform t-test to see if two samples are related.
tTest=ttest_rel(df["control"], df["exposed"])
print("P-value="+str(tTest.pvalue))
if tTest.pvalue>0.05:
    print("H0 stands. No difference in growth")
else:
    print("H0 rejected. Difference in growth.")
