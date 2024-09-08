import requests
import time

testDestination = 'https://www.google.com'

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def test_proxy(proxy):
    proxy_parts = proxy.split(':')
    if len(proxy_parts) != 4:
        return f"FAIL - Invalid proxy format: {proxy}"
    
    ip, port, user, password = proxy_parts
    proxy_dict = {
        'http': f'http://{user}:{password}@{ip}:{port}',
        'https': f'http://{user}:{password}@{ip}:{port}'
    }

    try:
        start_time = time.time()
        response = requests.get(testDestination, proxies=proxy_dict, timeout=5)
        response_time = int((time.time() - start_time) * 1000)  
        if response.status_code == 200:
            return f"{proxy}: {GREEN}OK{RESET} - {response_time} ms"
        else:
            return f"{proxy}: {RED}FAIL{RESET} - Status code {response.status_code} "
    except requests.exceptions.Timeout:
        return f"{proxy}: {RED}FAIL{RESET} - Timeout"
    except requests.exceptions.RequestException as e:
        return f"{proxy}: {RED}FAIL{RESET}"

def main():
    try:
        while True:
            print("\n👇📝 Paste your list here and press Enter twice to start testing ⏎:")
            proxies_list = []
            while True:
                line = input()
                if line == '':
                    break
                proxies_list.append(line)
            for proxy in proxies_list:
                result = test_proxy(proxy)
                print(result)
    except KeyboardInterrupt:
        print("\nbye!")

if __name__ == "__main__":
    main()
