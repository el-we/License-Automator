# License-Automator
A set of helpful scripts for your license management.

This set of scripts automatically generates license files for your projects. It extracts license information from your project's dependencies, sorts them by license type, and generates an HTML file containing the sorted list of dependencies and their associated licenses.

## Installation

1. Clone or download this repository to your local machine.
2. Copy the scripts folder to your project's root directory.

## Usage

### Option 1: Using package.json scripts
1. Add the following line to your package.json file's scripts section:
```"generate-licenses": "node scripts/generateLicenses.js"```

2. Run the script from the terminal:
```npm run generate-licenses```

### Option 2: Running directly from the terminal
Navigate to your project's root directory and run the following command:
```node scripts/generateLicenses.js```

## Output

The script will generate an license.html file in each specified project folder, containing the sorted list of dependencies and their associated licenses.
