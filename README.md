# ziplip

`ziplip` is a Python package designed to help you find passwords for encrypted zip files efficiently and effectively. Whether you're a developer or a power user, `ziplip` offers a straightforward solution to password recovery for zip archives.

<img src="https://bytebreach.github.io/img/ziplip.jpg">

## Benefits and Advantages
### Why Choose ziplip?

- Easy to Use: With a simple command-line interface and a straightforward Python API, ziplip is user-friendly and accessible to users of all skill levels.

- Efficient: ziplip leverages optimized algorithms to quickly try multiple passwords, minimizing the time needed to find the correct one.

- Flexible Output Options: Customize your output with options like silent mode and only-print mode, giving you control over what information is displayed.

- Cross-Platform: Works seamlessly on Windows, macOS, and Linux.

### Advantages Over Other Tools

- Integrated Python API: Unlike many other tools that are command-line only, ziplip can be easily integrated into Python scripts, allowing for automation and customization within your own applications.

- Customization: Options like silent mode and only-print mode provide a level of customization that many other tools lack.
<table>
<thead>
        <tr>
            <th>Feature</th>
            <th>ziplip</th>
            <th>Other Tools</th>
        </tr>
</thead>
<tbody>
        <tr>
            <td>Command Line Usage</td>
            <td>Yes</td>
            <td>Yes</td>
        </tr>
        <tr>
            <td>Python API</td>
            <td>Yes</td>
            <td>No</td>
        </tr>
        <tr>
            <td>Silent Mode</td>
            <td>Yes</td>
            <td>Limited</td>
        </tr>
        <tr>
            <td>Only-Print Mode</td>
            <td>Yes</td>
            <td>No</td>
        </tr>
  <tr>
            <td>Cross-Platform</td>
            <td>Yes</td>
            <td>Varies</td>
        </tr>
        <tr>
            <td>Open Source</td>
            <td>No</td>
            <td>Varies</td>
        </tr>
    </tbody>
</table>

## Installation

You can install `ziplip` via pip:

```bash
pip install ziplip
```
## Command

```bash
ziplip --file file.zip --password password.txt
```
- `--file <zip_file>` : Specifies the path to the zip file.

- `--password <password_file>` : Specifies the path to the file containing a list of passwords to try.

- Use the specified zip file and password file. Prints each password tried and indicates when the correct password is found.

```bash
ziplip --file file.zip --password password.txt -s
```
- `-s`, `--silent` : Silent mode. Only shows the correct password, does not print each password tried.

- Use the specified zip file and password file. Silent mode; only prints the correct password when found, without showing each password tried.

```bash
ziplip --file file.zip --password password.txt --only-pass
```
- `--only-pass` : Only prints the passwords as they are tried, does not indicate whether the password was correct or not.

- Use the specified zip file and password file. Only prints each password as it is tried, without indicating if it was correct or not.

```bash
ziplip --file file.zip --password password.txt -s --only-pass
```

- Use the specified zip file and password file. Silent mode with only passwords printed as they are tried. Does not indicate when the correct password is found, if found.

## Python Code Examples

- Using ziplip from a Python script:
```python
import ziplip

password = ziplip.main(zip_file="hello.zip", password_file="pass.txt", silent=True, print_output=False)
if password:
    print("Password found:", password)
else:
    print("Password not found.")

```

### Add input box
```python
import ziplip

zip_file = input("Enter the path to the zip file: ")
password_file = input("Enter the path to the password file: ")
password = ziplip.main(zip_file=zip_file, password_file=password_file, silent=True, print_output=False)
if password:
    print("Password found:", password)
else:
    print("Password not found.")
```

### Add arguments
```python
import ziplip
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Find password for a zip file.")
    parser.add_argument("--file", required=True, help="Path to the zip file")
    parser.add_argument("--password", required=True, help="Path to the password file")
    return parser.parse_args()

def cli():
    args = parse_arguments()
    password = ziplip.main(args.file, args.password, print_output=False)
    if password:
        print("Password found:", password)
    else:
        print("Password not found.")

if __name__ == "__main__":
    cli()
```
### Usage 
```bash
python zip-crack.py --file zip-file.zip --password password-list.txt
```


## Thank You

Thank you for using `ziplip`! We appreciate your support and hope that this tool helps make your work easier and more efficient. `ziplip` was created with the goal of providing a simple, yet powerful, solution for recovering passwords from encrypted zip files. Your feedback and contributions are invaluable to us and help improve the tool continuously.

If you have any suggestions, issues, or just want to say hello, feel free to reach out via our GitHub repository. We are always looking for ways to make `ziplip` better and your input is a crucial part of that process.

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
