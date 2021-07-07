from hospital import create_hospital_db, Hospital


def test_create_hospital_db():
    hospital_db = create_hospital_db(5)
    assert hospital_db == [1, 1, 1, 1, 1]


def test_get_status():
    patients_db = Hospital([1, 1, 2, 1, 1])
    status = patients_db.get_status(3)
    assert status == "Близок к выздоровлению"


def test_positive_change_of_status_1():
    patients_db = Hospital([1, 1, 2, 1, 1])
    patients_db.change_status(3, 1)
    assert patients_db._patients_db == [1, 1, 3, 1, 1]


def test_positive_change_of_status_2():
    patients_db = Hospital([1, 1, 3, 1, 1])
    patients_db.change_status(3, 1)
    assert patients_db._patients_db == [1, 1, 1, 1]


def test_negative_change_of_status():
    patients_db = Hospital([1, 1, 3, 1, 1])
    patients_db.change_status(5, -1)
    assert patients_db._patients_db == [1, 1, 3, 1, 0]


def test_remove_patient_1():
    patients_db = Hospital([1, 1, 3, 1, 0])
    patients_db._remove_patient(3)
    assert patients_db._patients_db == [1, 1, 1, 0]


def test_remove_patient_2():
    patients_db = Hospital([1, 0, 3, 1, 1])
    patients_db._remove_patient(2)
    patients_db._remove_patient(3)
    assert patients_db._discharged_patients == 2


def test_add_patient_1():
    patients_db = Hospital([1, 1, 1, 0])
    patients_db.add_patient()
    assert patients_db._patients_db == [1, 1, 1, 0, 1]


def test_add_patient_2():
    patients_db = Hospital([1, 1, 1, 0])
    patients_db.add_patient(status_code=0)
    assert patients_db._patients_db == [1, 1, 1, 0, 0]


def test_add_patient_3():
    patients_db = Hospital([1, 1, 1, 0])
    patients_db.add_patient()
    patients_db.add_patient()
    assert patients_db._new_patients == 2


def test_sum_up():
    patients_db = Hospital([1, 2, 3, 0, 3, 2, 1])
    patients_db._remove_patient(4)
    patients_db.add_patient(0)
    summary = patients_db.sum_up()
    assert summary == "Всего пациентов выписано за смену: 1." \
                      "\nПринято новых пациентов: 1." \
                      "\nОсталось пациентов в клинике: 7." \
                      "\nПациентов с диагнозом «Тяжело болен»: 1." \
                      "\nПациентов с диагнозом «Болен»: 2." \
                      "\nПациентов с диагнозом «Близок к выздоровлению»: 2." \
                      "\nПациентов с диагнозом «Выписать через пару дней»: 2."
