A simple Flask app that returns request details.

    $ curl -sq -H "Authorization: some_bearer_token" http://127.0.0.1:12345/test/post?please=ignore
    {
      "path": "test/post",
      "headers": {
        "Host": "127.0.0.1:12345",
        "User-Agent": "curl/7.64.0",
        "Accept": "*/*",
        "Authorization": "some_bearer_token"
      },
      "args": {
        "please": "ignore"
      },
      "form": {},
      "raw_data": "b''"
    }
