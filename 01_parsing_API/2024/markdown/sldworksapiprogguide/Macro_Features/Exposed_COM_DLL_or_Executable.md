---
title: "Exposed COM DLL or Executable and Macro Features"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Exposed_COM_DLL_or_Executable.htm"
---

# Exposed COM DLL or Executable and Macro Features

For macro features that define their behavior using COM, a COM server
needs to implement the[ISwComFeature](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature.html)interface. This interface has three methods that must be implemented in
the appropriate[macro feature
function](Overview_of_Macro_Features.htm):

- [ISwComFeature::Edit](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature~Edit.html)in the edit definition function
- [ISwComFeature::Regenerate](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature~Regenerate.html)in the rebuild function
- [ISwComFeature::Security](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature~Security.html)in the security function

To associate the COM server with the macro feature, supply the program
ID of the COM server as an argument to[IFeatureManager::InsertMacroFeature3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~InsertMacroFeature3.html)or[IFeatureManager::IInsertMacroFeature3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~IInsertMacroFeature3.html).

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
<param name="Items" value="IntroMacro$$**$$VBAMacro$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\Macro_Features\Exposed_COM_DLL_or_Executable.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
