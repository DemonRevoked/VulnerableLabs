```markdown
# VulnerableLabs

**VulnerableLabs** is a collection of intentionally vulnerable Docker environments designed for security testing, penetration testing practice, vulnerability analysis, and research. Each environment hosts a specific vulnerable application that can be deployed via Docker Compose.

---

## Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Disclaimer](#disclaimer)
- [Contributions](#contributions)
- [License](#license)
- [Repository](#repository)

---

## Features

This repository includes the following vulnerable applications:

- **Apache**
- **Samba**
- **Tomcat**
- **Joomla**
- **GitLab**
- **CouchDB**

---

## Prerequisites

Before using this repository, ensure you have installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3** (to run the included script)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/DemonRevoked/VulnerableLabs.git
   cd VulnerableLabs
   ```
2. Verify Docker and Docker Compose are correctly installed and running.

---

## Usage

1. Run the Python script from the repository root:
   ```bash
   python3 start_docker.py
   ```
2. Select a target (1–6) when prompted:
   ```
   Select the vulnerable target to start:
   1: apache
   2: samba
   3: tomcat
   4: joomla
   5: gitlab
   6: couchdb
   Enter choice (1-6):
   ```
3. The script will:
   - Stop and remove any running Docker containers.
   - Start the chosen vulnerable application.

---

## Troubleshooting

- **Permission Denied Errors (Linux):**  
  Run Docker commands with `sudo` or add your user to the `docker` group.  
- **Docker Not Running:**  
  Make sure Docker is installed and started.  
- **Containers Not Starting:**  
  Verify the `docker-compose.yml` files and your system resources.

---

## Disclaimer

These applications are intentionally vulnerable. **Do not expose them to public networks or production environments.** Deploy within an isolated, secure lab environment only.

---

## Contributions

Contributions, suggestions, and improvements are welcome. Please open an issue or submit a pull request.

---

## License

This repository is released under the [MIT License](LICENSE).

---

## Repository

[https://github.com/DemonRevoked/VulnerableLabs.git](https://github.com/DemonRevoked/VulnerableLabs.git)
```
