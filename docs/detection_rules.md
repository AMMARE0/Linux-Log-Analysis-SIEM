# Detection Rules

## SSH Brute Force Detection

Description:
Detects repeated failed SSH login attempts from the same IP address.

Log Source:
Linux authentication logs

Log File:
/var/log/auth.log

Detection Logic:
If an IP address generates more than 5 failed login attempts, an alert is triggered.

Reasoning:
Brute force attacks attempt multiple login attempts in a short time.

Response:
Investigate IP address and consider blocking via firewall.
