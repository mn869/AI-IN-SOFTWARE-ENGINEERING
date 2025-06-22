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
def sort_doctors_by_experience(reverse=False):
    print("\n🩺 Doctors Sorted by Experience:")
    sorted_doctors = sorted(hospital["doctors"], key=lambda d: d["experience"], reverse=reverse)
    for doc in sorted_doctors:
        print(f" - {doc['name']} ({doc['department']}): {doc['experience']} years")
def sort_patients_by_age(reverse=False):
    """Sorts and returns the list of patients by age."""
    print("\n👥 Patients Sorted by Age:")
    sorted_patients = sorted(hospital["patients"], key=lambda p: p["age"], reverse=reverse)
    for patient in sorted_patients:
        print(f" - {patient['name']} (Age: {patient['age']})")
def sort_bills_by_amount(reverse=False):
    """Sorts and returns the list of billing information by amount."""
    print("\n💰 Billing Information Sorted by Amount:")
    sorted_bills = sorted(hospital["billing"], key=lambda b: b["amount"], reverse=reverse)
    for bill in sorted_bills:
        patient = next((p for p in hospital["patients"] if p["id"] == bill["patient_id"]), None)
        if patient:
            status = "Paid" if bill["paid"] else "Unpaid"
            print(f" - {patient['name']} (ID: {patient['id']}): Ksh {bill['amount']} ({status})")
def sort_appointments_by_date(reverse=False):
    """Sorts and returns the list of appointments by date."""
    print("\n📅 Appointments Sorted by Date:")
    sorted_appointments = sorted(hospital["appointments"], key=lambda a: a["date"], reverse=reverse)
    for appointment in sorted_appointments:
        patient = next((p for p in hospital["patients"] if p["id"] == appointment["patient_id"]), None)
        doctor = next((d for d in hospital["doctors"] if d["id"] == appointment["doctor_id"]), None)
        if patient and doctor:
            print(f" - {patient['name']} with {doctor['name']} on {appointment['date']} ({appointment['status']})")
def sort_pharmacy_by_stock(reverse=False):
    """Sorts and returns the list of pharmacy stock by quantity."""
    print("\n💊 Pharmacy Stock Sorted by Quantity:")
    sorted_pharmacy = sorted(hospital["pharmacy"].items(), key=lambda item: item[1]["stock"], reverse=reverse)
    for medicine, details in sorted_pharmacy:
        print(f" - {medicine}: {details['stock']} units (Expiry: {details['expiry']})")                        
def get_doctor_by_department(department):
    """Returns a list of doctors in the specified department."""
    return [doctor for doctor in hospital["doctors"] if doctor["department"] == department]
def get_patient_by_condition(condition):
    """Returns a list of patients with the specified condition."""
    return [patient for patient in hospital["patients"] if patient["condition"].lower() == condition.lower()]
admitted_patients = [patient for patient in hospital["patients"] if patient["admitted"]]
def get_admitted_patients(sort_key=None):
    """Returns a list of admitted patients, optionally sorted by the given key."""
    patients = [patient for patient in hospital["patients"] if patient["admitted"]]
    if sort_key:
        # Check if the key exists in the patient dictionary
        if sort_key in patients[0]:
            return sorted(patients, key=lambda x: x.get(sort_key))
        else:
            print(f"Invalid sort key '{sort_key}'. Showing unsorted list.")
    return patients
def list_doctors_on_duty():
    print("\n👨‍⚕️ Doctors on Duty:")
    for doc in hospital["doctors"]:
        if doc["on_duty"]:
            print(f" - {doc['name']} ({doc['department']})")
def list_nurses():
    print("\n👩‍⚕️ Nurses:")
    for nurse in hospital["nurses"]:
        print(f" - {nurse['name']} (Shift: {nurse['shift']}, Ward: {nurse['ward']})")
def list_departments():
    print("\n🏥 Hospital Departments:")
    for dept in hospital["departments"]:
        print(f" - {dept}")
def list_equipment():
    print("\n🛠️ Hospital Equipment:")
    for equipment, details in hospital["equipment"].items():
        print(f" - {equipment}: {details['quantity']} units ({details['status']})") 
def list_pharmacy_stock():
    print("\n💊 Pharmacy Stock:")
    for medicine, details in hospital["pharmacy"].items():
        print(f" - {medicine}: {details['stock']} units (Expiry: {details['expiry']})")
def list_billing_info():
    print("\n💰 Billing Information:")
    for bill in hospital["billing"]:
        patient = next((p for p in hospital["patients"] if p["id"] == bill["patient_id"]), None)
        if patient:
            status = "Paid" if bill["paid"] else "Unpaid"
            print(f" - {patient['name']} (ID: {patient['id']}): Ksh {bill['amount']} ({status})")
def list_appointments():
    print("\n📅 Appointments:")
    for appointment in hospital["appointments"]:
        patient = next((p for p in hospital["patients"] if p["id"] == appointment["patient_id"]), None)
        doctor = next((d for d in hospital["doctors"] if d["id"] == appointment["doctor_id"]), None)
        if patient and doctor:
            print(f" - {patient['name']} with {doctor['name']} on {appointment['date']} ({appointment['status']})")
def main():
    print("Welcome to the AI-Powered Hospital Management System!\n")
    list_departments()
    list_doctors_on_duty()
    list_nurses()
    list_equipment()
    list_pharmacy_stock()
    list_billing_info()
    list_appointments()
    sort_doctors_by_experience()
    sort_patients_by_age()
    sort_bills_by_amount()
    sort_appointments_by_date()
    sort_pharmacy_by_stock()
    


    while True:
        print("\nOptions:")
        print("1. Get Doctors by Department")
        print("2. Get Patients by Condition")
        print("3. List Admitted Patients")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            dept = input("Enter department name: ")
            doctors = get_doctor_by_department(dept)
            if doctors:
                print(f"\nDoctors in {dept}:")
                for doc in doctors:
                    print(f" - {doc['name']} ({doc['experience']} years of experience)")
            else:
                print(f"No doctors found in {dept}.")
        
        elif choice == "2":
            condition = input("Enter patient condition: ")
            patients = get_patient_by_condition(condition)
            if patients:
                print(f"\nPatients with {condition}:")
                for patient in patients:
                    print(f" - {patient['name']} (Age: {patient['age']})")
            else:
                print(f"No patients found with condition '{condition}'.")
        
        elif choice == "3":
            sort = input("Sort admitted patients by (leave blank for no sort, e.g., 'age' or 'name'): ")
            admitted = get_admitted_patients(sort_key=sort) if sort else get_admitted_patients()
            if admitted:
                print("\nAdmitted Patients:")
                for patient in admitted:
                    print(f" - {patient['name']} (ID: {patient['id']}, Age: {patient['age']})")
            else:
                print("No patients are currently admitted.")
        
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()

