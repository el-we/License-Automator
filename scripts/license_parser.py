import json
import sys
import re


def parse_license_data(json_data, license_texts, manual_matches):
    data = json.loads(json_data)

    # Group the repos by license type
    license_groups = {}
    for key, value in data.items():
        # Check if there's a manual match for this repo
        if key in manual_matches:
            license_types = [manual_matches[key]]
        else:
            license_types = value['licenses']
            if not isinstance(license_types, list):
                license_types = [license_types]

        for license_type in license_types:
            # If there's an 'AND' in the license_type, split the licenses
            if ' AND ' in license_type:
                licenses = re.split(r' AND ', license_type)
            # If there's an 'OR' in the license_type, choose the first option
            elif ' OR ' in license_type:
                licenses = [re.findall(r'\w[\w.-]*', license_type)[0]]
            else:
                licenses = [license_type]

            for license in licenses:
                # Remove any leading '(' or trailing '*' and ')'
                license = license.strip("()*")

                if license not in license_groups:
                    license_groups[license] = []
                license_groups[license].append(key)

    # Sort the repo names within each license group
    for license_type, repos in license_groups.items():
        repos.sort()

    # Sort the license groups by license name
    sorted_license_groups = sorted(license_groups.items())

    output_html = ""

    for license_type, repos in sorted_license_groups:
        output_html += "<div>\n"
        output_html += f"<span> {license_type} </span>\n"
        output_html += "<ul>\n"

        for repo in repos:
            output_html += f"\t<li>{repo}</li>\n"

        output_html += "</ul>\n</br>\n"
        
        license_text = license_texts.get(license_type, f"Full license text for {license_type} not found.")
        output_html += f"{license_text}\n"
        output_html += "</div>\n</br>\n"
    
    return output_html


def main():
    input_json_file = sys.stdin.read()
    with open("scripts/license_texts.json", "r") as f:
        license_texts = json.load(f)

    # Define the manual matches dictionary here
    manual_matches = {
        "example-repo@1.0.0": "MIT",
        # Add more manual matches as needed, can be found by using the following command:
        # license-checker --json > license_data.json
        # inside one of the subfolders like frontend-app
        # then searching license_data.json for the repo name
        "defaultable@0.7.2": "Apache-2.0",
        "aws-sign@0.2.0": "Apache-2.0",
        "cookie-jar@0.2.0": "Apache-2.0",
        "forever-agent@0.2.0": "Apache-2.0",
        "hbo-dnsd@0.9.8": "Apache-2.0",
        "node-options@0.0.6": "Apache-2.0",
        "oauth-sign@0.2.0": "Apache-2.0",
        "request@2.16.6": "Apache-2.0",
        "tunnel-agent@0.2.0": "Apache-2.0",
        "base64id@0.1.0": "Base64id License",
        "boom@0.3.1": "Boom License",
        "cryptiles@0.1.0": "Cryptiles License",
        "hawk@0.10.2": "Hawk License",
        "hoek@0.4.2": "Hoek License",
        "hoek@0.7.6": "Hoek License",
        "json-stringify-safe@3.0.0": "ISC",
        "sntp@0.1.2": "SNTP License",
        "native-dns@0.6.1": "Native-DNS License",
        "blob@0.0.2": "MIT",
        "colors@0.6.2": "MIT",
        "dns@0.2.2": "MIT",
        "socket.io-parser@2.1.2": "MIT",
        "socket.io-parser@2.2.0": "MIT",
        "tinycolor@0.0.1": "MIT",
        "webpack-chain@6.5.1": "MPL-2.0",
        "argparse@2.0.1": "Python-2.0",
        "binaryheap@0.0.3": "PDM",
        "buffercursor@0.0.12": "PDM",
        "cycle@1.0.3": "PDM",
        "emitter@1.0.1": "PDM",
        "native-dns-cache@0.0.2": "PDM",
        "tomahawk@0.1.6": "PDM",
        "tomahawk-plugin-kv-memory-store@0.0.3": "PDM",
        "utf8@2.0.0": "UTF-8 License",
    }

    output_text = parse_license_data(input_json_file, license_texts, manual_matches)
    print(output_text)


if __name__ == "__main__":
    main()
