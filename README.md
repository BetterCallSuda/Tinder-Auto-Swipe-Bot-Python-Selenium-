# Tinder-Auto-Swipe-Bot-Python-Selenium-
Opens Tinder Web  Logs in manually (safer)  Automatically swipes Right (Like) every few seconds  Handles popups (location, notifications, match popup)


1️⃣ Open Tinder
driver.get("https://tinder.com")

2️⃣ Manual login

We don’t automate login to avoid captcha & blocks.

3️⃣ Handle popups

Tinder shows:

Location permission

Notifications popup

Match popup

We safely close them using try/except.

4️⃣ Swipe logic
body.send_keys(Keys.ARROW_RIGHT)


RIGHT ARROW → Like

LEFT ARROW → Nope

🔁 Change Swipe Behavior
❌ Swipe Left instead
body.send_keys(Keys.ARROW_LEFT)

🔀 Random swipe (more human-like)
import random

if random.random() > 0.3:
    body.send_keys(Keys.ARROW_RIGHT)
else:
    body.send_keys(Keys.ARROW_LEFT)

🛑 Common Issues & Fixes
Issue	Fix
Popups blocking swipe	Close popups
Bot detected	Increase delay
No swipe	Click body first
Stale element	Re-find body
🧠 How to Make It Safer (Recommended)

Increase delay (3–5 sec)

Randomize swipes

Stop after 20–30 swipes

Use test account only

📌 Learning Outcomes

Selenium keyboard automation

Popup handling

Timing control

Real-world DOM interaction

Bot detection awareness
