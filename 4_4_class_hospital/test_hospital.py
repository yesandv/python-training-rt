from hospital import Hospital


def test_create_patients_db():
    patients_db = Hospital([])
    patients_db.create(5)
    assert patients_db._Hospital__patients_db == [1, 1, 1, 1, 1]


def test_get_status():
    patients_db = Hospital([1, 1, 2, 1, 1])
    status = patients_db.get_status(3)
    assert status == "Слегка болен"


def test_positive_change_of_status():
    patients_db = Hospital([1, 1, 2, 1, 1])
    patients_db.change_status(3, 1)
    assert patients_db._Hospital__patients_db == [1, 1, 3, 1, 1]


def test_negative_change_of_status():
    patients_db = Hospital([1, 1, 3, 1, 1])
    patients_db.change_status(5, -1)
    assert patients_db._Hospital__patients_db == [1, 1, 3, 1, 0]
