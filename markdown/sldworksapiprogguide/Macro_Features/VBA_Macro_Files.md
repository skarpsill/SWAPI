---
title: "VBA Macro Files"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/VBA_Macro_Files.htm"
---

# VBA Macro Files

## VBA Macro Files and Macro Features

Macro features that use VBA macros to define the[macro
feature functions](Overview_of_Macro_Features.htm)must reside in SOLIDWORKS VBA macro files (*.swp).kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Each function:

- Must accept these three arguments, which must
  be declared as type VARIANT:

For example:

Function swmRegen(app As Variant, part As
Variant, feature As Variant) As Variant

- Can exist in the same or different file or module.

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
<param name="Items" value="IntroMacro$$**$$COMMacro$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\Macro_Features\VBA_Macro_Files.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
