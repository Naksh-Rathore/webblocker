# This is a website blocker made in Python!

### Hosts File
It uses the hosts file found in C:\Windows\System32\drivers\etc\hosts on Windows.
It is used to map hostnames to IP addresses on your local machine.<br /><br />

You can put 127.0.0.1 as the IP address for a URL and it will lead it to the local machine, making it unusable.<br />

For example, to make YouTube unusable, you can do this:
`127.0.0.1 www.youtube.com`<br />

![Edit Hosts File in Windows 11](https://allthings.how/content/images/wordpress/2021/07/allthings.how-how-to-edit-hosts-file-in-windows-11-image-1.png)<br />

### Usage and Logic
This script uses file reading and writing to hosts.txt to block websites.<br /><br />

To block and unblock a website, you can do this:
```python
def block_website(websites):
  try:
      with open(hosts_path, "r+") as file:
          content = file.read()
  
          for website in websites:
              if website not in content:
                  file.write(f"127.0.0.1 {website}\n")
  
  except PermissionError:
      print("Run as admin")

def unblock_websites(websites):
    try:
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

    except PermissionError:
        print("Run as admin")

```

To unlock the websites, input the password or answer a quiz with 100% marks.

### Have a Great Day!
