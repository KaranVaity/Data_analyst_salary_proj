import pandas as pd
df=pd.read_csv('DataAnalyst.csv')
columns = df.columns

#Drop the unnecessary column
df.drop(columns='Unnamed: 0', inplace=True)

#Clean salary column
df=df[df['Salary Estimate']!=-1]
df['Salary Estimate']=df['Salary Estimate'].apply(lambda x: x.lower().replace('$','').replace('k','').split('(')[0])

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

