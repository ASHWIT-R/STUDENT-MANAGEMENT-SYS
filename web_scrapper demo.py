import requests
from bs4 import BeautifulSoup
url = "https://www.lkouniv.ac.in/"
if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print("\nwebsite title:", soup.title.string)
print("Status Code of this:", response.status_code)

if soup.title:
    pass
else:
    print("No title found for the website.")
# ---------------------------
# ------------HEADINGS--------
# ----------------------------

print("\nHeadings of this website:")

headings = soup.find_all(["h1","h2","h3"])
print("Number of headings:", len(headings))

for heading in headings:
    print(heading.get_text(strip=True))

# ---------------------------
# ----------LINKS------------
# ----------------------------
print("\nLinks:")
links = soup.find_all("a", href=True) #HREF (HYPERTEXT REFRENCE) IS AN HTML ATTRIBUTR CONTAINS DESTINATION OF URL

for link in links:
    print(link.get_text(strip=True))
    print(link["href"])

# ---------------------------
# ----------IMGS------------
# ----------------------------
print("\nImages:")

images = soup.find_all("img")

for image in images:
    print(image.get("src"))

# ---------------------------
# ----------STATS------------
# ----------------------------
print("\n========== PAGE STATISTICS ==========")

print("H1 tags:", len(soup.find_all("h1")))
print("H2 tags:", len(soup.find_all("h2")))
print("H3 tags:", len(soup.find_all("h3")))
print("Links:", len(soup.find_all("a")))
print("Images:", len(soup.find_all("img")))
print("Paragraphs:", len(soup.find_all("p")))

keyword = input("\nEnter a keyword to search: ")

page_text = soup.get_text(" ", strip=True) #strip=True is used to remove extra spaces and new lines from text.STRIP  

if keyword.lower() in page_text.lower():
    print("Keyword found!")
else:
    print("Keyword not found.")
