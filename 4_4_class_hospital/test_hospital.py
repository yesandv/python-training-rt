from hospital import create_hospital_db, Hospital


def test_create_hospital_db():
    hospital_db = create_hospital_db(5)
    assert hospital_db == [1, 1, 1, 1, 1]


def test_get_status():
    patients_db = Hospital([1, 1, 2, 1, 1])
    status = patients_db.get_status(3)
    assert status == "Близок к выздоровлению"


def test_positive_change_of_status():
    patients_db = Hospital([1, 1, 2, 1, 1])
    patients_db.change_status(3, 1)
    assert patients_db._patients_db == [1, 1, 3, 1, 1]


def test_negative_change_of_status():
    patients_db = Hospital([1, 1, 3, 1, 1])
    patients_db.change_status(5, -1)
    assert patients_db._patients_db == [1, 1, 3, 1, 0]


def test_remove_patient():
    patients_db = Hospital([1, 1, 3, 1, 0])
    patients_db.remove_patient(3)
    assert patients_db._patients_db == [1, 1, 1, 0]


def test_add_patient_1():
    patients_db = Hospital([1, 1, 1, 0])
    patients_db.add_patient()
    assert patients_db._patients_db == [1, 1, 1, 0, 1]


def test_add_patient_2():
    patients_db = Hospital([1, 1, 1, 0])
    patients_db.add_patient(0)
    assert patients_db._patients_db == [1, 1, 1, 0, 0]
