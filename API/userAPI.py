from .base_api import BaseAPI

class userAPI(BaseAPI):
    def get_user_all(self):
        return self.request.get("/api/user")

    def create_user(self, token, payload):
        return self.request.post(
            "/api/user",
            headers={
                "Authorization": f"Bearer {token}"
            },
            data= payload
        )

    def get_user(self, id_user):
        return self.request.get(f"/spi/user/{id_user}")

    def update_user_by_id(self, token, id_user, payload):
        return self.request.patch(
            f"/api/user/{id_user}",
            headers={
                "Authorization": f"Bearer {token}"
            },
            data=payload
        )

    def delete_user_by_id(self, token, id_user):
        return self.request.delete(
            f"/api/user/{id_user}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )