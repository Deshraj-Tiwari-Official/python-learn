def http_status(status):
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case _:
            print("Something else")


http_status(404)
http_status(200)
http_status(500)
