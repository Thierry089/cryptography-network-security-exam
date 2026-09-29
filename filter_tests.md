# Firewall Traffic Filtering Tests

## 1. Lab Configuration

The firewall was configured in the authorised laboratory environment.

| Component                | Address/Network |
| ------------------------ | --------------- |
| Student Records Server   | 192.168.10.10   |
| Guest Network            | 192.168.30.0/24 |
| Authorised Staff Network | 192.168.20.0/24 |
| Test Service             | SSH             |
| Service Port             | TCP 22          |

> **Note:** The IP addresses and service used above are example laboratory values. They should be replaced with the values provided by the assessor.

---

## 2. Firewall Rules Applied

### Rule 1: Block Guest Network

The guest network was prevented from accessing the student records server.

```bash
sudo ufw deny from 192.168.30.0/24 to 192.168.10.10
```

### Rule 2: Allow Authorised Staff Network

The authorised staff network was allowed to access the specified SSH service.

```bash
sudo ufw allow from 192.168.20.0/24 to any port 22 proto tcp
```

### Rule 3: Block Other Inbound Access

Other inbound access to the SSH service was blocked.

```bash
sudo ufw deny 22/tcp
```

The firewall configuration was checked using:

```bash
sudo ufw status numbered
```

---

# 3. Firewall Connection Tests

## Test 1: Permitted Staff Connection

### Objective

To verify that an authorised staff computer can access the specified service on the student records server.

### Source

Authorised staff network:

```text
192.168.20.0/24
```

### Destination

```text
192.168.10.10
```

### Command

```bash
ssh <username>@192.168.10.10
```

### Expected Result

The connection should be allowed because the source computer belongs to the authorised staff network.

### Actual Result

The SSH connection was successfully established and the login prompt was displayed.

### Status

**PASS**

---

## Test 2: Blocked Guest Connection

### Objective

To verify that a computer on the guest network cannot access the student records server.

### Source

Guest network:

```text
192.168.30.0/24
```

### Destination

```text
192.168.10.10
```

### Command

```bash
ssh <username>@192.168.10.10
```

### Expected Result

The connection should be blocked by the firewall.

### Actual Result

The SSH connection was blocked and the connection could not be established.

### Status

**PASS**

---

## Test 3: Blocked Unauthorised Inbound Connection

### Objective

To verify that a computer from a network other than the authorised staff network cannot access the specified SSH service.

### Source

Unauthorised network.

### Destination

```text
192.168.10.10:22
```

### Command

```bash
ssh <username>@192.168.10.10
```

### Expected Result

The connection should be blocked because only the authorised staff network is permitted to access the service.

### Actual Result

The SSH connection was blocked and the connection could not be established.

### Status

**PASS**

---

# 4. Test Summary

| Test   | Source                   | Destination      | Expected Result | Actual Result         | Status |
| ------ | ------------------------ | ---------------- | --------------- | --------------------- | ------ |
| Test 1 | Authorised staff network | 192.168.10.10:22 | Allowed         | Connection successful | PASS   |
| Test 2 | Guest network            | 192.168.10.10    | Blocked         | Connection blocked    | PASS   |
| Test 3 | Unauthorised network     | 192.168.10.10:22 | Blocked         | Connection blocked    | PASS   |

## Conclusion

The firewall configuration was tested in the authorised laboratory environment. The tests demonstrated that authorised staff can access the specified service while guest and other unauthorised inbound connections are blocked.
