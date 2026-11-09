from API.userAPI import userAPI

def test_get_all_user(api_context):
    user = userAPI(api_context)
    response = user.get_user_all()
    assert response.status == 200