patients = []

def add_patients():
  name = input("enter patient name: ")
  age = int(input("enter age:"))
  disease = input("enter disease: ")
  
  patient = {
       "name" : name,
        "age" : age,
        "disease" : disease} 

  patients.append(patient)
  print("patient added successfully!")
  print(patients)

def view_patient ():
  if len(patients)==0:
     print("No patient found.")
  else:
    for i, patient in enumerate(patients ,1):
      print("\npatient",i)
      print("name:",patient["name"])
      print("age:",patient["age"])  
      print("disease:",patient["age"]) 
def search_patient():
     name = input("Enter patient name to search: ")
     for patient in patients :
       if patient["name"].lower()==name.lower():
         print("patient found!")
         print("name:",patient["name"])
         print("age:",patient["age"])
         print("disease:", patient["disease"])
         return 

print("patient not found.")

while True :
  print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
  print("1. add patient")
  print("2. view patient")
  print("3. search patient")
  print("4. exit")

  choice = input("enter your choice: ")

  if choice == "1":
    add_patients()

  elif choice =="2":
    view_patient()

  elif choice =="3":
    search_patient()

  elif choice =="4":
    print("Thank you!")
    break
  else:
    print("invalid choice!")
