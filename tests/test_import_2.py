import pytest

def test_import_bulk_person_ids(api):
    person_ids = [101, 202, 303, 404]

    for pid in person_ids:
        response = api.import_person(pid)
        assert response.status_code == 200, f"Falló con ID: {pid}"
