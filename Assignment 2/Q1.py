import numpy, json, requests
with open('api.text', 'r') as APIFILE:
    url = APIFILE.read()
    print(url)
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Error occured: {str(e)}")
print(response.status_code)
if response.status_code != 200:
    print(f"Http error: {response.status_code}, text: {response.text}")
res = response.json()
#API INFO METADATA

info = res.get("info", [])
statusOFAPI = res.get('status')
print(f"Api Info: {info}")
print(f"Status: {statusOFAPI}")

if res.get('status') != "success":
    error = res.get('reason')
    print(f"Error: {error}")
elif "data" not in res:
    print(f"No Data available for match")
else:
    print("Match data available")
content = res.get("data", [])
for matches in content:
    print("---------------------------------")
    print(f"Match name: {matches.get("name")}")
    print(f"Match Status: {matches.get("status")}")
    print(f"Venue: {matches.get("venue")}")
    print(f"Date: {matches.get("date")}")
    if "score" in matches:
        score = matches.get("score", [])
        for s in score:
            print("    ----------------------------")
            print(f"    Inning : {s.get('inning')}")
            print(f"    Runs: {s.get('r')}")
            print(f"    Wickets: {s.get('w')}")
            print(f"    Overs: {s.get('o')}")