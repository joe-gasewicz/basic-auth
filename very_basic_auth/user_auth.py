from jupyterhub.auth import Authenticator


class TestAuth(Authenticator):

    async def authenticate(self, handler, data=None):
        return None

