from playwright.sync_api import sync_playwright
import pytest
import random

@pytest.fixture
def api_context(scope="session"):
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url = "https://book.anhtester.com",
            extra_http_headers={
                "Accept" : "application/json"
            }
        )
        yield request_context
        request_context.dispose()

def test_register(api_context):
    email = f"auto{random.randint(1, 100)}@gmail.com"
    payload={
        "name":"autotest 1",
        "email": email,
        "password" : "Test123@" }


    response = api_context.post("/api/register",data=payload)
    assert response.status== 200
    print(response.json())


def test_get_all_user(api_context):
    response = api_context.get("/api/user")
    print(response.status)
    assert response.status == 200
    body = response.json()
    print(body)

