import os
import json

def extract_data(path):
    data = None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        with open(path, 'r', encoding='utf-16') as f:
            data = json.load(f)
    return data

def main():
    sbom_path = os.path.abspath('sbom.json')
    licenses_path = os.path.abspath('licenses.json')

    for path in [sbom_path, licenses_path]:
        if not os.path.exists(path): raise Exception(f'Root "{path}" not found!')

    sbom = extract_data(sbom_path)
    licenses = extract_data(licenses_path)

    libraries = []
    for lib in sbom['components']:
        for license in licenses:
            if license['Name'].upper().strip() == lib['name'].upper().strip():
                libraries.append({
                    "name": lib['name'],
                    "version": lib['version'],
                    "license": license['License'],
                    "reference": lib['externalReferences'][0]['url']
                })
                break
    return libraries

if __name__ == "__main__":
    libraries = main()
    readme_content = f"""# SOFTWARE BILL OF MATERIALS

This file contains specifications about libraries needed to execute project.

The file was written based on `requirements.txt`, aiming to catalog licenses of all packages.

## Libraries

"""
    
    for lib in libraries:
        readme_content += f"""###  {lib['name']}

**Version**: {lib['version']}

**License**: {lib['license']}

**Reference**: {lib['reference']}

"""

    with open('SBOM.md', 'w') as docs:
        docs.write(readme_content)