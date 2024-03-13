from files.password_generator import generate_password

class GeneralParameters:
    def __init__(self, project_name, location):
        self.project_name = project_name
        self.location = location

    def __str__(self):
        config_params = f"Project name: {self.project_name}, Location: {self.location}"
        return config_params

class PowerUser:
    def __init__(self, power_user, power_user_password=None):
        self.power_user = power_user
        if power_user_password is None:
            power_user_password = generate_password()
        self.power_user_password = power_user_password

    def __str__(self):
        config_params = f"Power user: {self.power_user}, password: {self.power_user_password}"
        return config_params

class WifiMain:
    def __init__(self, ssid_name, ssid_encryption, ssid_password=None):
        self.ssid_name = ssid_name
        self.ssid_encryption = ssid_encryption
        if ssid_password is None:
            ssid_password = generate_password()
        self.ssid_password = ssid_password

    def __str__(self):
        config_params = f"Main SSID: {self.ssid_name}, Main SSID Encryption: {self.ssid_encryption}, Main Password: {self.ssid_password}"
        return config_params

class WifiGuest(WifiMain):
    def __init__(self, ssid_name, ssid_encryption, ssid_password):
        super().__init__(ssid_name, ssid_encryption, ssid_password)
        if ssid_password is None:
            ssid_password = generate_password()
        self.ssid_password = ssid_password

    def __str__(self):
        config_params = f"Guest SSID: {self.ssid_name}, Guest SSID Encryption: {self.ssid_encryption}, Guest Password: {self.ssid_password}"
        return config_params