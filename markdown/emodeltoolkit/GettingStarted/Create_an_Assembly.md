---
title: "Create an Assembly"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/GettingStarted/Create_an_Assembly.htm"
---

# Create an Assembly

See Also

You will typically follow these steps to create an assembly using the
eModelToolkit.

1. Create an application using[eDApplication::Create](../eDApplication/eDApplication_Class.htm).
2. Create a scene ([eDScene](../eDScene/eDScene_Class.htm))
  using[eDApplication::CreateScene](../eDApplication/eDApplication_Class.htm).
3. Create and add a new configuration ([eDConfiguration](../eDConfiguration/eDConfiguration_Class.htm))
  to that scene using[eDScene::CreateConfiguration](../eDScene/eDScene_Class.htm).
4. Create and add a new assembly ([eDAssembly](../eDAssembly/eDAssembly_Class.htm))
  to that configuration using[eDConfiguration::CreateAssembly](../eDConfiguration/eDConfiguration_Class.htm).
  This is the top-level root component.
5. To create a new component with no children:
6. To create a subassembly, create a new assembly
  ([eDAssembly](../eDAssembly/eDAssembly_Class.htm)) using[eDAssembly::CreateSubAssembly](../eDAssembly/eDAssembly_Class.htm).
  The parent-child link is created for you.

Add parts or more subassemblies to that assembly
using[eDAssembly::CreatePart](../eDAssembly/eDAssembly_Class.htm)and[eDAssembly::CreateAssembly](../eDAssembly/eDAssembly_Class.htm),
respectively.

1. Repeat Steps 5 and 6
  to create additional components.
2. Repeat Steps 3 - 6 to
  create additional configurations.
3. Create the serialization
  object ([eDSerializer](../eDSerializer/eDSerializer_Class.htm))
  from[eDScene::CreateSerializer](../eDScene/eDScene_Class.htm).
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\GettingStarted\Create_an_Assembly.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
