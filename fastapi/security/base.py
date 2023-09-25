from fastapi.openapi.models import SecurityBase as SecurityBaseModel

#test
class SecurityBase:
    model: SecurityBaseModel
    scheme_name: str
