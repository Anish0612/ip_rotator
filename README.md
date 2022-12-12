# Ip_rotator

ip_rotator helps to hides your ip address in http request.

This library searches every free proxy server that is available and set proxy in the request library.

This library will allow the user to bypass IP-based rate-limits for sites and services.

## Installation

```console
$ pip install ip-rotator
```

ip_rotator officially supports Python 3.7+.


## Usage
---

### Default
```python
import ip_rotator

proxy = ip_rotator.Proxy(https = False)  # To access https url set (https = True)

response = proxy.session.get('http://api.ipify.org/?format=json')

```
#### Output
```console
> Ip : 89.43.10.141       Connected    
  Ip :      89.37.4.82
  Country : Iran
  Https :   no
```


### To Change Ip
___

```python
import ip_rotator

proxy = ip_rotator.Proxy(https = False)  # To access https url set (https = True)

proxy.changeIp()  # to change ip
```