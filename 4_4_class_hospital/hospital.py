def create_hospital_db(num_of_patients):
    hospital_db = []
    for i in range(num_of_patients):
        hospital_db.append(1)
    return hospital_db


class Hospital:
    def __init__(self, patients_db):
        self._patients_db = patients_db
        self._discharged_patients = 0
        self._new_patients = 0
        self._status_db = {0: "Тяжело болен", 1: "Болен", 2: "Близок к выздоровлению", 3: "Выписать через пару дней"}

    def get_status(self, patients_id):
        patient_index = patients_id - 1
        status_code = self._patients_db[patient_index]
        status = self._status_db.get(status_code)
        return status

    def change_status(self, patients_id, level_up_or_down):
        patients_index = patients_id - 1
        self._patients_db[patients_index] += level_up_or_down
        if self._patients_db[patients_index] > 3:
            self._remove_patient(patients_id)

    def _remove_patient(self, patients_id):
        patients_index = patients_id - 1
        del self._patients_db[patients_index]
        self._discharged_patients += 1
        print(f'Пациент с ID {patients_id} выписан.')

    def add_patient(self, status_code=1):
        self._patients_db.append(status_code)
        self._new_patients += 1

    def _get_statistics(self):
        statistics_data_as_dict = {}
        for status in self._status_db.keys():
            if self._patients_db.count(status) > 0:
                statistics_data_as_dict[self._status_db.get(status)] = self._patients_db.count(status)
        return statistics_data_as_dict

    def sum_up(self):
        summary = []
        if self._discharged_patients > 0:
            summary.append(f'Всего пациентов выписано за смену: {self._discharged_patients}.')
        if self._new_patients > 0:
            summary.append(f'Принято новых пациентов: {self._new_patients}.')
        summary.append(f'Осталось пациентов в клинике: {len(self._patients_db)}.')
        statistics = self._get_statistics()
        for status in statistics.keys():
            summary.append(f'Пациентов с диагнозом «{status}»: {statistics.get(status)}.')
        return "\n".join(summary)


if __name__ == "__main__":
    total_num_of_patients = int(input("Укажите сколько всего пациентов в клинике: "))

    hospital_db = create_hospital_db(total_num_of_patients)

    patients_db = Hospital(hospital_db)

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
            print(f'Статус пациента с id {patient_id}: {status}.')

        elif request == "Принять пациента":
            status_code = input("Введите код диагноза нового пациента: ")
            if status_code == "":
                patients_db.add_patient()
            else:
                patients_db.add_patient(int(status_code))

    print(patients_db.sum_up())
