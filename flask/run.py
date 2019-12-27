import os
from app.__init__ import createApp
from app.helpers.catchRouteErrors import catchRouteErrors
from app.views import addResources

APP = createApp()

addResources(APP)

catchRouteErrors(APP)

# if __name__ == "__main__":
#     APP.run()
