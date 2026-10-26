from playwright.sync_api import sync_playwright
import pytest
import random
import string, json


@pytest.fixture
def api_context(scope="session"):
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://book.anhtester.com",
            extra_http_headers={"Accept": "application/json"},
        )
        yield request_context
        request_context.dispose()


def random_string(len: int):
    chars = string.ascii_lowercase
    return "".join(random.choices(chars, k=len))


def test_register(api_context):
    email = f"auto{random.randint(1, 100)}@gmail.com"
    name = f"auto{random_string(4)}{random.randint(10,99)}"
    # payload={
    #     "name": name,
    #     "email": email,
    #     "password" : "Test123@" }
    payload = {
        "name": "autotest99",
        "email": "auto99@gmail.com",
        "password": "Test123@",
    }
    response = api_context.post("/api/register", data=payload)
    assert response.status == 201
    print(response.json())


def test_get_all_user(api_context):
    response = api_context.get("/api/user")
    print(response.status)
    assert response.status == 200
    body = response.json()
    print(body)


def test_login(api_context):
    payload = {"email": "auto99@gmail.com", "password": "Test123@"}
    response = api_context.post("/api/login", data=payload)
    assert response.status == 200
    body = response.json()
    token = body["accessToken"]
    with open("tests/token.json", "w") as f:
        json.dump({"accessToken": token}, f, indent=4)


def get_token():
    with open("tests/token.json", "r") as f:
        return json.load(f)["accessToken"]


def test_update_user(api_context):
    token = get_token()
    idupdate = "cmvped0zw0kbt7uw16jlu67yq"
    payload = {
        "address": "123 Hoang Hoa Tham",
        "phone": "12345",
    }
    response = api_context.patch(
        f"/api/user/{idupdate}",
         headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        data=payload
    )
    assert response.status == 201
    body = response.json()
    print(body)
