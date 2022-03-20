from enum import Enum

ENCRYPTION_KEY = '1fa7kkp26uNDLqv3S_WW7WjYZXonmygy2ZE8V9VOsBM='
DEFAULT_QR_FILENAME = "qr.png"

ORGANIZATION_TYPE = "organization"
EMPLOYEE_TYPE = "employee"

TYPE_QR_FIELD = "type"
ORG_NAME_QR_FIELD = "org_name"
EMPLOYEE_NAME_QR_FIELD = "employee_name"
ID_QR_FIELD = "id"


class UserType(Enum):
    CUSTOMER = 1
    ORGANIZATION = 2
    EMPLOYEE = 3