import pandas as pd
import numpy as np

df = pd.read_csv('adult.data.csv')
# print(df.head())
# df.info()

# race_count = df['race'].value_counts().values[:]
# print(race_count)

# average_age_men = df[df['sex']=='Male']['age'].mean()
# print(average_age_men)

# percentage_bachelors = len(df[df['education']=='Bachelors'])/len(df)
# print(percentage_bachelors)

# show = df[(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')]
# show_1 = show[show['salary']=='>50K']
# val1 = np.round(len(show[show['salary']=='>50K'])/len(show)*100, decimals=1)
# print(val1)

# show_2 = df[~(df['education']=='Bachelors')&~(df['education']=='Masters')&~(df['education']=='Doctorate')]
# val2 = np.round(len(show_2[show_2['salary']=='>50K'])/len(show_2)*100, decimals=1)
# print(val2)

# min_work_hours = df['hours-per-week'].min()
# print(min_work_hours)

# hito_min_work_hours = df[df['hours-per-week']==min_work_hours]
# min_work_hours_salary = int(len(hito_min_work_hours[hito_min_work_hours['salary']=='>50K'])/len(hito_min_work_hours)*100)
# print(min_work_hours_salary)

# salary_per_country = df[['native-country','salary']]
# sum_salary_country = salary_per_country['native-country'].value_counts().sort_index(axis=0).to_frame()
# sum_salary_country = sum_salary_country.drop(['Holand-Netherlands', 'Outlying-US(Guam-USVI-etc)'], axis=0).reset_index()
# high_paid_count = salary_per_country[salary_per_country['salary']=='>50K'].value_counts().sort_index(axis=0).to_frame().reset_index()
# total_country = salary_per_country['native-country'].unique()
# rich_country = df.groupby('native-country').size()
# salary_country = pd.DataFrame({
#   'Native-Country' : sum_salary_country['index'],
#   'people'  : sum_salary_country['native-country'],
#   'salary_>50K' : high_paid_count[0]
# })
# salary_country['ptg_high_paid'] = salary_country['salary_>50K']/salary_country['people']
# print(salary_country.sort_values(by='ptg_high_paid', ascending=False))
# print(salary_country[salary_country.ptg_high_paid==salary_country.ptg_high_paid.max()]['ptg_high_paid'].item())

india_high_paid = df[(df['native-country']=='India')&(df['salary']=='>50K')]
india_popular_occu = india_high_paid['occupation'].value_counts().to_frame().reset_index()
print(india_popular_occu)
print(india_popular_occu[india_popular_occu.occupation==india_popular_occu.occupation.max()]['index'].item())