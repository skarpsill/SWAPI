---
title: "Visual C++ 6 Standalone and Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Visual_CPP_6_Standalone_and_Add-in_Applications.htm"
---

# Visual C++ 6 Standalone and Add-in Applications

## Visual C++ 6.0 Standalone and Add-in Applications

### Standalone Applications (.exe files)

To create an instance of the SOLIDWORKS software, your executable project
should contain lines of code similar to the following:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//Import the SOLIDWORKS type library

#import "[sldworks.tlb](../Overview/Type_Libraries.htm)"
raw_interfaces_only, raw_native_types, no_namespace, named_guids

//Import the SOLIDWORKS constant type librarykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

#import "[swconst.tlb](../Overview/Type_Libraries.htm)"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}raw_interfaces_only,
raw_native_types, no_namespace, named_guidskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

int _tmain(int argc, _TCHAR* argv[])kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

{

//Initialize COM

CoInitialize(NULL);kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//Use[ATL smart pointers](../Overview/Smart_Pointers.htm)

CComPtr<ISldWorks> swApp;

//Create an instance of SOLIDWORKS

HRESULT hres = swApp.CoCreateInstance(__uuidof(SldWorks),
NULL, CLSCTX_LOCAL_SERVER);

.

.// Your
code

.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//Shut down SOLIDWORKS

swApp->ExitApp();

//Release COM reference

swApp = NULL;

//Uninitialize COM

CoUninitialize();

return 0;

}

### Add-in Applications (.dll files)

Visual C++ applications have the option of using a COM or Dispatch interface.
See[COM vs. Dispatch](../Overview/COM_vs_Dispatch.htm)for
details.

NOTE:For COM DLL add-ins, success
or failure on import/export is returned by the add-in through the HRESULT.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic1" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="StandaloneApplicationsLibraries$$**$$VisualC++NETStandaloneApplicationsLibraryFiles$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\GettingStarted\Visual_CPP_6_Standalone_and_Add-in_Applications.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
