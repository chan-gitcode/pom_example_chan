from playwright.sync_api import APIRequestContext

class BaseAPI:
    def __init__(self, request: APIRequestContext):
        self.request = request