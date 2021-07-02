class Hospital:
    def __init__(self, patients_db):
        self.__patients_db = patients_db

    def create(self, num_of_patients):
        for i in range(num_of_patients):
            self.__patients_db.append(1)

    def get_status(self, patients_id):
        status_db = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен",
                     3: "Близок к выздоровлению", 4: "Выписать через пару дней", 5: "Выписан"}

        patient_index = patients_id - 1
        status_code = self.__patients_db[patient_index]
        status = status_db.get(status_code)
        return status

    def change_status(self, patients_id, level_up_or_down):
        patients_index = patients_id - 1
        self.__patients_db[patients_index] += level_up_or_down


if __name__ == "__main__":
    patients_db = Hospital([])

    total_num_of_patients = int(input("Укажите сколько всего пациентов в клинике: "))
    patients_db.create(total_num_of_patients)

    number_of_requests = int(input("Укажите кол-во осмотров: "))
    for i in range(number_of_requests):
        request = input("Введите команду: ")

        if request == "Изменить статус":
            patient_id = int(input("Введите id пациента: "))
            level_up_or_down = int(input("Улучшить диагноз (1) или ухудшить диагноз (-1)? "))
            patients_db.change_status(patient_id, level_up_or_down)

        elif request == "Узнать статус":
            patient_id = int(input("Введите id пациента: "))
            status = patients_db.get_status(patient_id)
            print(f'Статус пациента с ID {patient_id}: {status}.')
