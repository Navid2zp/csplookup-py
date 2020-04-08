
class NoAPIKey(Exception):
    def __str__(self):
        return "no api key provided"


class ServerError(Exception):
    def __str__(self):
        return "server error"


class ExpiredKey(Exception):
    def __str__(self):
        return "api key expired"


class DailyLimitReached(Exception):
    def __str__(self):
        return "daily limit reached"


class MonthlyLimitReached(Exception):
    def __str__(self):
        return "monthly limit reached"


class MaxLimitReached(Exception):
    def __str__(self):
        return "max limit reached"


class NoIpProvided(Exception):
    def __str__(self):
        return "no ip provided"


class InvalidIp(Exception):
    def __str__(self):
        return "invalid ip"


class InvalidKey(Exception):
    def __str__(self):
        return "invalid api key"


class InactiveKey(Exception):
    def __str__(self):
        return "api key is deactivated"


class UnknownError(Exception):
    def __str__(self):
        return "unknown error"


class ParseError(Exception):
    def __str__(self):
        return "error while parsing json data. you might need to update the library"
