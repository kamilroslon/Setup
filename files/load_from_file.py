import yaml
from files.parameters import GeneralParameters, PowerUser, WifiMain, WifiGuest


def load_config(file_path):
    with open(file_path, mode="r") as config_file:
        data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data


def load_general(yaml_data):
    general_location = yaml_data['General']['location']
    general_name = yaml_data['General']['project_name']
    general = GeneralParameters(general_name, general_location)
    return general


def load_main_wifi(yaml_data):
    ssid_name = yaml_data['Wireless_network']['ssid_name']
    ssid_password = yaml_data['Wireless_network']['ssid_password']
    ssid_encryption = yaml_data['Wireless_network']['ssid_encryption']
    hidden = yaml_data['Wireless_network']['hidden']
    main_ssid = WifiMain(ssid_name, ssid_encryption, hidden, ssid_password)
    return main_ssid


def load_guest_wifi(yaml_data):
    ssid_name = yaml_data['Wireless_guest_network']['ssid_name']
    ssid_password = yaml_data['Wireless_guest_network']['ssid_password']
    ssid_encryption = yaml_data['Wireless_guest_network']['ssid_encryption']
    hidden = yaml_data['Wireless_guest_network']['hidden']
    guest_ssid = WifiGuest(ssid_name, ssid_encryption, hidden, ssid_password)
    return guest_ssid
