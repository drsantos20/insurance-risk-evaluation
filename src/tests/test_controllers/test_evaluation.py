from tests.test_controllers.client import client


def test_evaluation_risk():
    body = {
        "age": 33,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2019},
    }
    expected_response = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "economic",
        "life": "regular",
    }
    response = client.post("/insurance/evaluation", json=body)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_evaluation_risk_life_responsible():
    body = {
        "age": 33,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 1],
        "vehicle": {"year": 2019},
    }
    expected_response = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "regular",
        "life": "responsible",
    }
    response = client.post("/insurance/evaluation", json=body)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_evaluation_risk_bad_request():
    body = {
        "age": 33,
        "dependents": 2,
        "house": {"unknown_property": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2019},
    }
    response = client.post("/insurance/evaluation", json=body)
    assert response.status_code == 422

def test_404():
    body = {
        "age": 33,
        "dependents": 2,
        "house": {"unknown_property": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2019},
    }
    response = client.post("/insurance/evaluation-risk", json=body)
    assert response.status_code == 404

