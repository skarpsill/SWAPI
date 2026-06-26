---
title: "Accessing Bodies in Body Folders"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Accessing_Bodies_in_Body_Folders.htm"
---

# Accessing Bodies in Body Folders

The[IBodyFolder](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder.html)interface lets you access bodies in solid, surface, and various weldment
body folders.

1. If traversing the FeatureManager design tree,
  then use[IFeature::GetTypeName](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetTypeName.html)to determine the type of feature. If the feature is any of the following
  types, then you have a body folder feature:

- or -

If you selected a folder and it is any of
the following types of folders, then you have a body folder feature:

- swSelBODYFOLDER
- swSelSUBATOMFOLDER
- swSelSUBWELDFOLDER

NOTE:A top-level folder feature namedCut
listis identified as SolidBodyFolder, a solid body folder feature.
Any subfolder feature namedCut-List-Itemis identified CutListFolder, a cut list subfolder feature.

1. Call[IFeature::GetSpecificFeature2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetSpecificFeature2.html)to get the BodyFolder interface.
2. Call[IBodyFolder::Type](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~Type.html)to get the type of body folder.
3. Call[IBodyFolder::GetBodyCount](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~GetBodyCount.html)to get the number
  of bodies in the folder and call[IBodyFolder::GetBodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~GetBodies.html)to get the bodies in the folder in the order in which they appear in the
  FeatureManager design tree.NOTE:These methods deal only with the bodies in the folder; they do
  not include the bodies within any subfolders. You must call[IFeature::GetFirstSubFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetFirstSubFeature.html)and[IFeature::GetNextSubFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetNextSubFeature.html)to traverse through the subfolders.
4. To get the feature for a body, call[IBodyFolder::GetFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~GetFeature.html).

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
<param name="Items" value="EXGetBodiesBodyFolders$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\APIHelp with Document!X\sw2009\sldworksAPIProgGuide\Overview\Accessing_Bodies_in_Body_Folders.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
