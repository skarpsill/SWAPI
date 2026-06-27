---
title: "Components, Configurations, and Suppression States"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Components,_Configurations,_and_Suppression_States.htm"
---

# Components, Configurations, and Suppression States

To query the suppression states of a component across multiple configurations,
use:

- [IModelDoc2::ConfigurationManager](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDoc2~ConfigurationManager.html)
- [IConfigurationManager::GetConfigurationParams](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IConfigurationManager~GetConfigurationParams.html)

IConfigurationManager::GetConfigurationParams outputs an array of the
configured elements in the document, which is the same information shown
in a design table. If a component is suppressed in a specific configuration,
that component is included in the array. If a component's suppression
state is not output, then the component's suppression state applies to
all configurations.

To query the suppression states of subassembly components across multiple
configurations, you must query each of the subassembly documents and perform
the same operation.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic3" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="EXConfigParams$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\Help\APIHelp with Document!X\sw2009\sldworksAPIProgGuide\Overview\Components,_Configurations,_and_Suppression_States.htm">
<param name="_ID" value="RelatedTopic3">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
