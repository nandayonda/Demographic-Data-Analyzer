import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().values[:]

    # What is the average age of men?
    average_age_men = np.round(df[df['sex']=='Male']['age'].mean(),decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round(len(df[df['education']=='Bachelors'])/len(df)*100,decimals=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')]
    lower_education = df[~(df['education']=='Bachelors')&~(df['education']=='Masters')&~(df['education']=='Doctorate')]

    # percentage with salary >50K
    higher_education_rich = np.round(len(higher_education[higher_education['salary']=='>50K'])/len(higher_education)*100, decimals=1)
    lower_education_rich = np.round(len(lower_education[lower_education['salary']=='>50K'])/len(lower_education)*100, decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week']==min_work_hours]

    rich_percentage = int(len(num_min_workers[num_min_workers['salary']=='>50K'])/len(num_min_workers)*100)

    # What country has the highest percentage of people that earn >50K?
    salary_per_country = df[['native-country','salary']]
    sum_salary_country = salary_per_country['native-country'].value_counts().sort_index(axis=0).to_frame()
    sum_salary_country = sum_salary_country.drop(['Holand-Netherlands', 'Outlying-US(Guam-USVI-etc)'], axis=0).reset_index()
    high_paid_count = salary_per_country[salary_per_country['salary']=='>50K'].value_counts().sort_index(axis=0).to_frame().reset_index()
    total_country = salary_per_country['native-country'].unique()
    rich_country = df.groupby('native-country').size()
    salary_country = pd.DataFrame({
      'Native-Country' : sum_salary_country['index'],
      'people'  : sum_salary_country['native-country'],
      'salary_>50K' : high_paid_count[0]
    })
    salary_country['ptg_high_paid'] = salary_country['salary_>50K']/salary_country['people']
    Clean_country_list = salary_country.sort_values(by='ptg_high_paid', ascending=False)

    highest_earning_country = Clean_country_list[Clean_country_list.ptg_high_paid==Clean_country_list.ptg_high_paid.max()]['Native-Country'].item()
    highest_earning_country_percentage = np.round(Clean_country_list[Clean_country_list.ptg_high_paid==Clean_country_list.ptg_high_paid.max()]['ptg_high_paid'].item()*100,decimals=1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_paid = df[(df['native-country']=='India')&(df['salary']=='>50K')]
    india_popular_occu = india_high_paid['occupation'].value_counts().to_frame().reset_index()
    top_IN_occupation = india_popular_occu[india_popular_occu.occupation==india_popular_occu.occupation.max()]['index'].item()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
