import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs('plots/diabetes')


diabetes_df = pd.read_csv('diabetes.tab.txt',
                          sep='\s+',
                          header=0)

plt.style.use("fivethirtyeight")

#for the purpose of this assignment, here is the basic 20+ figures

sns.pairplot(diabetes_df, hue='SEX', diag_kind='hist')
plt.tight_layout()
plt.savefig('plots/diabetes/diabetes_pairplot_hue_sex.png')
plt.show()
plt.clf()


#heatmap to better visalize where there is a strong correlation

fig, axes = plt.subplots(figsize=(8,8))
sns.heatmap(diabetes_df.corr(), annot=True, cmap='RdPu')
axes.set_xticklabels(diabetes_df.columns, rotation=45)
axes.set_yticklabels(diabetes_df.columns, rotation=45)
axes.set_title(f'Heatmap for all columns in diabetes dataset')
plt.tight_layout()
plt.savefig('plots/diabetes/heatmap.png')
plt.show()
plt.clf()


#The relationship between BMI and Y (progression of diabetes) along with the BP level of the patient

plt.style.use("dark_background")

fig, axes = plt.subplots(1, 1, figsize=(8, 8))

axes.scatter(diabetes_df['Y'], diabetes_df['BMI'], s=(diabetes_df['BP']) ** 1.2,
             label=f'Y to BMI with BP level', color='w', marker='^', edgecolors='blue', alpha=0.8)

axes.set_xlabel(f'Y')
axes.set_ylabel(f'BMI')
axes.set_title(f'Y, BMI and BP (size)')


axes.legend()
plt.tight_layout()
plt.savefig(f'plots/diabetes/multiplot_scatter_size.png', dpi=300)
plt.show()
plt.clf()



#Comparing S1 and S2 (which are highly correlated) against Y

plt.style.use("dark_background")

fig, axes = plt.subplots(1, 1, figsize=(7, 7))

axes.scatter(diabetes_df['Y'], diabetes_df['S1'], alpha=0.7, label='S1')
axes.scatter(diabetes_df['Y'], diabetes_df['S2'], alpha=0.7, label='S2')


axes.set_xlabel('Y')
axes.set_ylabel('S1 and S2 levels')
axes.set_title(f'S1 & S2 levels compared against Y')
axes.legend()
plt.tight_layout()
plt.show()
plt.clf()



#This figure allows to see how the BP level is higher when the Y (progression of diabetes after one year) is higher, comparing both sexes

plt.style.use("fivethirtyeight")
sns.set()

fig, ax = plt.subplots(figsize=(8,8))

sns.lineplot(x="Y", y="BP",
            hue="SEX", data=diabetes_df)
ax.set_xlabel('Y')
ax.set_ylabel('BP')
ax.set_title(f'BP level as the diabetes progression is higher for both sexes')
ax.legend()
plt.tight_layout()
plt.savefig(f'plots/diabetes/BP_diabetes_progression_sexes.png', dpi=300)
plt.show()

plt.clf()


