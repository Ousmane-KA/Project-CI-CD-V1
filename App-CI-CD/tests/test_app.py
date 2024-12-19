import pytest
from app.app import app  # Importe l'application Flask à tester


@pytest.fixture
def client():
    """
    Fixture pour configurer un client de test Flask.
    Permet de tester les endpoints de l'application sans lancer un vrai serveur.
    """
    app.config['TESTING'] = True  # Activer le mode test pour désactiver certaines fonctionnalités comme CSRF.
    with app.test_client() as client:
        yield client


def test_index_status_code(client):
    """
    Teste si le point de terminaison "/" retourne le bon code HTTP.
    """
    response = client.get("/")  # Effectuer une requête GET sur "/"
    assert response.status_code == 200, "La réponse ne retourne pas un statut HTTP 200."


def test_index_content(client):
    """
    Teste si le contenu retourné par le point de terminaison "/" est correct.
    """
    response = client.get("/")  # Effectuer une requête GET sur "/"
    assert b"Bienvenue dans CI/CD Demo avec Flask!" in response.data, \
        "Le contenu attendu n'est pas présent dans la réponse."

