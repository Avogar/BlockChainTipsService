from enum import Enum

ENCRYPTION_KEY = b'1fa7kkp9'
DEFAULT_QR_FILENAME = "qr.png"

ORGANIZATION_TYPE = "organization"
EMPLOYEE_TYPE = "employee"

TYPE_QR_FIELD = "type"
ORG_NAME_QR_FIELD = "org_name"
EMPLOYEE_NAME_QR_FIELD = "employee_name"
ID_QR_FIELD = "id"
CHECKSUM_FIELD = "checksum"

PROVIDER_URL = "https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"


class UserType(Enum):
    CUSTOMER = 1
    ORGANIZATION = 2
    EMPLOYEE = 3
