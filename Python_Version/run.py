import api
import window
def run(location):
    file = api.run(location)
    window.app(file, location)
    print("refreshed")
run(str(window.location('j')))

