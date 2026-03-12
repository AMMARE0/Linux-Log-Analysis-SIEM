# Attack Simulation

This project includes simulated attacks to test detection rules.

## SSH Brute Force Simulation

A brute force attack was simulated using repeated SSH login attempts.

Example command:

ssh wronguser@localhost

This generates repeated failed login entries in:

/var/log/auth.log

These events are then detected by the SSH brute force detection script.

## Expected Detection

If more than 5 failed login attempts occur from the same IP within a short period, the system triggers an alert.
