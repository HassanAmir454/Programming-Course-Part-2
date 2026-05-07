class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"{self.name}, {self.age}"


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization
        self.available = True

    def diagnose(self, patient):
        return

    def prescribe_treatment(self):
        pass


class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.medical_history = []

    def add_record(self, record):
        pass


class Appointment:
    def __init__(self, doctor, patient, time):
        self.doctor = doctor
        self.patient = patient
        self.time = time
        self.status = "Scheduled"
        doctor.available = False

    def complete_appointment(self):
        self.status = "Completed"
        self.doctor.avaiable = True

        diagnosis = self.doctor.diagnose(self.patient)
        treatment = self.doctor.prescribe_treatment()

        self.patient.add_record({
            "doctor": self.doctor.name,
            "diagnosis": diagnosis,
            "treatment" : treatment
        })
    
    def __str__(self):
        return f"{self.time} | {self.patient.name} with Dr. {self.doctor.name} [{self.status}]"





class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def find_available_doctor(self, specialization=None):
        if specialization:
            return next((doctor for doctor in self.doctors if doctor.available and doctor.specialiation == specialization), None)
        return next((doctor for doctor in self.doctors if doctor.available), None)

    def book_appointment(self, patient, time, specialization=None):
        doctor = self.find_avaiable_doctor(specialization)

        if not doctor:
            print("No doctor available!")
            return None
        
        appointment = Appointment(doctor, patient, time)
        self.appointments.append(appointment)
        return appointment

    def show_appointments(self):
        for appointment in self.appointments:
            print(appointment)
