# 🔥 SIMPLE LOCAL DATABASE (NO MONGODB)

patients_db = []

def insert_patient(data):
    patients_db.append(data)

def get_patient(patient_id):
    for patient in patients_db:
        if patient["patient_id"] == patient_id:
            return patient
    return None