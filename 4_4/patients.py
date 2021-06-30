def get_initial_db_of_patients(db, total_num_of_patients):
    for i in range(total_num_of_patients):
        db.append(1)
    return db


def get_status_of_patients(patients_db, patient_id):
    status_db = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен",
                 3: "Близок к выздоровлению", 4: "Выписать через пару дней", 5: "Выписан"}

    patient_index = patient_id - 1

    status_code = patients_db[patient_index]
    status = status_db.get(status_code)
    return status


def change_status_of_patients(patients_db, patient_id, level_up_or_down):
    patient_index = patient_id - 1
    if level_up_or_down == 1:
        patients_db[patient_index] += 1
    elif level_up_or_down == -1:
        patients_db[patient_index] += -1


if __name__ == "__main__":
    patients = []

    num_of_patients = int(input("Укажите сколько всего пациентов в клинике: "))

    patients_db = get_initial_db_of_patients(patients, num_of_patients)

    number_of_requests = int(input("Укажите кол-во осмотров: "))
    for i in range(number_of_requests):
        request = input("Введите команду: ")

        if request == "Изменить статус":
            patient_id = int(input("Введите id пациента: "))
            level = int(input("Положительное или отрицательное изменение? "))
            change_status_of_patients(patients_db, patient_id, level)

        elif request == "Узнать статус":
            patient_id = int(input("Введите id пациента: "))
            status = get_status_of_patients(patients_db, patient_id)
            print(f'Статус пациента с ID {patient_id}: {status}.')
