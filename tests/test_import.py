# tests/test_import.py

def test_import_happy_path(api):
    """
    Prueba el caso exitoso (happy path) con un personId válido.
    """
    person_id = 111  
    response = api.import_person(person_id)

    assert response is not None, "La respuesta es None"
    assert response.status_code == 200, f"Se esperaba 200 pero se recibió {response.status_code}"
    print(f"[INFO] Happy Path: status={response.status_code}, body={response.json()}")


def test_import_sad_path_invalid_id(api):
    """
    Prueba el caso de error (sad path) con un personId inválido (por ejemplo, string).
    """
    person_id = "invalido"  # tipo incorrecto
    response = api.import_person(person_id)

    assert response is not None, "La respuesta es None"
    assert response.status_code >= 400, f"Se esperaba error, pero se recibió status {response.status_code}"
    print(f"[INFO] Sad Path (invalid): status={response.status_code}, body={response.text}")


def test_import_sad_path_missing_id(api):
    """
    Prueba el caso de error (sad path) cuando no se envía personId.
    Se simula pasando None y controlándolo en el método.
    """
    person_id = None
    response = api.import_person(person_id)

    assert response is not None, "La respuesta es None"
    assert response.status_code >= 400, f"Se esperaba error, pero se recibió status {response.status_code}"
    print(f"[INFO] Sad Path (missing): status={response.status_code}, body={response.text}")
