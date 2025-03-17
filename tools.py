from enum import Enum
class RedirectType(Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"

class Redirector:
 

    def redirect(self, url: str, params: dict = None, redirect_type: RedirectType = RedirectType.EXTERNAL):
       pass
