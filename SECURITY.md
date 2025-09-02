# Security Policy

## Supported Versions

We take security seriously and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of these methods:

### 1. Private Security Advisory (Preferred)
- Go to the [Security tab](https://github.com/xbard-C42/privacy-rights-registry/security/advisories) of this repository
- Click "Report a vulnerability"
- Provide detailed information about the vulnerability

### 2. Email
Send details to: **security@c42os.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)

## Security Response Process

1. **Acknowledgement**: We'll acknowledge receipt within 24 hours
2. **Assessment**: We'll assess the vulnerability within 48 hours
3. **Fix Development**: Critical issues will be addressed immediately
4. **Disclosure**: We follow responsible disclosure practices

## Security Measures

This registry implements multiple security layers:

### Infrastructure Security
- Rate limiting on all endpoints
- Strong password requirements with validation
- JWT token expiration and rotation
- Comprehensive audit logging
- Security headers (HSTS, XSS Protection, etc.)
- Non-root Docker containers

### Data Protection
- Database password hashing with bcrypt
- Encrypted JWT tokens
- Anti-doxxing protection enforcement
- Comprehensive audit trails
- GDPR compliance measures

### Production Hardening
- Docker container security
- Database connection security
- Redis security for rate limiting
- Nginx reverse proxy configuration
- SSL/TLS encryption requirements

## Vulnerability Categories

### Critical (Immediate Response)
- Remote code execution
- Authentication bypass
- Data exposure vulnerabilities
- Anti-doxxing protection bypass

### High (24-48 hour response)
- Privilege escalation
- SQL injection
- Cross-site scripting (XSS)
- Rate limiting bypass

### Medium (1 week response)
- Information disclosure
- Denial of service
- Configuration vulnerabilities

### Low (Best effort)
- Minor information leaks
- Non-exploitable issues

## Security Best Practices for Contributors

1. **Never commit secrets**: Use `.env.example` templates
2. **Input validation**: Validate all user inputs
3. **Authentication**: Verify all protected endpoints
4. **Logging**: Log security-relevant events
5. **Dependencies**: Keep dependencies updated
6. **Testing**: Include security test cases

## Known Security Considerations

### By Design
- Anti-doxxing protection blocks data lookups (this is intentional)
- Rate limiting may block legitimate high-volume usage
- Strong password requirements may frustrate some users

### Monitored Risks
- Database performance under high load
- Redis availability for rate limiting
- JWT token size and performance

## Security Contacts

- **Primary**: security@c42os.com
- **Backup**: xbard@protonmail.com
- **Green Party Contact**: info@greenparty.ie (for Irish political concerns)

## Legal Framework

This registry operates within:
- Irish Data Protection Act 2018
- EU GDPR requirements
- Irish Government digital security standards

Security vulnerabilities that could impact Irish citizens' privacy rights are treated with the highest priority.

---

**The faster security issues are reported, the faster we can protect Irish citizens from privacy violations.**
