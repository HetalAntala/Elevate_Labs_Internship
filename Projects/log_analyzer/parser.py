import re

def parse_line(line):
    apache_pattern = r'(\d+\.\d+\.\d+\.\d+).*"(GET|POST).*" (\d+)'
    ssh_pattern = r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)'

    # Apache
    if "GET" in line or "POST" in line:
        match = re.search(apache_pattern, line)
        if match:
            return {
                "ip": match.group(1),
                "method": match.group(2),
                "status": int(match.group(3)),
                "type": "apache"
            }

    # SSH
    if "Failed password" in line:
        match = re.search(ssh_pattern, line)
        if match:
            return {
                "ip": match.group(1),
                "type": "ssh",
                "event": "failed_login"
            }

    return None