# lib/validations.py

#Helper methods for validation

# Validate for string 
def _validate_string_attribute(self, attribute_name, value):
    """Helper method to validate string-based attributes."""
    if not isinstance(value, str):
        raise ValueError(f"{attribute_name} must be a string.")
    
# Validate for not empty       
def _validate_not_empty_attribute(self, attribute_name, value):
    """Helper method to validate non-empty attributes."""
    if len(value) == 0:
        raise ValueError(f"{attribute_name} must not be empty.")
    
# Validate for not empty string 
def validate_non_empty_string(value):
    """Helper function to validate a non-empty string."""
    return isinstance(value, str) and len(value) >= 1

# Validate inputs
def validate_input(prompt, validation_func, error_message):
    """Reusable function for validating input."""
    while True:
        user_input = str(input(prompt).strip().lower())
        if validation_func(user_input):
            return user_input
        else:
            print(error_message)