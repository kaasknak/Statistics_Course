from scipy.stats import shapiro
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd

treat1pat=1996
treat2pat=1490
notcure1=135
cured1=treat1pat-notcure1
cured2=1443
notcure2=treat2pat-cured2
#Calculate percentages to compare
perc1cure=cured1/treat1pat
perc2cure=cured2/treat1pat

#Test. Average is set for 0 but since there is not subtraction that seems odd. Not sure how you would perform a subtraction though in this case.
testT=proportions_ztest([notcure1, notcure2], [treat1pat, treat2pat])

print("p_value="+str(testT[1]))

if testT[1]>0.05:
    print("H0 stands. Both treatments are equal.")
else:
    print("H0 rejected. Treatments don't have the same effectiveness.")
