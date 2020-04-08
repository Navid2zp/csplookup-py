# csplookup
Client library for CSP Lookup API.


### Install
```
pip install csplookup
```

### Usage

```python
from csplookup import CSPClient
from csplookup.errors import MaxLimitReached

client = CSPClient(api_key="YOUR_API_KEY")
res = client.lookup("4.2.2.4")

# check for api errors
try:
    res.check_api_errors()
except MaxLimitReached:
    print("max limit reached")
except Exception as err:
    print("other errors")
# NOTE: check errors file for more exceptions

# get json data:
json_data = res.get_json()
print(json_data)
# country code:
print(json_data["Result"]["Country"]["IsoCode"])
# or
print(res.get_country_code())

```

#### Methods

Some helper methods that can help you get the data you need faster:
```python
# get country iso code
print(res.get_country_code())

# get country name (in english):
print(res.get_country_en_name())

# get city name (in english):
print(res.get_city_en_name())
```

License
----

MIT
