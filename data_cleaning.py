import pandas as pd
df=pd.read_csv('DataAnalyst.csv')
columns = df.columns

#Drop the unnecessary column
df.drop(columns='Unnamed: 0', inplace=True)

#Clean salary column
df=df[df['Salary Estimate']!='-1']
df['Salary Estimate']=df['Salary Estimate'].apply(lambda x: x.lower().replace('$','').replace('k','').split('(')[0])

#Create max, min and avg salary columns

df['Max_salary']=df['Salary Estimate'].apply(lambda x: int(x.split('-')[1]))
df['Min_salary']=df['Salary Estimate'].apply(lambda x: int(x.split('-')[0]))
df['Avg_salary']=(df['Max_salary']+df['Min_salary'])/2

#Lowercase all the job titles
df['Job Title']=df['Job Title'].str.lower() 

#Create a new column Job Type based on the Job titles
def get_job_type(x):
    if 'health' in x or 'clinical' in x:
        return 'healthcare analyst'
    elif 'management' in x or 'manager' in x:
        return 'management analyst'
    elif 'finance' in x or 'financial' in x:
        return 'financial analyst'
    elif 'business' in x:
        return 'business analyst'
    elif 'operation' in x:
        return 'operations analyst'
    elif 'market' in x:
        return 'marketing analyst'
    elif 'consultant' in x:
        return 'consultant'
    elif 'intern' in x:
        return 'intern'
    elif 'senior' in x or 'sr' in x:
        return 'senior analyst'
    elif 'junior' in x or 'jr' in x:
        return 'junior analyst'
    elif 'scientist' in x or 'science' in x:
        return 'data scientist'
    else:
        return 'data analyst'
df['Job Type']=df['Job Title'].apply(get_job_type)

# Remove ratings from company name
df['Company Name']=df.apply(lambda x: x['Company Name'][:-3] if x.Rating!=-1 else x['Company Name'], axis=1)

#Create a state column
df['State']=df['Location'].str[-2:]
df['Same_state_as_HQ']=df.apply(lambda x: 1 if x['Headquarters'][-2:]==x['State'] else 0, axis=1)

#Find number of competitors
df['Num_of_comp']=df['Competitors'].apply(lambda x: 0 if x=='-1' else x.count(',')+1)

#age of the companies
df['Age']=df['Founded'].apply(lambda x: x if x==-1 else 2021-x)

#Extract information from job description regarding the tools
skills = ['python', 'r', 'tableau', 'sas', 'spark', 'excel', 'splunk', 'sql']
df['Job Description']=df['Job Description'].str.lower()
for sk in skills:
    df[sk]=df['Job Description'].apply(lambda x: int(sk in x.replace(',', ' ').replace(';', ' ').split()))

#Save the cleaned data

df.to_csv('salary_data_cleaned.csv', index=False)

df_cleaned = pd.read_csv('salary_data_cleaned.csv')