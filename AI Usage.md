# AI Usage Disclosure

This document transparently outlines how AI tools were used during the development of this project, including what they were used for, what they were not used for, and how their output was verified before being incorporated.

## Tools Used

- **Tool name**: Claude,Gemini
- **Purpose**: Supporting technical tasks such as debugging, documentation, and code review — not for generating the core project from scratch.

## Where AI Was Used

### 1. Environment & Tooling Setup
- Used AI to understand and troubleshoot SSH key-based authentication (`ssh-keygen`, `ssh-agent`, `authorized_keys` configuration) while setting up access to this repository.
- Used AI to debug a `git clone` failure by walking through SSH connection tests (`ssh -T git@github.com`) and identifying the correct clone URL format.

### 2. Debugging
- Used AI to help interpret error messages and narrow down root causes for specific bugs (e.g., permission errors, misconfigured files).
- AI suggestions were tested locally before being accepted; nothing was copied in blindly.

### 3. Documentation
- Used AI to help structure and phrase parts of this README/documentation for clarity and consistency.
- The technical content and accuracy of the documentation were verified manually against the actual codebase.

### 4. Code Review / Suggestions
- Used AI to review specific functions or snippets for potential bugs, edge cases, or readability improvements.
- All suggested changes were reviewed, understood, and tested before being merged.



