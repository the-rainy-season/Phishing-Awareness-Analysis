import re

print("=" * 60)
print("PHISHING AWARENESS ANALYZER")
print("=" * 60)

print("\nPaste Email/Message (Type END on a new line when finished):\n")

lines = []

while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

message = "\n".join(lines)

message_lower = message.lower()

suspicious_keywords = [
    "urgent",
    "verify",
    "password",
    "login",
    "click here",
    "bank",
    "winner",
    "free",
    "account suspended",
    "update immediately",
    "limited time",
    "confirm identity",
    "security alert"
]

red_flags = []

# Check suspicious keywords
for keyword in suspicious_keywords:
    if keyword in message_lower:
        red_flags.append(f"Suspicious keyword detected: '{keyword}'")

# Detect URLs
urls = re.findall(r'https?://\S+|www\.\S+', message)

for url in urls:
    red_flags.append(f"Link detected: {url}")

    if any(shortener in url for shortener in ["bit.ly", "tinyurl", "goo.gl"]):
        red_flags.append("Shortened URL detected")

# Check urgency tactics
urgency_words = ["urgent", "immediately", "now", "asap"]

for word in urgency_words:
    if word in message_lower:
        red_flags.append(f"Urgency tactic found: '{word}'")

# Risk Score
risk_score = min(len(red_flags) * 10, 100)

print("\n" + "=" * 60)
print("PHISHING ANALYSIS REPORT")
print("=" * 60)

if red_flags:
    print("\nRed Flags Found:\n")

    for i, flag in enumerate(red_flags, start=1):
        print(f"{i}. {flag}")

else:
    print("\nNo major phishing indicators found.")

print(f"\nRisk Score: {risk_score}%")

if risk_score >= 70:
    result = "HIGH RISK PHISHING MESSAGE"
elif risk_score >= 30:
    result = "SUSPICIOUS MESSAGE"
else:
    result = "LIKELY SAFE"

print("\nResult:")
print(result)

print("\nWhy is it Unsafe?")

if red_flags:
    print(
        "This message contains phishing indicators such as "
        "suspicious keywords, links, urgency tactics, or requests "
        "for sensitive information."
    )
else:
    print("No major phishing patterns were detected.")

print("\nSecurity Recommendation:")
print("Do not click unknown links, verify sender identity, and never share passwords or OTPs.")

print("\n" + "=" * 60)