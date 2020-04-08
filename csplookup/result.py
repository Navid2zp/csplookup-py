from .errors import ParseError, ServerError, NoAPIKey, DailyLimitReached, InactiveKey, InvalidIp, InvalidKey, \
    MonthlyLimitReached, UnknownError, ExpiredKey, NoIpProvided, MaxLimitReached


# TODO: object result
class LookupResult:
    def __init__(self, raw_result):
        self.result = raw_result
        self.json_data = None

    def _set_json_data(self):
        if not self.json_data:
            self.json_data = self.result.json()

    def get_json(self):
        self._set_json_data()
        return self.json_data

    def get_country_code(self):
        self._set_json_data()
        try:
            return self.result["Result"]["Country"]["IsoCode"]
        except:
            raise ParseError

    def get_country_en_name(self):
        try:
            return self.result["Result"]["Country"]["Names"]["en"]
        except:
            raise ParseError

    def get_city_en_name(self):
        try:
            if self.result["Result"]["Country"]["Names"]:
                return self.result["Result"]["Country"]["Names"]["en"]
            return None
        except:
            raise ParseError

    # checks for api errors and raises one if there is any
    def check_api_errors(self):
        self._set_json_data()

        if "ErrorCode" not in self.json_data or self.json_data.get("ErrorCode") == "":
            return
        try:
            if self.json_data["ErrorCode"] == "SERVER_ERROR":
                raise ServerError
            elif self.json_data["ErrorCode"] == "EXPIRED_KEY":
                raise ExpiredKey
            elif self.json_data["ErrorCode"] == "DAILY_LIMIT_REACHED":
                raise DailyLimitReached
            elif self.json_data["ErrorCode"] == "MONTHLY_LIMIT_REACHED":
                raise MonthlyLimitReached
            elif self.json_data["ErrorCode"] == "MAX_LIMIT_REACHED":
                raise MaxLimitReached
            elif self.json_data["ErrorCode"] == "INVALID_KEY":
                raise InvalidKey
            elif self.json_data["ErrorCode"] == "DEACTIVATED_KEY":
                raise InactiveKey
            elif self.json_data["ErrorCode"] == "INVALID_IP":
                raise InvalidIp
            elif self.json_data["ErrorCode"] == "NO_IP_PROVIDED":
                raise NoIpProvided
            elif self.json_data["ErrorCode"] == "NO_API_KEY":
                raise NoAPIKey
            else:
                raise UnknownError
        except:
            raise ParseError
