# pages/import_api.py

import requests

class ImportAPI:
    def __init__(self, base_url, token):
        self.url = f"{base_url}/import"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    def import_person(self, person_id):
        """
        Envía una solicitud POST al endpoint con el personId proporcionado.
        """
        payload = [{"personId": person_id}]
        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            return response
        except requests.RequestException as e:
            print(f"[ERROR] Fallo la solicitud: {e}")
            return None
