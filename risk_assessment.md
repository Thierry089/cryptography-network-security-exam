# cryptography-network-security-exam
Polytechnic Institute security review risk assessment

# Risk Assessment

## 1. Assets, Vulnerabilities and Consequences

| Asset | Vulnerability | Possible Consequence |
|---|---|--
| Student records server | Guest network has access to the records server | Unauthorized users could access, modify, or steal confidential student information. |
| Files transferred between campuses | File transfers are unencrypted | Attackers could intercept and read sensitive files while they are being transferred. |
| Staff accounts and server access | Weak staff passwords | Attackers could guess or crack passwords and gain unauthorized access to systems and student records. |

## 2. Risk Ranking

| Rank | Risk | Likelihood | Impact | Reason |
|---|---|---|---|---|
| 1 | Guest network access to the records server | High | High | Guest users should not have access to the internal records server. If an attacker connects to the guest network, they may attempt to reach the server and access confidential records. |
| 2 | Weak staff passwords | High | High | Weak passwords are easier to guess or crack. A compromised staff account could provide unauthorized access to student records and other internal resources. |
| 3 | Unencrypted file transfers | Medium | High | Files transferred between campuses can potentially be intercepted and read by attackers, especially if the network traffic is monitored. |

### External server access attempts

The repeated attempts to reach the server from an unfamiliar external address are also a security warning. They may indicate scanning or attempted unauthorized access. This should be investigated and monitored, although the available information is not enough to confirm that the address represents a successful attack.

## 3. Recommended Controls

### Risk 1: Guest network access to the records server
**Control:** Implement network segmentation and firewall rules.

The guest network should be isolated from the internal network containing the student records server. Firewall or traffic-filtering rules should block traffic from the guest network to the records server while allowing only authorized internal systems to connect.

### Risk 2: Weak staff passwords
**Control:** Enforce a strong password policy and multi-factor authentication (MFA).

Staff should use long, unique passwords, and MFA should be enabled for accounts that can access sensitive systems. This reduces the likelihood of unauthorized access through guessed or compromised passwords.

### Risk 3: Unencrypted file transfers
**Control:** Use encrypted file-transfer protocols such as SFTP or HTTPS.

Files should be transferred using encrypted communication so that intercepted network traffic does not expose the contents of the files.

## Conclusion

The most important risks identified are unauthorized access to the student records server, weak staff authentication, and exposure of files during transmission. Network segmentation, stronger authentication, and encrypted communication can significantly reduce these risks.
