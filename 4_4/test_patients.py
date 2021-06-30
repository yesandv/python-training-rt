from patients import get_status_of_patients, change_status_of_patients


def test_check_status_of_patients():
    patients_db = [1, 1, 1, 2, 1]
    status = get_status_of_patients(patients_db, 4)
    assert status == "Слегка болен"


def test_change_status_of_patients_1():
    patients_db = [1, 1, 1, 2, 4]
    change_status_of_patients(patients_db, 5, 1)
    assert patients_db == [1, 1, 1, 2, 5]


def test_change_status_of_patients_2():
    patients_db = [1, 1, 1, 2, 5]
    change_status_of_patients(patients_db, 1, -1)
    assert patients_db == [0, 1, 1, 2, 5]
