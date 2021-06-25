id_status_list = []

patient_status = {0: "Тяжело болен",
                  1: "Болен",
                  2: "Слегка болен",
                  3: "Близок к выздоровлению",
                  4: "Выписать через пару дней",
                  5: "Выписан"}


def set_initial_status_for_patients():
    for i in range(100):
        id_status_list.append(1)


def check_status_of_patients(id_status_list, patient_status, patient_id):
    patient_id += -1
    check_status = patient_status.get(id_status_list[patient_id])
    return check_status


def change_status_of_patients(id_status_list, patient_id, level):
    patient_id += -1
    if level == 1:
        id_status_list[patient_id] += 1
    elif level == -1:
        id_status_list[patient_id] += -1


if __name__ == "__main__":
    id_status_list = []

    patient_status = {0: "Тяжело болен",
                      1: "Болен",
                      2: "Слегка болен",
                      3: "Близок к выздоровлению",
                      4: "Выписать через пару дней",
                      5: "Выписан"}

    for i in range(100):
        id_status_list.append(1)

    number_of_requests = int(input())
    for i in range(number_of_requests):
        request = input()

        if request == "Изменить статус":
            patient_id = int(input()) - 1
            level = int(input())
            if level == 1:
                id_status_list[patient_id] += 1
                new_status = patient_status.get(id_status_list[patient_id])
            elif level == -1:
                id_status_list[patient_id] += -1
                new_status = patient_status.get(id_status_list[patient_id])

        elif request == "Узнать статус":
            patient_id = int(input()) - 1
            check_status = patient_status.get(id_status_list[patient_id])
            print(check_status)
