import os
import requests
from duolingo import Duolingo

# 환경 변수에서 로그인 정보 가져오기
DUOLINGO_USERNAME = os.getenv("yeseong9623")
DUOLINGO_PASSWORD = os.getenv("962357841Ss@")
WEBHOOK_URL = os.getenv("https://hooks.zapier.com/hooks/catch/21085754/28h11m3/")

# 듀오링고 로그인
lingo = Duolingo(DUOLINGO_USERNAME, DUOLINGO_PASSWORD)

# 데이터 가져오기
user_info = lingo.get_user_info()
xp_today = user_info.get('xpGoalToday', 0)
streak = user_info.get('site_streak', 0)

# Webhook으로 데이터 전송
payload = {
    "date": requests.get("https://worldtimeapi.org/api/timezone/Etc/UTC").json()["datetime"][:10],
    "xp_today": xp_today,
    "streak": streak,
    "goal_met": "Yes" if xp_today >= 50 else "No"
}
response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    print("Webhook sent successfully!")
else:
    print(f"Failed to send webhook: {response.status_code}")