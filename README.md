# Sloppy
🐇 Unsecured Api Exploiter

## Example
### Payload
```JSON
{
    "name": "Github",
    "url": "https://github.com",
    "headers": {},
    "body": {},
    "actions": [
        {
            "route": "/Neotoxic-off",
            "method": "GET",
            "headers": {},
            "body": {}
        },
        {
            "route": "/Neotoxic-off",
            "method": "POST",
            "headers": {},
            "body": {}
        }
    ],
    "automatisms": []
}
```

### Output
```
[ WAIT ] loading payloads...
[ DONE ] 1 payloads loaded
[ WAIT ] checking payloads...
[ DONE ] payload 'Github' valid
[ DONE ] all payloads checked
[ WAIT ] executing payloads...
[ WAIT ] recording results...
	--> GET 200 https://github.com/Neotoxic-off
	--> POST 403 https://github.com/Neotoxic-off
[ DONE ] results recorded
[ DONE ] all payloads executed
[ WAIT ] saving records...
[ DONE ] records saved
```

### Record
```JSON
[
    {
        "url": "https://github.com/Neotoxic-off",
        "method": "GET",
        "code": 200,
        "headers": {},
        "cookies": {},
        "content": null,
        "history": []
    },
    {
        "url": "https://github.com/Neotoxic-off",
        "method": "POST",
        "code": 403,
        "headers": {},
        "cookies": {},
        "content": null,
        "history": []
    }
]
```
