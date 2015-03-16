# simple-beddit
Simple Beddit API wrapper written in Python2.7

## Usage
1. Initialize with beddit user **email** and **password**

   ```python
client = BedditClient.get_auth_client('<email>', '<password>')
```

   or if already has **user_id** and **user_token** from Beddit Server

   ```python
client = BedditClient('<user_id>', '<token>')
```

2. Get a list of sleep data by calling **get_sleep** with optional query parameters [(detail)](https://github.com/beddit/beddit-api/blob/master/3-Resources.md#get-apiv1useruser_idsleep)
    - **after** (String): get sleep data updated after certain date ("YYYY-mm-dd")
    - **start**, **end** (String): get sleep data between **start** and **end** ("YYYY-mm-dd")
    - **reverse** (String): get sleep data in reverse date order
    - **limit** (Integer): max numbers of returned results

   ```python
  query1 = client.get_sleep(after='2015-01-01', reverse='yes')
  query2 = client.get_sleep(start='2015-03-01', end='2015-03-16')
```

## Official Http API Document
https://github.com/beddit/beddit-api
