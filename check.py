import os, requests
URL = "https://egy.voxcinemas.com/movies/bts-world-tour-arirang-in-jakarta-live-viewing"
html = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=30).text.lower()
if "almaza" in html:
    requests.post(
        f"https://api.telegram.org/bot{os.environ['TOKEN']}/sendMessage",
        data={"chat_id": os.environ["CHAT_ID"], "text": "الحجز فتح في Almaza! " + URL},
    )
