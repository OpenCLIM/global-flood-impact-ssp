# global-flood-impact-ssp
This model is optional - users can select a future urban projection (ssp) and the chosen year (year). 
Data outputs from the UDM model must be added as input files, with the selected ssp and year included in the name. 
The outputs from UDM are usually in .zip file. No modifications to these need to be made.


## Input Parameters
* Year
  * Description: The future year of interest.
* SSP
  * Desctiption: The selected Shared Socio-Economic Pathway
    
## Input Files (data slots)
* SSP Datasets
  * Description: zipped outputs for all of the SSP scenario UDM outputs.
  * Location: /data/ssps

## Outputs
The model should output an updated csv file, with the additional two parameter results.
If there is a UDM output that matches the selected parameters, the file appears as an output ready to be unzipped and read.
