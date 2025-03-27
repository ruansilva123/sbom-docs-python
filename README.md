# Automatic SBOM Generation

![Python Version](https://img.shields.io/badge/Python%20version-3.13-004975)

The Software Bill of Materials is an inventory that lists all software components, including versions, licenses and dependencies.

## 📦 How to use

1. Create a virtual machine in your project:

        python -m venv venv

2. Activate the virtual machine:

        venv\Scripts\activate

3. Install dependencies:

        pip install pip-licenses cyclonedx-bom

4. Run CycloneDX:

        cyclonedx-py requirements requirements.txt > sbom.json

5. After run pip-licences:

        pip-licenses --format=json > licenses.json

6. In the end, run script:

        python license.py

> ⚠️PS: To generate file, the project must have the files license.py, licenses.json, sbom.json and requirements.txt in the root path, unless you change the script.

You can view result in [Result](./SBOM.md).
