# IRIS_NTK
Modifications to the IRIS Noise Tool Kit, in order to work with the polarization attributes bundle using python 3.  Tested here with python 3.7 and obspy 1.2.  The starting point for these modifications is found at https://seiscode.iris.washington.edu/projects/noise-toolkit-polarization-attributes-bundle, based on Koper and Hawley, 2010.

Customization of these commands is expected through the command line, such as net, sta, loc arguments, or through the parameter files.  See the [IRIS Noise Toolkit polarization attributes website](https://seiscode.iris.washington.edu/projects/noise-toolkit-polarization-attributes-bundle/wiki) for more instructions on the use of this package.

### Compute polarization attributes: `ntk_computePolarization.py`
Run in 1-hr bins, with 50% overlap.
>python bin/ntk_computePolarization.py param=computePolarization net=ZQ sta=RTBD loc=DASH cha=HH? start=2016-06-20T00:00:00 end=2016-10-04T00:00:00 type=frequency mode=0

Another version of this command, for use through an ssh connection, could be as follows.
> nohup python -u bin/ntk_computePolarization.py param=computePolarization net=ZQ sta=RTBD loc=DASH cha=HH? start=2016-06-20T00:00:00 end=2016-10-04T00:00:00 type=frequency mode=0 > RTBD2.log &

For *debugging* or other trouble-shooting, while modifying the function within Spyder or another IDE, you can use the following, and insert `breakpoint()` at the crash points.
> %run bin/ntk_computePolarization.py param=computePolarization net=IU sta=ANMO loc=10 cha=BH? start=2010-02-01T01:00:00 end=2010-02-01T02:00:00 type=frequency mode=plot

#### For use with local files
Only the parameter file `param/computePolarization.py` needs to be modified to use these scripts on local files.  There are two specific places where this file should be modified:
1. **requestClient** should be changed from "FDSN" to "FILES".
2. **respDirectory** should be a string (enclosed in "") with the path to an appropriate stationXML or response file.  This path should end in a forward slash (/).
3. **fileTag** should be a string (enclosed in "") with the path to the data files, including the operative files identifed with typical glob characters, such as "path/to/files/\*HH\*"
Example use to run the code with local files is as follows:
> nohup python -u bin/ntk_computePolarization.py param=computePolarizationLEMON net=LM sta=BBEL loc=DASH cha=HH? start=2017-06-29T00:00:00 end=2017-10-04T00:00:00 type=frequency mode=0 > BBEL.log &

### Extract polarization attributes for a station: `ntk_extractPolarHour.py`
Pull out all polarization attributes as a function of both time and frequency/period.
> python bin/ntk_extractPolarHour.py param=extractPolarHour net=ZQ sta=RTBD loc=DASH chandir=HHZ_HHE_HHN start=2016-06-20T00:00:00 end=2016-10-04T00:00:00 type=frequency mode=0

### Plot polarization attributes in a spectrogram style: `ntk_spectrograms.py`
Python script.  Run, for example through Spyder or another IDE, rather than through the terminal window.
