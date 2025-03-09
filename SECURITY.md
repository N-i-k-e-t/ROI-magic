# Security Policy

## I. Purpose

This Security Policy outlines the measures taken to protect the confidentiality, integrity, and availability of the InvestWise India platform, its code, algorithms, user data, and intellectual property. This policy applies to all employees, contractors, and users of the platform.

## II. Supported Versions

We are committed to providing timely security updates for supported versions of the InvestWise India platform. The following table indicates the currently supported versions:

| Version | Supported          | End of Life (EOL) |
| ------- | ------------------ | ----------------- |
| 1.0.x   | :white_check_mark: | TBD               |
| < 1.0   | :x:                | [Date]            |

*Note:* Only the latest minor version within a major version is actively supported. Security updates will not be provided for unsupported versions.

## III. Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a potential security vulnerability in the InvestWise India platform, please report it to us immediately by emailing security@investwiseindia.com.

*   **What to Include in Your Report:**
    *   A clear description of the vulnerability.
    *   Steps to reproduce the vulnerability (if possible).
    *   Affected components and versions.
    *   Potential impact of the vulnerability.
    *   Your contact information (so we can reach you for clarification).

*   **What to Expect:**
    *   We will acknowledge receipt of your report within 2 business days.
    *   We will investigate the vulnerability and provide an initial assessment within 5 business days.
    *   We will keep you informed of our progress and estimated timeline for resolution.
    *   If the vulnerability is accepted, we will work to develop and deploy a fix as quickly as possible.
    *   We will publicly disclose the vulnerability (after a fix has been deployed) to inform other users and promote transparency.
    *   If the vulnerability is declined, we will provide a clear explanation of our reasoning.

*   **Responsible Disclosure:** We appreciate responsible disclosure of vulnerabilities. Please refrain from publicly disclosing the vulnerability until we have had a reasonable opportunity to investigate and address it.

## IV. Security Measures

We employ a multi-layered approach to security, including:

*   **Code Security:**
    *   Secure Coding Practices: We follow secure coding practices to minimize the risk of vulnerabilities such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
    *   Code Reviews: All code changes are subject to peer review to identify potential security flaws.
    *   Static Analysis: We use static analysis tools to automatically scan our codebase for vulnerabilities.
    *   Dependency Management: We carefully manage our dependencies and promptly update them to address known vulnerabilities.
*   **Algorithm Security:**
    *   Data Validation: We validate all user inputs to prevent malicious data from compromising our algorithms.
    *   Model Security: We take steps to protect our machine learning models from adversarial attacks and data poisoning.
    *   Regular Audits: We conduct regular audits of our algorithms to ensure their accuracy and security.
*   **Data Security:**
    *   Encryption: We encrypt sensitive data both in transit and at rest.
    *   Access Control: We implement strict access control policies to limit access to sensitive data.
    *   Data Minimization: We only collect and store the data that is necessary for the operation of the platform.
    *   Data Retention: We retain data only for as long as it is needed and securely dispose of it when it is no longer required.
*   **Infrastructure Security (GitHub & Streamlit):**
    *   **GitHub Security:**
        *   Two-Factor Authentication (2FA): All developers are required to enable 2FA on their GitHub accounts.
        *   Branch Protection Rules: We use branch protection rules to prevent unauthorized changes to our codebase.
        *   Secret Scanning: We enable GitHub's secret scanning feature to automatically detect and prevent the accidental exposure of sensitive credentials.
        *   Regular Audits: We conduct regular audits of our GitHub repository to identify and address potential security risks.
    *   **Streamlit Security:**
        *   Secure Configuration: We follow Streamlit's security best practices to ensure the platform is securely configured.
        *   Input Validation: We validate all user inputs to prevent malicious code injection.
        *   Regular Updates: We promptly update Streamlit to address known vulnerabilities.
*   **Incident Response:**
    *   We have a well-defined incident response plan to handle security incidents effectively.
    *   We regularly test our incident response plan to ensure its effectiveness.

## V. Licensing and Intellectual Property Protection

*   **License:** The InvestWise India platform is licensed under the [Choose a License - e.g., Apache 2.0, MIT License, or a proprietary license].
*   **Copyright:** All code, algorithms, and content on the platform are protected by copyright.
*   **Reverse Engineering:** Reverse engineering, decompilation, or disassembly of the platform is strictly prohibited.
*   **Unauthorized Use:** Unauthorized use, reproduction, or distribution of the platform is strictly prohibited.

## VI. Updates to this Policy

We may update this Security Policy from time to time. We will post any changes on our website and notify users as appropriate.

## VII. Contact Information

If you have any questions or concerns about this Security Policy, please contact us at security@investwiseindia.com.

## VIII. Enforcement

Violation of this Security Policy may result in disciplinary action, up to and including termination of employment or contract.

**Additional Notes:**

*   **Choose a License:** Carefully consider the implications of different open-source licenses (Apache 2.0, MIT) versus a proprietary license. An open-source license may encourage community contributions but also allows others to use your code. A proprietary license gives you more control but may limit adoption.
*   **Legal Review:** Have this security policy reviewed by a lawyer to ensure it is legally sound and compliant with all applicable laws and regulations.
*   **Regular Audits:** Conduct regular security audits of your code, infrastructure, and policies to identify and address potential weaknesses.
*   **Training:** Provide security awareness training to all employees and contractors.
*   **Incident Response Plan:** Develop a detailed incident response plan that outlines the steps to be taken in the event of a security breach.
*   **Third-Party Security Tools:** Consider using third-party security tools to monitor your platform for vulnerabilities and threats.

This comprehensive security policy will help protect your platform, your users, and your intellectual property. Remember to adapt it to your specific needs and circumstances.
