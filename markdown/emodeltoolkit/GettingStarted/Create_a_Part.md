---
title: "Create a Part"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/GettingStarted/Create_a_Part.htm"
---

# Create a Part

See Also

You will typically follow these steps to create a part using the eModelToolkit.

1. Create an application using[eDApplication::Create](../eDApplication/eDApplication_Class.htm).
2. Create a scene ([eDScene](../eDScene/eDScene_Class.htm))
  using[eDApplication::CreateScene](../eDApplication/eDApplication_Class.htm).
3. Create and add a new configuration ([eDConfiguration](../eDConfiguration/eDConfiguration_Class.htm))
  to that scene using[eDScene::CreateConfiguration](../eDScene/eDScene_Class.htm).
4. Create and add a new part ([eDPart](../eDPart/eDPart_Class.htm))
  to that configuration using[eDConfiguration::CreatePart](../eDConfiguration/eDConfiguration_Class.htm).
5. Create a new body ([eDBody](../eDBody/eDBody_Class.htm))
  and populate it with data using[eDScene::CreateBody](../eDScene/eDScene_Class.htm)and eDBody methods.

NOTE:[eDCurveList](../eDCurveList/eDCurveList_Class.htm),[eDShellList](../eDShellList/eDShellList_Class.htm),
and[eDMarkerList](../eDMarkerList/eDMarkerList_Class.htm)are all independent. In this toolkit, you do not bound curves with marker
points or bound faces with curves. Shells may or may not combine to form
recognizable surfaces or solid bodies.

1. [eDBody::CreateCurveList](../eDBody/eDBody_Class.htm)//Create sketch segment
2. [eDBody::CreateShellList](../eDBody/eDBody_Class.htm)

[eDShellList::InsertFacets](../eDShellList/eDShellList_Class.htm)//Input face geometry data

1. [eDBody::CreateMarkerList](../eDBody/eDBody_Class.htm)

[eDMarkerList::InsertMarker](../eDMarkerList/eDMarkerList_Class.htm)//Input point data

1. Add the body to the
  part with[eDPart::AddBody](../eDPart/eDPart_Class.htm).
2. Repeat Steps 3 - 6 to
  add additional configurations.
3. Create the serialization
  object ([eDSerializer](../eDSerializer/eDSerializer_Class.htm))
  using[eDScene::CreateSerializer](../eDScene/eDScene_Class.htm).
4. Save the scene to disk
  using[eDSerializer::Serialize](../eDSerializer/eDSerializer_Class.htm)with[eDSerializerParams](../eDSerializerParams/eDSerializerParams_Class.htm)as a parameter.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="SeeAlso" >
<param name="UseIcon" value="0" >
<param name="Items" value="GettingStarted$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\GettingStarted\Create_a_Part.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
