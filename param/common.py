import os
#
# Noise Toolit common configuration parameters
#

#
# how file naming is done
# PQLX if file name contains time, it will be in HH24:MM:SS format
# WINDOWS if file name contains time, it will be in HH24_MM_SS format
#
namingConvention = "WINDOWS" # use 'WINDOWS' or 'PQLX'

#
# Directories
#
ntkDirectory     = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dataDirectory    = os.path.join(ntkDirectory,"data")
#respDirectory    = None
respDirectory    = os.path.join(dataDirectory,"resp") # to disable looking for response files on local drives, set this parameter to None. Otherwise, set it to the response directory path
workDir          = os.path.join(ntkDirectory,"scratch")
pdfDirectory     = "PDF"
psdDirectory     = "PSD"
polarDbDirectory = "polarDb"
psdDbDirectory   = "psdDb"
powerDirectory   = "POWER"
polarDirectory   = "POLAR"
imageDirectory   = "IMAGE"

