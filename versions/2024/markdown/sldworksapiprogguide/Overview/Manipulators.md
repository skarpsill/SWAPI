---
title: "Manipulators"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Manipulators.htm"
---

# Manipulators

You can create a manipulator to use in your part and assembly documents.

Typically to create a manipulator:

1. Create the handler interface,[ISwManipulatorHandler2](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwManipulatorHandler2.html),
  which your add-in application must implement. Your add-in application:

1. Create the[IManipulator](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IManipulator.html)object using[IModelViewManager::CreateManipulator.](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelViewManager~CreateManipulator.html)
2. Use the IManipulator methods and properties to:

1. Customize the size and appearance of the specific
  manipulator using the specific manipulator's methods and properties.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic0" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="EXCreateTriadManipulator$$**$$EXImplementManipulatorHandler$$**$$TriadManipulator_Object$$**$$DragArrowManipulator_Object$$**$$SwManipulatorHandler2_Object$$**$$Manipulator_Object$$**$$EXCreateDragArrowManipulator$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\Help\APIHelp with Document!X\sw2009\sldworksAPIProgGuide\Overview\Manipulators.htm">
<param name="_ID" value="RelatedTopic0">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
