import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').age.count().sort_values(ascending=False)

    # What is the average age of men?
    average_age_men = float('{:.1f}'.format(df[df.sex == 'Male'].age.mean()))

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = 100*(df[df['education'] == 'Bachelors']['education'].count()/df['education'].count())
    percentage_bachelors = float('{:.1f}'.format(percentage_bachelors))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df.education.isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~(df.education.isin(['Bachelors','Masters','Doctorate']))]

    # percentage with salary >50K
    higher_rich_count = higher_education[higher_education.salary == '>50K'].age.count()
    higher_education_count = higher_education.age.count()
    higher_education_rich = (higher_rich_count/higher_education_count)*100
    higher_education_rich = float('{:.1f}'.format(higher_education_rich))

    lower_rich_count = lower_education[lower_education.salary == '>50K'].shape[0]
    lower_education_count = lower_education.shape[0]
    lower_education_rich =100*(lower_rich_count/lower_education_count)
    lower_education_rich= float('{:.1f}'.format(lower_education_rich))
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    min_work_rich = num_min_workers[num_min_workers.salary == '>50K'].age.count()
    min_work_count = num_min_workers.age.count()
    rich_percentage = 100*min_work_rich/min_work_count

    # What country has the highest percentage of people that earn >50K?
    high_salary_df = df[df.salary == '>50K']
    country_total = df.groupby('native-country').salary.count()
    high_salary_df = high_salary_df.groupby('native-country').salary.count()

    for country in high_salary_df.index:
      high_salary_df.loc[country] = high_salary_df.loc[country]/country_total.loc[country]
    highest_earning_country_percentage =high_salary_df.max()*100
    highest_earning_country_percentage = float('{:.1f}'.format(highest_earning_country_percentage))
    highest_earning_country = high_salary_df.idxmax()
  
    # Identify the most popular occupation for those who earn >50K in India.
    IN_df = df[df['native-country'] == "India"]
    top_IN_occupation = IN_df[IN_df.salary == '>50K'].occupation.value_counts().idxmax()

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
