import os.path
import time
import requests
from concurrent.futures import ThreadPoolExecutor


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://www.douyin.com",
    "priority": "u=1, i",
    "referer": "https://www.douyin.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "uifid": "5bdad390e71fd6e6e69e3cafe6018169c2447c8bc0b8484cc0f203a274f99fdb8bf16dc319c6d39fa22dcfc9802fbf3451b7536f5f0571e7aec774947b89dc3979ab7dea5c30dfef9e0361762c3ef616e0802fbb0f7e29671e9231b23fdb02eedc66d2472fc69c3186a62b16d37ff508c6c46f74610b635885a2b1b19446c08d0366a18a2ba9eb126ccaddb03fab85ac40696a6c14026a1e05af2a06b5cf356f",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36"
}
cookies = {
    "enter_pc_once": "1",
    "UIFID_TEMP": "5bdad390e71fd6e6e69e3cafe6018169c2447c8bc0b8484cc0f203a274f99fdb8bf16dc319c6d39fa22dcfc9802fbf346aebfbe2f744015b78f5a382f83b6d6d236856fc6d10453cd1ba4d2efacd2d78",
    "hevc_supported": "true",
    "strategyABtestKey": "%221769499841.425%22",
    "passport_csrf_token": "2c63541d25b3ef165cedafac44673e97",
    "passport_csrf_token_default": "2c63541d25b3ef165cedafac44673e97",
    "ttwid": "1%7CZg_wbxjr2zj5--jmP7_NfbTPRoC_5R3E1mgAaYAj3Io%7C1769499840%7C08e89591558a23a91f1765a0babb4241bee2d1237afdb45bd3912da42c9e57b4",
    "bd_ticket_guard_client_web_domain": "2",
    "download_guide": "%221%2F20260127%2F0%22",
    "passport_assist_user": "CkBntclCkM3JNnzW0DfB-207Djv5xNER76aAPGuIWvBsAl574CE1LBM_Vce8ClZ-B1Zqu05lmmHPsR9rNUZL2wHfGkoKPAAAAAAAAAAAAABQAD4sTNOWUaurUCW_SZtDjjci_WF8WcyW6ZNceIHxkzkL_7ICvqTdj8otMgbgpdvi-RCVg4gOGImv1lQgASIBAw5OHek%3D",
    "n_mh": "9J1TqPAcxjd1cPROh6Vg0Ofi5p8hvQGaqV8t5vrgFzE",
    "sid_guard": "205a264971f108afb0e6cceba5763465%7C1769499917%7C5184000%7CSat%2C+28-Mar-2026+07%3A45%3A17+GMT",
    "uid_tt": "db36b79fc7c6d724529fbd8193001abc",
    "uid_tt_ss": "db36b79fc7c6d724529fbd8193001abc",
    "sid_tt": "205a264971f108afb0e6cceba5763465",
    "sessionid": "205a264971f108afb0e6cceba5763465",
    "sessionid_ss": "205a264971f108afb0e6cceba5763465",
    "session_tlb_tag": "sttt%7C19%7CIFomSXHxCK-w5szrpXY0Zf________-jsE3rLqF7UNzpqpXMmuHBbdelCymSQMFGY8tFLkm_51I%3D",
    "is_staff_user": "false",
    "sid_ucp_v1": "1.0.0-KDBkOWViNjYzMDUzYzM5NzkwMDA1OWU4MTE1ZmJjYjlhMzdjMzFmZmUKIAjP2vDDgs14EI3a4csGGO8xIAwwp5CKpAY4B0D0B0gEGgJsZiIgMjA1YTI2NDk3MWYxMDhhZmIwZTZjY2ViYTU3NjM0NjU",
    "ssid_ucp_v1": "1.0.0-KDBkOWViNjYzMDUzYzM5NzkwMDA1OWU4MTE1ZmJjYjlhMzdjMzFmZmUKIAjP2vDDgs14EI3a4csGGO8xIAwwp5CKpAY4B0D0B0gEGgJsZiIgMjA1YTI2NDk3MWYxMDhhZmIwZTZjY2ViYTU3NjM0NjU",
    "_bd_ticket_crypt_cookie": "1b2b8892c0d317c2dbb9de665748da74",
    "__security_mc_1_s_sdk_sign_data_key_web_protect": "ddc6a25d-4e87-a40d",
    "__security_mc_1_s_sdk_cert_key": "46b23679-497b-b8b8",
    "__security_mc_1_s_sdk_crypt_sdk": "13a77e42-4330-bcb5",
    "__security_server_data_status": "1",
    "login_time": "1769499920792",
    "publish_badge_show_info": "%220%2C0%2C0%2C1769499921336%22",
    "UIFID": "5bdad390e71fd6e6e69e3cafe6018169c2447c8bc0b8484cc0f203a274f99fdb8bf16dc319c6d39fa22dcfc9802fbf3451b7536f5f0571e7aec774947b89dc3979ab7dea5c30dfef9e0361762c3ef616e0802fbb0f7e29671e9231b23fdb02eedc66d2472fc69c3186a62b16d37ff508c6c46f74610b635885a2b1b19446c08d0366a18a2ba9eb126ccaddb03fab85ac40696a6c14026a1e05af2a06b5cf356f",
    "SelfTabRedDotControl": "%5B%5D",
    "is_dash_user": "1",
    "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D",
    "playRecommendGuideTagCount": "14",
    "totalRecommendGuideTagCount": "14",
    "gulu_source_res": "eyJwX2luIjoiMzRlYjBiNWI5YTNlY2RkMjY3ZGQzOTBkNjhjMjk1MGIzMjY2YmUyMDc3MWViYmZlMTIzNDM4ZDMxZmNkYTVjOCJ9",
    "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22",
    "sdk_source_info": "7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273c343c3d343c3437303c333234272927676c715a75776a716a666a69273f2763646976602778",
    "bit_env": "Ivkmtan1GLCjm59yPKYPamRGlcw_Bt_eadVFAt4Ti6qnDtISZ5nefAKhGwkhoc_IrgtplhJgukJwVDZD3M_580Av7dxtmsxjCBNXxf5847k-AcuhXllFooeqYR2eZQe2zpfK42GKw5EnJAW7enEOpHNmbwH2r_ukX3Zrn3qmwCI3B41IL6h1UhZPispLl2phaAh7fPnICM8J2xSneqZ4F17ZQae4cIH5wICglKbHE1QuuNvjQHfX3dySbxIm0s52ZVz7-2H7HTm34-D3MFoB-uUh1HSeOLTiRDJ9N6U5dbPdr79LR-1v1j4Gu5Ccy8F0Afoe9vvf_cfA0UiFb7ueK6VE9NIumogYy9Uay-NUcLN5emCgGX93b9Eobwxm-axKYUBzgFdtK1vCYJPY7xe1UxarOP0UwDGFgXRBk3VyMJ5FEKdBZEqp0lvu51Jgeeyg52KXlhIQS4S_AJkR66ghYCYOAY3Q1-wgYTrOnXW2lNFcVU4-8TZatO8rsSDE8s5j",
    "passport_auth_mix_state": "12fic2male7x310375ndz7ym6qovtaxl",
    "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAA9I5Qq1aqRLfj3UWStMyIK0HRTFISPLX4kteVJwe__fA%2F1769529600000%2F0%2F0%2F1769522651834%22",
    "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAA9I5Qq1aqRLfj3UWStMyIK0HRTFISPLX4kteVJwe__fA%2F1769529600000%2F0%2F1769522051834%2F0%22",
    "IsDouyinActive": "true",
    "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1496%2C%5C%22screen_height%5C%22%3A291%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22",
    "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRHdzZkpqQmwwNDhBZXZNSjJ6YkZkcFdpRXpWMlRISno2NFFsK1RvL2hhQjdjeWJhOFMvUTNsWlIwcGlkNUtxbUt5Um9ycFN4QjBYeXZEdlJBY2hpc0E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
    "home_can_add_dy_2_desktop": "%221%22",
    "biz_trace_id": "e1ec26e2",
    "odin_tt": "9616c40ac6268d154055a17a75e130946bd2cf1a682af16332eaab5c85ab31d56bf2689237c446fffe46a2cc4dd946156cc02cf81fa06b22eebad092410da29d",
    "bd_ticket_guard_client_data_v2": "eyJyZWVfcHVibGljX2tleSI6IkJEd3NmSmpCbDA0OEFldk1KMnpiRmRwV2lFelYyVEhKejY0UWwrVG8vaGFCN2N5YmE4Uy9RM2xaUjBwaWQ1S3FtS3lSb3JwU3hCMFh5dkR2UkFjaGlzQT0iLCJ0c19zaWduIjoidHMuMi5mYTNkZjVmMTgxYzcwNjllZDY1Yzc5NWE5MmRiY2Y4YTE4ZjZkNTIxY2QwNTYxZGViYzdmZDQ5ZWRjZmI2YzM3YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiI1QVhtd0NPR29pRy9PN0dqcXNDR0t2UVNGa1prenBqajVicFFjcnNYMkd3PSIsInNlY190cyI6IiNLZFUreEFhK0NlY3pid2U5YlMvWE14SUtsaFgzU0taaTR4MFB4TUk5Yk5uVlI4b0Rrc2dSRXFmdkdlVGMifQ%3D%3D"
}
params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "sec_user_id": "MS4wLjABAAAAoH-TeFQnXau0tbARA47wFz6-q4qwBHmPEtdLuJOAH6RUeKEFtZBWEHR1WhiAOEBw",
        "max_cursor": "1757219381000",
        "locate_query": "false",
        "show_live_replay_strategy": "1",
        "need_time_list": "0",
        "time_list_query": "0",
        "whale_cut_token": "",
        "cut_version": "1",
        "count": "18",
        "publish_video_strategy_type": "2",
        "from_user_page": "1",
        "update_version_code": "170400",
        "pc_client_type": "1",
        "pc_libra_divert": "Windows",
        "support_h265": "1",
        "support_dash": "1",
        "cpu_core_num": "16",
        "version_code": "290100",
        "version_name": "29.1.0",
        "cookie_enabled": "true",
        # "screen_width": "1496",
        # "screen_height": "291",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Chrome",
        "browser_version": "143.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "143.0.0.0",
        # "os_name": "Android",
        # "os_version": "6.0",
        "device_memory": "8",
        # "platform": "Android",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "100",
        "webid": "7599943874563950107",
        "uifid": "5bdad390e71fd6e6e69e3cafe6018169c2447c8bc0b8484cc0f203a274f99fdb8bf16dc319c6d39fa22dcfc9802fbf3451b7536f5f0571e7aec774947b89dc3979ab7dea5c30dfef9e0361762c3ef616e0802fbb0f7e29671e9231b23fdb02eedc66d2472fc69c3186a62b16d37ff508c6c46f74610b635885a2b1b19446c08d0366a18a2ba9eb126ccaddb03fab85ac40696a6c14026a1e05af2a06b5cf356f",
        # "msToken": "pJ8oxW1f7vgA2Mc9qSCN8Xe9FIX2NFPmZiHvDhCV2HiI0zVjGVKwXXvUGlVMAgx9Y8owy62GQJK3gOIXgOSEACgxbc0Xhub-ioDPDJK3HEv9MU4gOgPLyPUoqVUVKWbcFqvJWIgqrOBlY-pYU8HJS-46-Yo55G5yacJfHI47NYgQvNFmGOUhanc=",
        # "a_bogus": "dv4VDFSEdN5fFdKbYCGzyb/UN/gANM8ydeTxSbaTtNPtO1MOzuPpQPclaoLo4P2DkWphkq37fDtMYxncszUiZF9komkDuiJSp029nW6Lh1imPlTmEHDiSukFowsFlQiEa5I6N9fRXssn6nn-VNnYWP5aH5PoRcDZWqP4DFuybDbWpB6T9oOVeah2",
        "verifyFp": "verify_mkwailaw_SZ97vN71_ziiF_4PVa_9O2U_h1w8HZKswtzc",
        "fp": "verify_mkwailaw_SZ97vN71_ziiF_4PVa_9O2U_h1w8HZKswtzc"
    }
def get_html(i):
    url = "https://www-hj.douyin.com/aweme/v1/web/aweme/post/"
    res = requests.get(url, headers=headers, cookies=cookies, params=params)
    params["max_cursor"] = res.json()["max_cursor"]
    data=res.json()["aweme_list"][0]
    author=data["author"]["nickname"]
    title=data["desc"]
    video_url=data["video"]['play_addr']["url_list"][2]
    res1=requests.get(video_url,headers=headers, cookies=cookies)
    if not os.path.exists(f"{author}抖音"):
        os.makedirs(f"{author}抖音")
    path=os.path.join(f"{author}抖音",f"{title}.mp4")
    with open(path,"wb")as f:
        f.write(res1.content)
    print("ok")
    time.sleep(2)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3)as executor:
        executor.map(get_html,range(1,11))




