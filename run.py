import api
import window
import install
install.install('aioambient')
install.install('PySimpleGUI')
apidata = open('api.txt', 'r+t')
macdata = open('mac.txt', 'r+t')
z = apidata.readline()
y = macdata.readline()
if z == 'api':
    window.api_app()
if y == 'mac':
    window.mac_app()
window.app()