from patients import create_db_of_patients, get_status_of_patient, change_status_of_patient


def test_create_db_of_patients():
    patients_db = create_db_of_patients(5)
    assert patients_db == [1, 1, 1, 1, 1]


def test_get_status_of_patient():
    patients_db = [1, 1, 1, 2, 1]
    status = get_status_of_patient(patients_db, 4)
    assert status == "Слегка болен"


def test_positive_change_status_of_patient():
    patients_db = [1, 1, 1, 2, 4]
    change_status_of_patient(patients_db, 5, 1)
    assert patients_db == [1, 1, 1, 2, 5]


def test_negative_change_status_of_patient():
    patients_db = [1, 1, 1, 2, 5]
    change_status_of_patient(patients_db, 1, -1)
    assert patients_db == [0, 1, 1, 2, 5]
