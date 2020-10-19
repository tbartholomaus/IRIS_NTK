import common
import os

#
# how file naming is done
#
namingConvention = common.namingConvention

#
# initialize a few parametrs
#
VERBOSE       = 0         # thurn the verbose mode on or off
userAgent     = "product_pub_noise-toolkit_polarization" # userAgent is used to identify the data requester, please change
plot          = 0         # turn plotting on or off
figureSize    = (18.0, 12.0) # image size (widt, height)
plotTraces    = 0         # plot trace?
plotSpectra   = 1         # plot spectra?
plotSmooth    = 0         # plot the smoothed spectra?
outputValues  = 1         # output smooth values
colorSpectra  = "blue"    # spectra plot color
colorTrace    = "blue"    # timeseries plot color
colorSmooth   = "red"     # smooth plot color orange

#
# smoothing
#
# smoothing window width in octave 
# for test against PQLX use 1 octave width
#
doSmoothing      = True
octaveWindowWidth= float(1.0/4.0)   # smoothing window width : float(1.0/1.0)= 1 octave smoothing; float(1.0/4.0) 1/4 octave smoothing, etc
octaveWindowShift= float(1.0/8.0)   # smoothing window shift : float(1.0/4.0)= 1/4 octave shift; float(1.0/8.0) 1/8 octave shift, etc

ntkDirectory     = common.ntkDirectory
workDir          = common.workDir
dataDirectory    = common.dataDirectory
#respDirectory    = common.respDirectory
respDirectory    =  "/Users/timb/Documents/syncs/OneDrive - University of Idaho/RESEARCHs/LemonCrk_GHT/Seis_analysis/RESP/"

polarDbDirectory = common.polarDbDirectory # Polarization database directory where individual polarization files are stored

xType            = ["period","frequency"]
xStart           = ["Nyquist","Nyquist"] # smoothing starting ferqueny/period reference (Nyquist= Nyquist frequency, 1= 1Hz/1Sec)
xlabel           = {"period":"Period (s)", "frequency":"Frequency (Hz)"}
header           = {"period":"     Period   PowerUD  powerEW     powerNS      Lambda      Beta^2      ThetaH      ThetaV       PhiVH       PhiHH",
                  "frequency":"   Frequency  PowerUD     powerEW     powerNS      Lambda      Beta^2      ThetaH      ThetaV       PhiVH       PhiHH"}
showHeader       = 1


maxT             = 100
windowLength     = 3600    # seconds, subwindows of the above window for processing
windowShift      = int(windowLength * 0.5) # 50% overlap

# 
#  NOTE: make sure that components in each group are in the CORRECT order (BHZ, BHE, BHN)
# 
channel          = "HH?"
channelGroups    = [['BHZ','BHE','BHN'],['BHZ','BH2','BH1'],["HHZ","HHE","HHN"],["HHZ","HH2","HH1"]]

#
# decon filter frequency bands, Hz
# define a filter band to prevent amplifying noise during the deconvolution
#
performInstrumentCorrection = True
applyScale      = True # True will scale the waveform by the stage-zero gain, not used if performInstrumentCorrection above is set to True
waterLevel      = 120  # set water-level in db to use it when inverting spectrum. The ObsPy module shrinks values under 
                    # water-level of max spec amplitude. In other wortds, water-level represents a clipping of the inverse spectrum and 
                    # limits amplification to a certain maximum cut-off value
                    # see: http://docs.obspy.org/master/_modules/obspy/core/trace.html#Trace.remove_response
                    #

#
# Units to return response in ('DIS', 'VEL' or ACC)
#
unit              = "ACC"
unitLabel         = "m/s/s"

#
# if instrument response correction is not requested, then units must be provided by user
# under generic label of "SEIS" for seismic and "INF" for infrasound
#
powerUnits        = {"M/S":"Power[10 log10(m**2/s**4/Hz)](dB)","PA":"Power[10 log10(Pascals**2/Hz)](dB)"} if performInstrumentCorrection else {"SEIS":"Power[10 log10(m**2/s**2/Hz)](dB)","INF":"Power[10 log10(Pascals**2/Hz)](dB)"}



#
# plot parameters
#
ylimLow        = {}
ylimHigh       = {}
xlimMin        = {}
xlimMax        = {}

variables      = ["powerUD","powerEW","powerNS","powerLambda","betaSquare","thetaH","thetaV","phiVH","phiHH"]

periodMin      = 0.01
periodMax      = 100
for var in variables:
   xlimMin.update({var:{"period":periodMin,"frequency":1.0/periodMax}})
   xlimMax.update({var:{"period":periodMax,"frequency":1.0/periodMin}})

ylimLow        = {"powerUD":-200,
                  "powerEW":-200,
                  "powerNS":-200,
                  "powerLambda":-200,
                  "betaSquare":0,
                  "thetaH":0,
                  "thetaV":0,
                  "phiVH":-90,
                  "phiHH":-180
                 }

ylimHigh       = {"powerUD":-70,
                  "powerEW":-70,
                  "powerNS":-70,
                  "powerLambda":-70,
                  "betaSquare":1,
                  "thetaH":360,
                  "thetaV":90,
                  "phiVH":90,
                  "phiHH":180
                 }

subplot      = {"powerUD":331,"powerEW":334,"powerNS":337,"powerLambda":332,"betaSquare":335,"thetaH":338,"thetaV":333,"phiVH":336,"phiHH":339}
yLabel       = {"powerUD":"UD " + powerUnits['M/S'],
                "powerEW":"EW " + powerUnits['M/S'],
                "powerNS":"NS " + powerUnits['M/S'],
                "powerLambda":"Lambda power/dB",
                "betaSquare":"degree of polarization (Beta^2)",
                "thetaH":"Polarization azimuth (Theta H)",
                "thetaV":"Polarization inclination (Theta V)",
                "phiVH":"V-H phase difference (Phi VH)",
                "phiHH":"H-H phase difference (Phi H-H)"}

#
# decon filter
# define a filter band to prevent amplifying noise during the deconvolution
#
deconFilter1 = 0.01 # you may set ALL deconFilter parameter values to <= 0 to bypass this filter
deconFilter2 = 0.05
deconFilter3 = 80.0
deconFilter4 = 100.0

#
# normalization factor to be included while converting power to PSD
# set to 1.0 if extra factor is not needed
#
#normFactor = 1.0
normFactor = 2.0

##################################################################################
#
# requestClient to call to get the waveforms from (FDSN, IRIS or FILES). 
#
# most waveforms should be requested using FDSN
# for restricted data access, you need user and password information
# for information on how to access restricted data see:
# http://service.iris.edu/irisws/timeseries/1/
#
##requestClient = "FDSN"

##user          = None
##password      = None
###user          = 'nobody@iris.edu' # anonymous access user
###password      = 'anonymous'       # anonymous access password

#
# you can read files from local disk (using filTag to point to them)
# and get the response from IRIS DMC
#
requestClient = "FILES"
fromFileOnly  = True # get responses from local files only. If False, will go to IRIS to get the missing responses
<<<<<<< HEAD
fileTag       = "../../day_vols/LEMON/BBEL/*"#os.path.join(dataDirectory,"SAC","*.SAC")
=======
fileTag       = "/Users/timb/Documents/syncs/OneDrive - University of Idaho/RESEARCHs/LemonCrk_GHT/Seis_analysis/DATA/BBEL/*HH*"#"../../day_vols/LEMON/BBEL/"#os.path.join(dataDirectory,"SAC","*.SAC")
>>>>>>> bdb06cb0e79c689edee4d9e1d8213839ed2c2e03
#
##################################################################################

#
# segment parameters
#
nSegments      = 15  # total number of segments to calculate FFT for a window
percentOverlap = 50  # percent segment overlap
nSegWindow     = int((nSegments-1)*(1.0-float(percentOverlap)/100.0)) + 1   # number of side-by-side segments for the above nSegments and percent Overlap
                                                                       # There are (nSegments -1) non-overlaping segments and 1 full segment


#
# trace scaling for display
#
scaling = 1

