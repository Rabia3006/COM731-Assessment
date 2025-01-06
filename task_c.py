import matplotlib.pyplot as plt
import pandas as pd

def plot_treatment_proportions(df, ethnicity):
    selected_df = df.loc[:,['Ethnicity', 'Treatment']]
    counts = selected_df.query('Ethnicity == @ethnicity').groupby('Treatment').size()
    proportions = counts / counts.sum()

    fig = plt.figure(figsize=(6,6))
    plt.pie(counts, labels = proportions.index, autopct='%1.1f%%', startangle=90)
    plt.title(f"Proportion of Treatments for {ethnicity}s")
    plt.show()

def plot_average_smoking_packs_consumption(df):
    grouped_data=df.groupby(['Ethnicity', 'Stage'])['Smoking_Pack_Years'].mean().unstack()
    fig, ax = plt.subplots(figsize=(6, 6))
    for ethnicity in grouped_data.index:
        ax.plot(grouped_data.columns, grouped_data.loc[ethnicity], marker='o', label=ethnicity)        
    
    ax.set_title('Average Smoking Packs Consumption Across Cancer Stages by Ethnicity') 
    ax.set_xlabel('Cancer Stage') 
    ax.set_ylabel('Average Smoking Packs Consumption')
    ax.legend(title='Ethnicity', fontsize=6)
    plt.show()

def plot_average_blood_pressure(df):
    bp_averages_by_treatment_type = df.groupby('Treatment')[['Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic' , 'Blood_Pressure_Pulse']].mean()
    fig, ax = plt.subplots(figsize=(6, 6)) 

    bp_averages_by_treatment_type['Blood_Pressure_Systolic'].plot(kind='bar', ax=ax, width=0.15, position=0, label='Systolic', color='skyblue') 
    bp_averages_by_treatment_type['Blood_Pressure_Diastolic'].plot(kind='bar', ax=ax, width=0.15, position=1, label='Diastolic', color='salmon')
    bp_averages_by_treatment_type['Blood_Pressure_Pulse'].plot(kind='bar', ax=ax, width=0.15, position=2, label='Pulse', color='red')

    ax.set_title('Average Blood Pressure Types Across Different Treatment Types') 
    ax.set_xlabel('Treatment Types') 
    ax.set_ylabel('Average Blood Pressure') 
    ax.legend(title='BP Type', fontsize=6)
    plt.show()

def plot_average_smoking_consumption_by_age_group(df):
    bins = [30,40,50,60,70,80]
    labels = ['30-40', '40-50', '50-60', '60-70', '70-80']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

    grouped_data = df.groupby(['Age_Group', 'Ethnicity'], observed=True)['Smoking_Pack_Years'].mean().unstack()
    fig, ax = plt.subplots(figsize=(8, 6))

    grouped_data.plot(kind="bar", ax=ax)

    ax.set_title('Average Smoking Packs Consumption by Age Group Across Different Ethnicities') 
    ax.set_xlabel('Age Group') 
    ax.set_ylabel('Average Smoking Packs Consumption') 
    ax.legend(title="Ethnicity", fontsize=6)
    plt.show()
