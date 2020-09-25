###########################################################
#
# HISTORY:
#    2017-01-18 Manoch: added support for '' (blank) location codes
#                       blank location codes can be represented as blank or None
#    2014-02-07 Manoch: created
#
###########################################################
#
# check for blank location codes (DASH)
#
def getLocation(location):
    if location.strip().lower() == "dash":
       return  "--"
    elif len(location.strip()) == 0 or location.strip().lower() == "none":
       return  "--" #TCB Changes this from "" to "--" 
    else:
       return  location.strip()
