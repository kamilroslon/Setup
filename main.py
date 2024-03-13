import os
from files.qr_code_generator import generate_qr_code
from files.load_from_file import load_general, load_config, load_main_wifi, load_guest_wifi

def run_example():
    config_file = os.path.join(".", "config.yml")
    yaml_data = load_config(config_file)
    general_config = load_general(yaml_data)
    main_ssid = load_main_wifi(yaml_data)
    guest_ssid = load_guest_wifi(yaml_data)

    main_file_output = f"{general_config.project_name}_{main_ssid.ssid_name}.png"
    guest_file_output = f"{general_config.project_name}_{guest_ssid.ssid_name}.png"

    output_qr_code_main = os.path.join("output", main_file_output.replace(" ", "_"))
    output_qr_code_guest = os.path.join("output", guest_file_output.replace(" ", "_"))
    generate_qr_code(main_ssid, general_config, output_qr_code_main, hidden=False)
    generate_qr_code(guest_ssid, general_config, output_qr_code_guest, hidden=False)

    print(general_config)
    print(main_ssid)
    print(guest_ssid)


if __name__ == '__main__':
    run_example()