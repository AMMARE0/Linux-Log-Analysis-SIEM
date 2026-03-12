## Overview

This project demonstrates automated Linux log monitoring and threat detection using Python.  
The system parses Linux authentication logs and identifies suspicious activity such as SSH brute force attacks.

Security events are analyzed and prepared for visualization in a SIEM-style dashboard environment.

## Project Structure

parsers/        - Log parsing scripts  
detections/     - Security detection rules  
scripts/        - Automation scripts  
sample_logs/    - Example Linux log files  
dashboards/     - SIEM dashboard configurations  
docs/           - Project documentation  
screenshots/    - Dashboard and detection screenshots

## Skills Demonstrated

- Linux log analysis
- Security detection engineering
- Threat monitoring automation
- Python scripting
- SIEM concepts

## MITRE ATT&CK Mapping

| Detection | Technique | ID |
|----------|-----------|----|
| SSH Brute Force | Brute Force | T1110 |
| Unauthorized Login Attempts | Valid Accounts | T1078 |

## Future Improvements

- Real-time log monitoring using `tail` or log streaming
- Integration with Elasticsearch and Kibana dashboards
- Additional detection rules (privilege escalation, suspicious sudo activity)
- Alerting via email or messaging platforms
- Log enrichment with threat intelligence feeds
