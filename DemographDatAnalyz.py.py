import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[(df['sex']=='Male')]['age'].mean(skipna=True).round(decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'].value_counts(normalize=True).loc['Bachelors']*100).round(decimals=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_ser = df['education'].value_counts()
    higher_education = edu_ser.loc['Bachelors'] + edu_ser.loc['Masters'] + edu_ser.loc['Doctorate']
    lower_education = edu_ser.sum() - higher_education

    # percentage with salary >50K
    high_edu_rich = df[((df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate'))&(df['salary']=='>50K')]
    HER = high_edu_rich['salary'].count()
    higher_education_rich = ((HER / higher_education)*100).round(decimals=1)
    low_edu_rich = df[~((df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate'))&(df['salary']=='>50K')]
    LER = low_edu_rich['salary'].count()
    lower_education_rich = ((LER / lower_education)*100).round(decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df[(df['hours-per-week']==df['hours-per-week'].min())])['hours-per-week'].count()
    num_min_rich = (df[(df['hours-per-week']==df['hours-per-week'].min()) & (df['salary']=='>50K')])['salary'].count()
    rich_percentage = ((num_min_rich / num_min_workers)*100).round(decimals=1)

    # What country has the highest percentage of people that earn >50K?
    earner_country_list = ((df[(df['salary']=='>50K')])['native-country'].value_counts())
    worker_country_list = df['native-country'].value_counts()
    highest_earning_country = (earner_country_list / worker_country_list).idxmax()
    highest_earning_country_percentage = ((earner_country_list / worker_country_list).max()*100).round(decimals=1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['salary']=='>50K') & (df['native-country']=='India')])['occupation'].value_counts().idxmax()

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
