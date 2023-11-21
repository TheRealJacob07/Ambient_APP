import api
import window
def run():
    file = api.run()
    window.app(file)
    print("refreshed")

run()
