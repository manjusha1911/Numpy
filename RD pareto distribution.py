from numpy import random
# print(random.pareto(a=2,size=(2,3)))
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()