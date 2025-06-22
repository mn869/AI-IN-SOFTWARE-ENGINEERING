hospital = {
    "departments": [
        "Cardiology", "Pediatrics", "Radiology", "Emergency",
        "Orthopedics", "Oncology", "Neurology", "Maternity"
    ],
    
    "doctors": [
        {"id": 1, "name": "Dr. Amina", "department": "Cardiology", "experience": 12, "on_duty": True},
        {"id": 2, "name": "Dr. Brian", "department": "Pediatrics", "experience": 5, "on_duty": False},
        {"id": 3, "name": "Dr. Chao", "department": "Radiology", "experience": 8, "on_duty": True},
        {"id": 4, "name": "Dr. David", "department": "Oncology", "experience": 15, "on_duty": True},
        {"id": 5, "name": "Dr. Esther", "department": "Maternity", "experience": 6, "on_duty": False}
    ],
    
    "nurses": [
        {"name": "Nurse Joy", "shift": "morning", "ward": "Pediatrics"},
        {"name": "Nurse Nancy", "shift": "night", "ward": "Emergency"},
        {"name": "Nurse James", "shift": "evening", "ward": "Oncology"}
    ],
    
    "patients": [
        {"id": 101, "name": "John Doe", "age": 45, "condition": "Hypertension", "admitted": True},
        {"id": 102, "name": "Jane Smith", "age": 6, "condition": "Flu", "admitted": False},
        {"id": 103, "name": "Mary Wanjiku", "age": 29, "condition": "Fracture", "admitted": True},
        {"id": 104, "name": "Peter Njoroge", "age": 72, "condition": "Cancer", "admitted": True},
        {"id": 105, "name": "Faith Mumo", "age": 32, "condition": "Pregnancy", "admitted": False}
    ],
    
    "appointments": [
        {"patient_id": 101, "doctor_id": 1, "date": "2025-06-22", "status": "completed"},
        {"patient_id": 105, "doctor_id": 5, "date": "2025-06-23", "status": "scheduled"},
        {"patient_id": 102, "doctor_id": 2, "date": "2025-06-21", "status": "cancelled"},
        {"patient_id": 104, "doctor_id": 4, "date": "2025-06-24", "status": "scheduled"}
    ],
    
    "equipment": {
        "MRI": {"quantity": 2, "status": "operational"},
        "X-Ray": {"quantity": 4, "status": "under maintenance"},
        "Ventilators": {"quantity": 10, "status": "operational"},
        "ECG Machine": {"quantity": 3, "status": "operational"}
    },
    
    "pharmacy": {
        "Paracetamol": {"stock": 500, "expiry": "2026-01"},
        "Amoxicillin": {"stock": 200, "expiry": "2025-08"},
        "Ibuprofen": {"stock": 300, "expiry": "2024-11"},
        "Insulin": {"stock": 80, "expiry": "2025-02"}
    },
    
    "billing": [
        {"patient_id": 101, "amount": 15000, "paid": True},
        {"patient_id": 103, "amount": 23000, "paid": False},
        {"patient_id": 104, "amount": 120000, "paid": True},
        {"patient_id": 105, "amount": 5000, "paid": False}
    ]
}
def bubble_sort(data, key, reverse=False):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = data[j].get(key)
            b = data[j + 1].get(key)
            if (a > b and not reverse) or (a < b and reverse):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
def sort_hospital_data():
    print("\n🔹 Doctors sorted by experience:")
    sorted_doctors = bubble_sort(hospital["doctors"].copy(), "experience")
    for d in sorted_doctors:
        print(f" - {d['name']}: {d['experience']} yrs")
    print("\n🔹 Patients sorted by age:")
    sorted_patients = bubble_sort(hospital["patients"].copy(), "age")
    for p in sorted_patients:
        print(f" - {p['name']}: {p['age']} yrs")
    print("\n🔹 Appointments sorted by date:")
    sorted_appointments = bubble_sort(hospital["appointments"].copy(), "date")
    for a in sorted_appointments:
        patient = next((p for p in hospital["patients"] if p["id"] == a["patient_id"]), {})
        doctor = next((d for d in hospital["doctors"] if d["id"] == a["doctor_id"]), {})
        print(f" - {patient.get('name', 'Unknown')} with {doctor.get('name', 'Unknown')} on {a['date']} ({a['status']})")
def display_hospital_info():
    print("🏥 Hospital Information System")
    print("🔹 Departments:")
    for dept in hospital["departments"]:
        print(f" - {dept}")
    
    print("\n🔹 Doctors:")
    for doc in hospital["doctors"]:
        status = "On Duty" if doc["on_duty"] else "Off Duty"
        print(f" - {doc['name']} ({doc['department']}, {doc['experience']} yrs, {status})")
    
    print("\n🔹 Nurses:")
    for nurse in hospital["nurses"]:
        print(f" - {nurse['name']} ({nurse['shift']} shift, Ward: {nurse['ward']})")
    
    print("\n🔹 Patients:")
    for patient in hospital["patients"]:
        status = "Admitted" if patient["admitted"] else "Not Admitted"
        print(f" - {patient['name']} ({patient['age']} yrs, Condition: {patient['condition']}, Status: {status})")
    
    print("\n🔹 Appointments:")
    for appointment in hospital["appointments"]:
        patient = next((p for p in hospital["patients"] if p["id"] == appointment["patient_id"]), {})
        doctor = next((d for d in hospital["doctors"] if d["id"] == appointment["doctor_id"]), {})
        print(f" - {patient.get('name', 'Unknown')} with {doctor.get('name', 'Unknown')} on {appointment['date']} ({appointment['status']})")
    
    print("\n🔹 Equipment Status:")
    for equipment, details in hospital["equipment"].items():
        print(f" - {equipment}: {details['quantity']} units, Status: {details['status']}")
    
    print("\n🔹 Pharmacy Stock:")
    for medicine, details in hospital["pharmacy"].items():
        print(f" - {medicine}: {details['stock']} units, Expiry: {details['expiry']}")
    
    print("\n🔹 Billing Information:")
    for bill in hospital["billing"]:
        patient = next((p for p in hospital["patients"] if p["id"] == bill["patient_id"]), {})
        status = "Paid" if bill["paid"] else "Unpaid"
        print(f" - {patient.get('name', 'Unknown')}: Ksh {bill['amount']}, Status: {status}")
if __name__ == "__main__":
    display_hospital_info()
    sort_hospital_data()
    print("\n🏥 End of Hospital Information System")
    