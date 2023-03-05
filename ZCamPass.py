import requests
from bs4 import BeautifulSoup
from termcolor import colored



# Display the banner message

banner = """

 ____      ___               ___
|_  /___  / __| __ _  _ __  | _ \ __ _  ___ ___
 / /|___|| (__ / _` || '  \ |  _// _` |(_-<(_-<
/___|     \___|\__,_||_|_|_||_|  \__,_|/__//__/


"""
print(colored(banner, 'green', attrs=['bold']))





def search_camera_info(name):
    url = "https://www.ispyconnect.com/userguide-default-passwords.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    rows = table.findAll('tr')
    cameras = []
    for row in rows[1:]:
        cols = row.findAll('td')
        if name.lower() in cols[0].text.lower():
            cameras.append({
                "Manufacturer": cols[0].text.strip(),
                "Username": cols[1].text.strip(),
                "Password": cols[2].text.strip(),
                "Default IP": cols[3].text.strip()
            })
    return cameras

def main():
    print(colored("Thank you for downloading Z-CamPass 1.0\nthis script helps pentesters to test the level of security of surveillance cameras in a network\nit is a script that contains a database of ip address and password as well as the default username of the cameras\nyou could contact me on my address zineddineabdou91@gmail.com or my linkdin zine eddine abdou for more information ", 'green', attrs=['bold']))
    print(colored("Important: the script does not work without an internet connection!  ", 'red', attrs=['bold']))
    while True:
        name = input("Please enter the camera manufacturer's name (or type 'exit' or 'q' to quit): ")
        if name.lower() in ['exit', 'q']:
            print(colored("See you soon!", 'green', attrs=['bold']))
            break
        cameras = search_camera_info(name)
        if len(cameras) > 0:
            print(colored("I found the default settings for your camera!", 'yellow', attrs=['bold']))
            for camera in cameras:
                print(colored(f"Manufacturer: {camera['Manufacturer']}", 'blue', attrs=['bold']))
                print(colored(f"Username: {camera['Username']}", 'green', attrs=['bold']))
                print(colored(f"Password: {camera['Password']}", 'green', attrs=['bold']))
                print(colored(f"Default IP: {camera['Default IP']}", 'green', attrs=['bold']))
        else:
            print(colored("Sorry, but I could not find the name of this camera. Please check your spelling or type an exact name.", 'red', attrs=['bold']))

if __name__ == "__main__":
    main()
