from scipy.stats import shapiro,ttest_1samp
import pandas as pd

treat1pat=1996
treat2pat=1490
notcure1=135
cured1=treat1pat-notcure1
cured2=1443
#Calculate percentages to compare
perc1cure=cured1/treat1pat
perc2cure=cured2/treat1pat

#Test. Average is set for 0 but since there is not subtraction that seems odd. Not sure how you would perform a subtraction though in this case.
testT=ttest_1samp([perc1cure, perc2cure], 0)

if testT.pvalue>0.05:
    print("H0 stands. Both treatments are equal.")
else:
    print("H0 rejected. Treatments don't have the same effectiveness.")
