import urllib.parse
import requests

while True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    orig = input("Enter starting point: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Enter Destination point: ")
    if dest == "quit" or dest == "q":
        break
    key = "vCEv5bHBSnKg9o8dJppJ13Dp5rekbRK9"


    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")