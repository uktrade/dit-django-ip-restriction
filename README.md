# DIT Django IP safelist

## install

`pip install -e git+https://www.github.com/uktrade/dit-django-ip-safelist@initial_commit#egg=ip_safelist`

## configure whole site IP restriction with basic auth fallback

### Add to middleware

```

MIDDLEWARE = [
    ...
    'ip_safelist.middleware.IpRestrictionOrBasicAuth',
]

### Configure settings

```
ENABLE_IP_SAFELIST = True
ALLOWED_IPS = ['127.0.0.1', ...]         # a list of allowed IPs
ALLOWED_IP_RANGES = ['x.x.x.x/32', ...]  # a list of allowed CIDRs
BASICAUTH_USERS = {
    'user1': 'user1pass',
    'user2': 'user2pass',
}
```

## TODO:
* write some docs
* Add some tests
