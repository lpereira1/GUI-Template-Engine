# GUI-Template-Engine

This Application helps to create multiple files based on a template and csv file.


To use this you will need Python3.6 or higher, and to have the tk (tkinter) library installed. This should be included in the windows
python distribution but on linux you may need to "sudo apt install python3-tk"

Run "GUI-Router.py"

Select your Template containing the Entries you want to replace with ##{ENTRY} such as below, only required entry is HOST_NAME as this is
currently the entry used to name the output file:

-------TEMPLATE EXAMPLE -----------------------------------

hostname ##{HOST_NAME}
!
!
!
!
interface Loopback0
ip address ##{IP1} ##{SUBNET1}
!
!
interface Loopback1
ip address ##{IP2} ##{SUBNET2}
!
!
!
router bgp ##{BGP_AS}
!
!
!
------------END EXAMPLE-------------------------------------


Select your CSV File. This should have each Template entry as a column header: 

Example CSV: 

HOST_NAME,IP1,SUBNET1,IP2,SUBNET2,BGP_AS
ROUTER1,10.1.0.1,255.255.255.0,10.2.0.1,255.255.255.0,65525
ROUTER2,10.1.0.2,255.255.255.0,10.2.0.2,255.255.255.0,65504

----------------------------------------------------------------

Finally select the output directory where the outfile files should be sent. They will be saved using HOST_NAME.config in the file.

