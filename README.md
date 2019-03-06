## How to install

download grabncheck.py, and place it in your python project
                    

## How to use

#### Grab proxies

```python
from .grabncheck import proxies
#grabs http proxies that are from the US and have SSL. This will only generate 100 proxies.
#this will return a list of proxies
proxies = proxies.grab('self', proxytype='http', timeout=7000, country='US', anonymity='all', ssl='all', limit=100)

print(proxies)
```

#### Check proxies

```python
from .grabncheck import proxies 
myProxies = ['35.174.94.98:80', '54.242.190.101:80', '50.232.162.65:80', '204.12.219.162:3128', '35.194.86.198:3128']
working_proxies = proxies.check('self', proxies=myProxies)

print(working_proxies)
```


#### Grab then check proxies

```python
from .grabncheck import proxies
#grab the proxies
proxies = proxies.grab('self', proxytype='http', timeout=7000, country='US', anonymity='all', ssl='all', limit=100)
#check the proxies grabbed
working_proxies = proxies.check('self', proxies=proxies)
#print the working proxies
print(working_proxies)
```

## proxies.grab() settings

#### proxies.grab() proxy types

1. http
2. socks4
3. socks5
4. all

#### proxies.grab() country codes

Any *Alpha 2 ISO* county codes. If county doesn't matter, pass *all*

#### proxies.grab() anonymity types   

1. elite
2. anonymous
3. transparent
4. all

#### proxies.grab() ssl types   

1. yes
2. no
3. all

#### proxies.grab() limit

The limit can be any number greater than 0. The limit will be the amount of proxies scraped


## proxies.check() settings

#### proxies.check() proxies

The list of proxies to be checked.


    
