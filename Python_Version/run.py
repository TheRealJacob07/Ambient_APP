import api
import window
def run(location):
    file = api.run(location)
    window.app(file)
    print("refreshed")

print(api.forecast_run(2))
run(str(window.location()))

