class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee

    def display(self):
        print("ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)

    def bill(self):
        return self.fee


p = Patient(1, "Amit", 25, "Fever", 500)

p.display()
print("Total Bill =", p.bill())
