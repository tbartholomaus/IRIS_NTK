# IRIS_NTK
Modifications to the IRIS Noise Tool Kit, in order to work with the polarization attributes bundle using python 3.  Tested here with python 3.7 and obspy 1.2.  The starting point for these modifications is found at https://seiscode.iris.washington.edu/projects/noise-toolkit-polarization-attributes-bundle, based on Koper and Hawley, 2010.

Customization of these commands is expected through the command line, such as net, sta, loc arguments, or through the parameter files.  See the [IRIS Noise Toolkit polarization attributes website](https://seiscode.iris.washington.edu/projects/noise-toolkit-polarization-attributes-bundle/wiki) for more instructions on the use of this package.

### Compute polarization attributes: `ntk_computePolarization.py`
Run in 1-hr bins, with 50% overlap.
>python bin/ntk_computePolarization.py param=computePolarization net=ZQ sta=RTBD loc=DASH start=2016-06-20T00:00:00 end=2016-10-04T00:00:00 type=frequency mode=0

Another version of this command, for use through an ssh connection, could be as follows.
> nohup python -u bin/ntk_computePolarization.py param=computePolarization net=ZQ sta=RTBD loc=DASH start=2016-06-20T00:00:00 end=2016-10-04T00:00:00 type=frequency mode=0 > RTBD2.log &

### Extract polarization attributes for a station: `ntk_extractPolarHour.py`
Pull out all polarization attributes as a function of both time and frequency/period.
> python bin/ntk_extractPolarHour.py param=extractPolarHour net=ZQ sta=RTBD loc=DASH chandir=HHZ_HHE_HHN start=2016-06-20T00:00:00 end=2016-10-04T00:00:00 type=frequency mode=0

### Plot polarization attributes in a spectrogram style: `ntk_spectrograms.py`
Python script.  Run, for example through Spyder or another IDE, rather than through the terminal window.
