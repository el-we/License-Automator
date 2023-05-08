const { exec } = require('child_process'); // module for executing shell scripts
const path = require('path'); // module for handling file paths

// path to the shell script
const scriptPath = path.join(__dirname, 'generate_license_files.sh');

// execute the shell script
exec(scriptPath, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing script: ${error.message}`);
    return;
  }

  if (stderr) {
    console.error(`Error output: ${stderr}`);
    return;
  }

  console.log(`Script output: ${stdout}`);
});
