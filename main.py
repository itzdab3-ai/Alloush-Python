import json
import hashlib
import random
import hmac
import asyncio
import aiohttp
import re
import uuid
import os
from urllib.parse import urlparse, parse_qs

# --- خوارزمية Gorgon ---
class Gorgon:
    def __init__(self):
        self.key = "97551682"
        self.aid = "1233"
        self.iv  = "7263291a"

    def Hrr(self, n):
        out = []
        while True:
            b = n & 0x7F
            n >>= 7
            if n:
                out.append(b | 0x80)
            else:
                out.append(b)
                break
        return bytes(out)

    def vgeta(self, num, data):
        ttxp = (num << 3) | 2
        return self.Hrr(ttxp) + self.Hrr(len(data)) + data

    def Quick(self, num, s):
        s = s.encode() if isinstance(s, str) else s
        return self.vgeta(num, s)

    def Enc(self, num, TikTok, url=None):
        if TikTok is None and url:
            TikTok = {k: v[0] for k, v in parse_qs(urlparse(url).query).items()}
        if TikTok is None:
            return b""
        if isinstance(TikTok, dict):
            TikTok = json.dumps(TikTok, separators=(",", ":"))
        elif not isinstance(TikTok, str):
            TikTok = str(TikTok)
        return self.Quick(num, TikTok)

    def build(self, params=None, cookies=None, data=None, payload=None, url=None):
        AHMED = b""
        AHMED += self.Enc(1, params, url)
        AHMED += self.Enc(2, cookies)
        AHMED += self.Enc(3, data or payload)
        return AHMED

    def Encoder(self, params=None, cookies=None, data=None, payload=None, url=None):
        builded = self.build(params, cookies, data, payload, url)
        msg = builded + self.iv.encode() + self.aid.encode()
        h = hmac.new(self.key.encode(), msg, hashlib.md5).hexdigest()       
        a = f"{random.randint(0, 0xFFFF):04x}"
        b = f"{random.randint(0, 0xFFFF):04x}"
        c = f"{random.randint(0, 0xFFFF):04x}"
        final = f"8404{a}{b}0000{h}{c}"
        return final

# --- إعدادات الواجهة والألوان ---
if os.name == 'nt':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        h = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()
        kernel32.GetConsoleMode(h, ctypes.byref(mode))
        kernel32.SetConsoleMode(h, mode.value | 0x0004)
    except: pass

print("\033[1;31m" + r'''::::::::::.:::.:::::::::::::::::::::::::::::.::.:::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::......    ...::::::::::::::::::::
:::::::::::::::::::.                ....:::::::::::::::
::::::::::::::::.                      .:::::::::::::::
::::::::::::::..                        .::::::::::::::
:::::::::::::.                          .::::::::::::::
:::::::::::.                            .::::::::::::::
:::::::::::.                     .     ::::::::::::::::
::::::::::.                      ..    :::::::....:::::
::::::::::.                 ..: ...    :::::........:::
::::::::::...               :-:  :-:.  .::::........:::
:::::::::::::..  .          .-.  :---::.::::::....:::::
:::::::::::::::..:                -----:...::::::::::::
::::::::::::::::::..               ::.     .:::::::::::
::::::::::::::::::::..                      .::::::::::
:::::::::::::::::::::::   ..:                 ..:::::::
::::::::::::::::::::::::::::.                    .:::::
:::::::::::::::::::::::::::.                       .:::
::::::..:....::::::::::::.                          .::
::::::..:....::::::::::.                            .::
::::....:....::::::::.                              .::
:::::..:::..::::::::.                                ::
:::::::::::::::::::.                                .::
:::::::::::::::::::                                 .::
::::::::::::::::::.                                 .::
::::::::::::::::::                                  .::
''' + "\033[0m")

text = "علــش @GX1GX1"
FG_BLACK, FG_WHITE, BG_GREEN, RESET = "\033[30m", "\033[97m", "\033[42m", "\033[0m"
pad = 3
content_width = len(text) + pad * 2
print(FG_BLACK + BG_GREEN + " " + "─" * content_width + " " + RESET)
print(FG_BLACK + BG_GREEN + "│" + " " * pad + FG_WHITE + text + FG_BLACK + " " * pad + "│" + RESET)
print(FG_BLACK + BG_GREEN + " " + "─" * content_width + " " + RESET)

a3, a7 = '\x1b[1;32m', '\x1b[38;5;13m'
print(a7+'رابطـ الفيـديو                     ')

# --- الكلاس الأساسي بعد الدمج ---
class Sayid:
    def __init__(self):
        self.gg_encoder = Gorgon() # تهيئة خوارزمية Gorgon
        self.url_input = input(a3+" URL⮕  ")
        self.threads = 500
        self.API = "https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/"
        self.counter = 0
        self.lock = asyncio.Lock()
        asyncio.run(self.main_run())

    async def main_run(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url_input, allow_redirects=True) as response:
                    full_url = str(response.url)
                
                match = re.search(r'/video/(\d+)', full_url)
                if match:
                    video_id = match.group(1)
                    tasks = [asyncio.create_task(self.worker(session, video_id)) for _ in range(self.threads)]
                    await asyncio.gather(*tasks)
                else:
                    print('{"error": "Invalid URL or no video_id found"}')
            except Exception as e:
                print(f"Error Url > {e}")

    def gen_dynamic_params(self):
        params = {
            "manifest_version_code": "350302",
            "_rticket": str(int(random.random() * 10**16)),
            "app_language": "en",
            "app_type": "normal",
            "iid": str(random.randint(7000000000000000000, 9000000000000000000)),
            "channel": "googleplay",
            "device_type": "RMX3941",
            "language": "en",
            "host_abi": "arm64-v8a",
            "locale": "en",
            "resolution": "1080*2290",
            "openudid": str(uuid.uuid4().hex[:16]),
            "update_version_code": "350302",
            "ac2": "wifi5g",
            "cdid": str(uuid.uuid4()),
            "sys_region": "US",
            "os_api": "34",
            "timezone_name": "America/New_York",
            "dpi": "480",
            "carrier_region": "US",
            "ac": "wifi",
            "device_id": str(random.randint(7000000000000000000, 9000000000000000000)),
            "os_version": "12",
            "timezone_offset": "10800",
            "version_code": "350302",
            "app_name": "musically_go",
            "ab_version": "35.3.2",
            "version_name": "35.3.2",
            "device_brand": "realme",
            "op_region": "US",
            "ssmix": "a",
            "device_platform": "android",
            "build_number": "35.3.2",
            "region": "US",
            "aid": "1340",
            "ts": str(int(random.random() * 10**10))
        }
        return params

    async def worker(self, session, video_id):
        while True:
            params = self.gen_dynamic_params()
            payload = {
                'pre_item_playtime': "",
                'first_install_time': "1737204216",
                'item_id': video_id,
                'is_ad': "false",
                'follow_status': "0",
                'sync_origin': "false",
                'follower_status': "0",
                'action_time': str(int(random.random() * 10**10)),
                'tab_type': "3",
                'play_delta': "1",
                'aweme_type': "0"
            }

            # توليد x-gorgon بناءً على الباراميترز والبودي الحالية
            gorgon_hex = self.gg_encoder.Encoder(params=params, data=payload)

            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go",
                'Accept-Encoding': "gzip",
                'x-ss-stub': "80867B02FBD2ECA6BA9AA62239D3B1EB",
                'x-gorgon': gorgon_hex,
                'x-khronos': str(int(random.random() * 10**10)),
                'Cookie': "store-idc=alisg; install_id=7516928038623151879; ttreq=1$5f3bc0fcb73296e39d74f6d161b1e2dfed2914e2;"
            }

            try:
                async with session.post(self.API, data=payload, headers=headers, params=params) as response:
                    if response.status == 200:
                        json_data = await response.json()
                        if json_data.get("status_code") == 0:
                            async with self.lock:
                                self.counter += 1
                                print(f"\033[44m\033[33m\r {self.counter}  الـسـرعة \033[0m", end='', flush=True)
            except:
                continue

if __name__ == "__main__":
    Sayid()
