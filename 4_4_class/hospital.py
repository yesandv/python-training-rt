class Patient:

    def __init__(self, id):
        self.id = id
        self.status_code = 1

    def get_status(self):
        status_db = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен",
                     3: "Близок к выздоровлению", 4: "Выписать через пару дней", 5: "Выписан"}

        status = status_db.get(self.status_code)
        return status

    def change_status_code(self, level):
        self.status_code += level


if __name__ == "__main__":
    patient_db = []

    num_of_patients = int(input("Укажите сколько всего пациентов в клинике: "))

    for i in range(1, num_of_patients + 1):
        patient = Patient(i)
        patient_db.append(patient)

    number_of_requests = int(input("Укажите кол-во осмотров: "))

    for i in range(number_of_requests):
        request = input("Введите команду: ")

        if request == "Изменить статус":
            patient_id = int(input("Введите id пациента: "))
            level = int(input("Улучшить диагноз (1) или ухудшить диагноз (-1)? "))
            for patient in patient_db:
                if patient_id == patient.id:
                    patient.change_status_code(level)
                    break

        elif request == "Узнать статус":
            patient_id = int(input("Введите id пациента: "))
            for patient in patient_db:
                if patient_id == patient.id:
                    print(patient.get_status())
                    break
