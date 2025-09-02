# Contributing to Privacy Rights Registry

Thank you for your interest in contributing to the Privacy Rights Registry! This project aims to prevent stalking and doxxing whilst creating legal liability for privacy violations in Ireland.

## 🎯 Project Mission

We're building infrastructure that:
- **Prevents stalking/doxxing** at the technical level
- **Creates legal liability** for companies that ignore privacy rights
- **Positions Ireland** as a leader in digital privacy rights
- **Operates within existing law** (no new legislation required)

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (production) or SQLite (development)
- Redis (for rate limiting)
- Docker (optional but recommended)

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/xbard-C42/privacy-rights-registry.git
   cd privacy-rights-registry
   ```

2. **Set up Python environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your local values
   ```

4. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

5. **Start the development server**:
   ```bash
   uvicorn main:app --reload
   ```

6. **Set up frontend** (if contributing to UI):
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### Docker Development

```bash
# Start all services
docker-compose up -d

# Run tests
docker-compose exec api pytest

# View logs
docker-compose logs -f api
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=. --cov-report=html

# Run specific test categories
python -m pytest tests/test_main.py::TestAntiDoxxingProtection

# Run frontend tests
cd frontend && npm test
```

### Test Categories

- **Unit Tests**: Individual function testing
- **Integration Tests**: API endpoint testing
- **Security Tests**: Anti-doxxing protection validation
- **Compliance Tests**: GDPR/Irish law compliance
- **Load Tests**: Performance under stress

### Writing Tests

- All new features must include tests
- Focus on security-critical functionality
- Test both success and failure cases
- Include edge cases and error conditions
- Test anti-doxxing protection thoroughly

## 📝 Code Style

### Python Code Style

We follow PEP 8 with some modifications:

```bash
# Format code
black .

# Check style
flake8 .

# Type checking
mypy .
```

### TypeScript/React Code Style

```bash
# In frontend directory
npm run lint
npm run type-check
```

### Key Principles

1. **Security First**: Every change must maintain security
2. **Privacy by Design**: Default to maximum privacy protection
3. **Irish Context**: Consider Irish legal/political context
4. **Performance**: Anti-doxxing checks must be fast
5. **Auditability**: Log all security-relevant actions

## 🔒 Security Guidelines

### Critical Security Requirements

1. **Never disable anti-doxxing protection** without explicit user consent
2. **All database queries** must be parameterised (no SQL injection)
3. **Rate limiting** must be maintained on all endpoints
4. **Audit logging** is mandatory for all privacy-related actions
5. **Password requirements** cannot be weakened
6. **JWT tokens** must have proper expiration

### Security Review Process

- All PRs undergo security review
- Anti-doxxing functionality requires extra scrutiny
- Database changes need migration review
- Authentication changes require senior review

## 🏛️ Legal and Compliance

### Irish Law Compliance

- Must comply with Data Protection Act 2018
- Must align with Irish government digital standards
- Consider Oireachtas committee recommendations
- Respect existing GDPR implementation

### Political Considerations

- Green Party adoption is a priority
- Consider impact on Irish digital sovereignty
- Align with progressive privacy policies
- Build for government deployment

## 🔄 Contribution Workflow

### 1. Issue Discussion

- Check existing issues first
- For new features, open an issue to discuss
- Security issues: follow `SECURITY.md` process
- Large changes: discuss with maintainers first

### 2. Development Process

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** following style guides
4. **Add/update tests** for your changes
5. **Update documentation** if needed
6. **Ensure tests pass**: `python -m pytest`
7. **Commit your changes**: Use clear, descriptive messages

### 3. Pull Request Process

1. **Update README.md** if needed
2. **Update CHANGELOG.md** for user-facing changes
3. **Create pull request** with detailed description
4. **Link related issues** in PR description
5. **Respond to review feedback**
6. **Squash commits** if requested

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Security improvement
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Security tests included (if applicable)

## Security Impact
Describe any security implications of this change

## Irish Government/Green Party Impact
Describe relevance to Irish deployment or policy goals

## Checklist
- [ ] My code follows the project style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published
```

## 📚 Documentation

### Documentation Requirements

- **Code comments**: Explain complex logic, especially security-related
- **API documentation**: Update OpenAPI specs for new endpoints
- **README updates**: Keep installation/usage instructions current
- **Architecture docs**: Document major design decisions

### Documentation Style

- Write for Irish government technical staff
- Assume familiarity with GDPR/privacy law
- Include practical deployment examples
- Focus on security and compliance implications

## 🏗️ Architecture Guidelines

### Core Principles

1. **Fail Secure**: If something breaks, default to blocking access
2. **Audit Everything**: Log all privacy-relevant actions
3. **Rate Limit Everything**: Prevent abuse at the infrastructure level
4. **Validate Everything**: Never trust user input
5. **Encrypt Everything**: Data at rest and in transit

### Database Design

- Use foreign keys for data integrity
- Index fields used in queries
- Store audit logs immutably
- Hash all passwords with bcrypt
- Use JSON fields for flexible rights storage

### API Design

- RESTful endpoints with clear naming
- Consistent error response format
- Rate limiting on all endpoints
- Comprehensive input validation
- JWT authentication for companies

## 🎨 Frontend Contributions

### React/TypeScript Guidelines

- Use TypeScript strictly (no `any` types)
- Follow React hooks patterns
- Implement proper error boundaries
- Use Tailwind CSS for styling
- Focus on accessibility

### UI/UX Principles

- **Privacy-first design**: Make privacy options prominent
- **Irish government aesthetics**: Professional, accessible
- **Mobile-responsive**: Works on all devices
- **Performance**: Fast loading, minimal JavaScript
- **Accessibility**: WCAG 2.1 AA compliance

## 🚦 Release Process

### Version Numbers

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking API changes
- **MINOR**: New features, backwards compatible
- **PATCH**: Bug fixes, security updates

### Release Checklist

1. All tests pass
2. Security review completed
3. Documentation updated
4. CHANGELOG.md updated
5. Version number bumped
6. Docker images built and tested
7. Deployment tested on staging

## 🤝 Community Guidelines

### Code of Conduct

- **Respectful**: Treat all contributors with respect
- **Inclusive**: Welcome contributions from all backgrounds
- **Constructive**: Provide helpful, actionable feedback
- **Privacy-focused**: Respect user privacy in all discussions
- **Irish-friendly**: Welcome Irish contributors especially

### Communication

- **GitHub Issues**: For bug reports and feature requests
- **Pull Requests**: For code review and discussion
- **Discussions**: For broader project discussions
- **Email**: security@c42os.com for security issues

## 🏆 Recognition

### Contributor Recognition

- Regular contributors may be added to README
- Significant contributions recognized in releases
- Priority consideration for Irish government roles
- Green Party acknowledgement opportunities

### Green Party Integration

We're actively working with the Green Party for:
- Political endorsement of the registry
- Government deployment opportunities
- Policy framework development
- International privacy leadership

## 📞 Getting Help

### Support Channels

- **GitHub Discussions**: General questions and ideas
- **GitHub Issues**: Bug reports and feature requests
- **Email**: xbard@protonmail.com for maintainer contact
- **Security**: security@c42os.com for security issues

### Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Irish Data Protection Act 2018](https://www.irishstatutebook.ie/eli/2018/act/7/enacted/en/html)
- [GDPR Compliance Guide](https://gdpr.eu/)

---

## 🇮🇪 Irish Digital Sovereignty

This project is part of Ireland's journey toward digital sovereignty. Every contribution helps:

- **Protect Irish citizens** from stalking and doxxing
- **Position Ireland** as a global privacy leader
- **Create legal liability** for privacy violations
- **Demonstrate** that progressive privacy policy works in practice

**Every line of code brings us closer to a privacy-respecting digital Ireland.**

---

*Built with 💚 in Edgeworthstown, Co. Longford, Ireland*
