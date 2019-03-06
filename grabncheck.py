import requests
class proxies():

    def grab(self, proxytype,timeout,country,anonymity,ssl,limit):
        r = requests.get(f'https://api.proxyscrape.com?request=getproxies&proxytype={proxytype}&timeout={timeout}&country={country}&anonymity={anonymity}&ssl={ssl}&limit={limit}')
        grabbed_proxies = r.text

        grabbed_proxies = grabbed_proxies.splitlines()

        return grabbed_proxies

    def check(self, proxies):
        working_proxies = []
        while len(proxies) >= 1:
            proxy = proxies[0].split(":")
            payload = {
                'ip_addr': proxy[0],
                'port': proxy[1]
            }
            r = requests.post('https://onlinechecker.proxyscrape.com/api/index.php', data=payload)

            response = r.json()
            if response['working'] == False:
                pass
            elif response['working'] == True:
                working_proxies.append(proxies[0])

            else:
                pass

            proxies.remove(proxies[0])
        return working_proxies
