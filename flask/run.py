import os
from app.__init__ import createApp
from app.helpers.catchRouteErrors import catchRouteErrors

APP = createApp()

catchRouteErrors(APP)

# if __name__ == "__main__":
#     APP.run()
