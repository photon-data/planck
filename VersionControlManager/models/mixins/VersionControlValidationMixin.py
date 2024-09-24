from django.core.exceptions import ValidationError

class VersionControlValidationMixin:
    def validate_connection_data(self, data):
        print(data)
        try:
            if self.name == 'GitHub':
                self.validate_github_data(data)
            elif self.name == 'Bitbucket':
                self.validate_bitbucket_data(data)
            # Add more conditions for other types as needed
        except ValidationError as e:
            # Gracefully handle the error, maybe log or store it
            print(f"Validation failed: {e}")
            return False  # Indicate validation failure
        return True  # Indicate validation success

    def validate_github_data(self, data):
        required_keys = ['api_token', 'username','organization']
        for key in required_keys:
            if key not in data:
                raise ValidationError(f"Missing required key for GitHub: {key}")

    def validate_bitbucket_data(self, data):
        required_keys = ['username', 'app_password', 'workspace']
        for key in required_keys:
            if key not in data:
                raise ValidationError(f"Missing required key for Bitbucket: {key}")
