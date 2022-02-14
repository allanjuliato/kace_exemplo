import requests


class Kace():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.org_name = ""
        self.base_url = ""
        self.connect_kace()

    def connect_kace(self):
        self.session = requests.session()
        self.session.headers = {"Accept": "application/json", 
                                "Content-Type": "application/json"}

        login_path = self.base_url + "ams/shared/api/security/login"

        response = self.session.post(login_path, json={
                                     "password": self.password,
                                     "userName": self.username,
                                     "organizationName": self.org_name
                                     })

        self.session.headers = {"Content-Type": "application/json",
                                "x-kace-csrf-token": response.cookies['KACE_CSRF_TOKEN'],
                                "x-kace-api-version": "8"}


    def inventory_all_devices(self):
        machine_path = self.base_url + "api/inventory/machines?shaping=machine all%20all&paging=limit ALL"

        response_machine = self.session.get(machine_path)
        machine_dict = response_machine.json()['Machines']

        return machine_dict

    def inventory_all_barcodes(self):
        barcodes_path = self.base_url + "api/asset/barcodes?shaping=asset all%20all&paging=limit ALL" 

        response_barcodes = self.session.get(barcodes_path)
        barcode_dict = response_barcodes.json()["Barcodes"]

        return barcode_dict

if __name__ == "__main__":
    kace = Kace()

#### RETURN MACHINES ####
    devices = kace.inventory_all_devices()

    #for device in devices:
    #    print(device['Name'])
    
    print(f'Quantos Devices temos no Kace {len(devices)}')

#### RETURN Service Tag ####
    barcodes = kace.inventory_all_barcodes()

    # for st in barcodes:
    #     print(f"Service Tag {st['barcode_data']}")
    
    print(f'Quantos Devices temos no Kace {len(barcodes)}')

