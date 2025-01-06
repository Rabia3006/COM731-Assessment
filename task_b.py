def retrieve_top_3_treatments(df, ethnicity):
    selected_df = df.loc[:,['Survival_Months','Ethnicity','Treatment']]
    return selected_df.query('Survival_Months > 100 & Ethnicity == @ethnicity').groupby('Treatment')['Survival_Months'].mean().sort_values(ascending=False).head(3)

def retrieve_average_white_blood_cell_counts(df, ethnicity):
    selected_df=df.loc[:,['Ethnicity','Treatment','White_Blood_Cell_Count']]
    return selected_df.query('Ethnicity == @ethnicity').groupby('Treatment')['White_Blood_Cell_Count'].mean()

def retrieve_average_smoking_packs(df, tumor_location):
    selected_df=df.loc[:,['Tumor_Location','Treatment','Blood_Pressure_Pulse','Tumor_Size_mm','Smoking_Pack_Years']]
    return selected_df.query('Tumor_Location == @tumor_location & Tumor_Size_mm < 15.0 & Blood_Pressure_Pulse > 90').groupby('Treatment')['Smoking_Pack_Years'].mean()

def retrieve_average_tumor_size(df, ethnicity):
    selected_df=df.loc[:,['Ethnicity', 'Age', 'Smoking_History', 'Tumor_Size_mm','Smoking_Pack_Years', 'Family_History', 'Comorbidity_Heart_Disease', 'Stage']]
    return selected_df.query('Ethnicity == @ethnicity & Age >= 60 & Smoking_Pack_Years > 50 & Family_History == "Yes" & Comorbidity_Heart_Disease == "Yes" & Smoking_History == "Former Smoker"').groupby('Stage')['Tumor_Size_mm'].mean()
