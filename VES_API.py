import requests


class VES():
    def __init__(self, token):
        self.__token = token

    def check_plate(self, num):
        num = self.make_num_valid(num)
        request_json = self.__fetch_plate_details(num)
        return request_json

    def __fetch_plate_details(self, num):
        print(num)
        url = ("https://driver-vehicle-licensing.api.gov.uk/" +
               "vehicle-enquiry/v1/vehicles")
        payload = "{\n\t\"registrationNumber\": \"" + str(num) + "\"\n}"
        headers = {
            'x-api-key': self.__token,
            'Content-Type': 'application/json'
        }
        request = requests.request("POST", url, headers=headers, data=payload)
        request_json = request.json()
        print(request_json)
        return request_json

    def is_int(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def make_num_valid(self, num):
        int_to_string = {
            "1": "I",
            "9": "S"
        }
        string_to_int = {
            "I": "1",
            "S": "9"
        }
        print(num)
        for i in range(0, 2):
            if self.is_int(num[i]):
                num = num[0:i] + str(int_to_string[num[i]]) + num[i+1:]
        for i in range(2, 4):
            if not self.is_int(num[i]):
                num = num[0:i] + str(string_to_int[num[i]]) + num[i+1:]
        for i in range(5, 7):
            if self.is_int(num[i]):
                num = num[0:i] + str(int_to_string[num[i]]) + num[i+1:]
        print(num)
        return num
