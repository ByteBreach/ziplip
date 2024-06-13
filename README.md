# ziplip

**ziplip** is a powerful and professional tool designed to help you unlock password-protected zip files effortlessly. This Python package supports a wide range of devices, making it accessible for everyone. It is especially tailored for Linux users, ensuring optimal performance and usability.

<img src="https://bytebreach.github.io/img/ziplip.jpg">



## Features

- **Password Testing**: Efficiently attempts to unzip a password-protected zip file using a list of potential passwords.
- **Silent Mode**: Suppresses output of password attempts, only displaying the found password for a clean and unobtrusive experience.
- **Automatic Extraction**: Automatically extracts the zip file after finding the correct password, saving you time and effort.
- **Save Found Password**: Conveniently saves the found password to a specified file for future reference.
- **Cross-Device Support**: Designed to work seamlessly across various devices and platforms, with a focus on Linux systems.

## Usage

```bash
ziplip --zip <zip_file> --pass <password_list> [--unzip] [--save <file>] [--silent]
```

### Options

- `--zip <zip_file>`: Specifies the zip file to be tested.
- `--pass <password_list>`: Specifies the file containing the list of passwords.
- `--unzip`: Automatically extracts the zip file after finding the correct password.
- `--save <file>`: Saves the found password to the specified file.
- `--silent`: Suppresses output of password attempts, only displaying the found password.

### Examples

1. **Basic usage**:
```bash
ziplip --zip file.zip --pass password.txt
```

3. **Unzip after finding the password**:
```bash
ziplip --zip file.zip --pass password.txt --unzip
```

5. **Save the found password to a file**:
```bash
ziplip --zip file.zip --pass password.txt --save find-pass.txt
```

7. **Silent mode (no password attempts displayed)**:
 ```bash
 ziplip --zip file.zip --pass password.txt --silent
 ```

8. **Silent mode and save the password to a file**:
```bash
ziplip --zip file.zip --pass password.txt --silent --save find-pass.txt
```

10. **Unzip and save the password to a file**:
```bash
ziplip --zip file.zip --pass password.txt --unzip --save find-pass.txt
```

12. **Silent mode and unzip after finding the password**:
```bash
ziplip --zip file.zip --pass password.txt --silent --unzip
```

14. **All flags together**:
   ```bash
ziplip --zip file.zip --pass password.txt --silent --unzip --save find-pass.txt
```

## Benefits

- **Efficiency**: Quickly test a large number of passwords without manual intervention, thanks to our optimized algorithm.
- **Automation**: Automatically extract the zip file once the correct password is found, streamlining your workflow.
- **Flexibility**: Save the found password to a file for future reference, ensuring you never lose access again.
- **Convenience**: Silent mode allows for unobtrusive password testing, only notifying when the correct password is found, perfect for professional environments.
- **Cross-Device Compatibility**: Supports a wide range of devices and platforms, making it a versatile tool for any user.
- **Linux Optimization**: Specifically designed for Linux users, ensuring the best performance and compatibility on your system.

## Disclaimer

### Responsibility

Please note that while `ziplip` is designed to be a helpful tool, the developers are not responsible for any misuse or damages that may arise from its use. Here are some important points to consider:

- **Legal Use**: Ensure that you have the legal right to access the zip files you are attempting to unlock. Unauthorized access to data is illegal and unethical.
- **Data Integrity**: Using password recovery tools can sometimes cause issues with the integrity of the zip file. Always make sure you have a backup of your files before attempting to recover passwords.
- **No Warranty**: `ziplip` is provided "as is" without any warranty of any kind, express or implied. The use of `ziplip` is at your own risk.

By using `ziplip`, you agree to these terms and understand that the developers cannot be held liable for any direct, indirect, incidental, or consequential damages that may occur from the use of this software.

Thank you once again for choosing `ziplip`! Happy coding!

---

Team : <a href="https://github.com/ByteBreach">ByteBreach</a>
