import re

class Validation:
    def id_valid_nic(nic: str)-> bool:
        return True
    
    def is_valid_email(email: str) -> bool:
        """Check if the email is valid format."""
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, email):
            return True
        else:
            return False