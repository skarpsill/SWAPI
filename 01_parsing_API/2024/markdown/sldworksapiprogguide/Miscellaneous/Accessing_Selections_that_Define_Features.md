---
title: "Accessing Selections that Define Features"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Miscellaneous/Accessing_Selections_that_Define_Features.htm"
---

# Accessing Selections that Define Features

#### To access selections that define features:

1. First, call theAccessSelectionsmethod for that feature data object (e.g.,[ICosmeticThreadFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ICosmeticThreadFeatureData.html),[IExtrudeFeatureData2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IExtrudeFeatureData.html),[IRevolveFeatureData2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IRevolveFeatureData2.html),[ISweepFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData.html),
  etc.).
2. Then, call the desired method for that feature
  data object.
3. Finally,
  release the feature data object:

(Table)=========================================================

begin!kadov{{

}}end!kadov

| If you... | Then... |
| --- | --- |
| modified the feature data object using IFeature::ModifyDefinition or IFeature::IModifyDefinition2 | the feature data object is automatically released. |
| did not modify the feature data object | call that feature data object's ReleaseSelectionAccess method. |

begin!kadov{{

}}end!kadov

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
<param name="Items" value="Feature List$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\Miscellaneous\Accessing_Selections_that_Define_Features.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
