def retrieve_demographic_information(patient_id, records):
    for record in records:
        if patient_id == int(record[0]):
            return {"Age":record[1], "Gender":record[2], "Smoking_History":record[3], "Ethnicity":record[9]}
    return None

def retrieve_medical_history(ethnicity, records):
    selected_records=[]
    for record in records:
        if ethnicity == record[9]:
            selected_records.append({"Patient_ID": record[0], "Family_History": record[11], "Comorbidity_Diabetes": record[12], "Comorbidity_Kidney_Disease": record[16], "Haemoglobin_Level": record[23]})
    return selected_records

def retrieve_treatment_details(records):
    selected_records=[]
    for record in records:
        if int(record[8]) > 100:
            selected_records.append({"Patient_ID": record[0], "Survival_Months": record[8], "Tumor_Size_mm": record[4], "Tumor_Location": record[5], "Stage": record[6]})
    return selected_records

def retrieve_high_risk_patients(records):
    high_risk_patients=[]
    for record in records:
        if int(record[1]) >= 60 and record[3] == "Former Smoker" and float(record[4]) >= 50 and (record[6] == "Stage III" or record[6] == "Stage IV") and record[11] == "Yes" and record[12] == "Yes" and record[13] == "Yes":
            high_risk_patients.append({"Patient_ID": record[0], "Age": record[1], "Smoking_History": record[3], "Tumor_Size_mm": record[4], "Stage": record[6], "Family_History": record[11], "Comorbidity_Diabetes": record[12], "Comorbidity_Hypertension": record[13]})
    return high_risk_patients
