---
title: "Other Microsoft VBA-enabled Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Other_Microsoft_VBA-enabled_Applications.htm"
---

# Other Microsoft VBA-enabled Applications

Because Microsoft VBA is embedded in the SOLIDWORKS software, the SOLIDWORKS
software is VBA-enabled and can inter-operate with other VBA-enabled applications,
such as Microsoft Excel, Microsoft Access, and Microsoft Visio.

For example, you can create a VBA application in the SOLIDWORKS software
that attaches to a running instance of Microsoft Excel. You can then access
the active sheet and retrieve data to use with the SOLIDWORKS software.

The following code shows how to attach to the active Microsoft Excel
object, get the value in cell A1 in the active sheet, and use that value
to set the density in a SOLIDWORKS part.

' Attach to active Excel object

Set xl = GetObject(, "Excel.Application")

' Get active
sheet in Excel

Set xlsh = xl.ActiveSheetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

' Get value
in Excel cell A1

density = xlsh.Cells(1,1)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

' Set density
in SOLIDWORKS part

Part.SetUserPreferenceDoubleValue swMaterialPropertyDensity,
densitykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Alternatively you can also attach to a running instance of the SOLIDWORKS
software from a VBA application created in Microsoft Excel.

In general, if your application is primarily a SOLIDWORKS API application,
then develop the application in the SOLIDWORKS software.

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
<param name="Items" value="TypesApplications$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\GettingStarted\Other_Microsoft_VBA-enabled_Applications.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>metadata type="DesignerControl" endspan
