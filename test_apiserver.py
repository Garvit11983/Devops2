import pytest
import requests

# Define the base URL for the FastAPI server
BASE_URL = "http://127.0.0.1:8002"

# Test cases for the API endpoints
testcases = [
    ("add/2/2", 4, "Test addition of 2 and 2"),
    ("subtract/5/3", 2, "Test subtraction of 5 and 3"),
    ("multiply/2/3", 6, "Test multiplication of 2 and 3"),
    ("add/-1/1", 0, "Test addition of -1 and 1"),
    ("multiply/0/5", 0, "Test multiplication by zero")
]

@pytest.mark.parametrize("endpoint, expected, description", testcases)
def test_api(endpoint, expected, description):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    
    # Assert that the response status code is 200
    assert response.status_code == 200, f"Request failed: {description}"
    
    # Assert that the result in the response matches the expected value
    result = response.json().get("result")
    assert result == expected, f"{description}. Expected {expected}, got {result}"

    print(f"Test passed: {description}")
