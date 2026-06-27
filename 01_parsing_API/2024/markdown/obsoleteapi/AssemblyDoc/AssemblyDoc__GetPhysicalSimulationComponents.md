---
title: "AssemblyDoc::GetPhysicalSimulationComponents"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__GetPhysicalSimulationComponents.htm"
---

# AssemblyDoc::GetPhysicalSimulationComponents

This method
is:

- obsolete and has not been
  superseded.
- nonfunctional in SolidWorks
  2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks
  2008 to access animation and simulation.

Description

This method gets the Physical
Simulation's components and transforms.

Syntax (OLE Automation)

void = AssemblyDoc.GetPhysicalSimulationComponents
( inDuration, outCount, outComponents, outTransforms, outStepStartTimes,
outStepDurations, outTotalPhysSimDuration)

(Table)=========================================================

| Input: | (long) inDuration | Total elapsed time for Physical
Simulation |
| --- | --- | --- |
| Output: | (long*) outCount | Size for all returned arrays |
| Output: | (VARIANT*) outComponents | VARIANT of type SafeArray of the Component2 objects |
| Output: | (VARIANT*) outTransforms | VARIANT of type SafeArray of
the MathTransform objects |
| Output: | (VARIANT*) outStepStartTimes | Array of doubles of size outCount;
when each step in the Physical Simulation should happen |
| Output: | (VARIANT*) outStepDurations | Array of doubles of size outCount; how long each
step in the Physical Simulation should take |
| Output: | (double*) outTotalPhysSimDuration | Total elapsed time Physical Simulation should
have taken |

Syntax (COM)

status = AssemblyDoc->GetPhysicalSimulationComponents
( inDuration, outCount, outComponents, outTransforms, outStepStartTimes,
outStepDurations, outTotalPhysSimDuration)

Parameters Table Start

(Table)=========================================================

| Input: | (long) inDuration | Total elapsed time for Physical Simulation |
| --- | --- | --- |
| Output: | (long*) outCount | Size for all returned arrays |
| Output: | (VARIANT*) outComponents | VARIANT of type SafeArray of the Component2 objects |
| Output: | (VARIANT*) outTransforms | VARIANT of type SafeArray of the MathTransform
objects |
| Output: | (VARIANT*) outStepStartTimes | Array of doubles
of size outCount; when each step in the Physical Simulation should happen |
| Output: | (VARIANT*) outStepDurations | Array of doubles of size outCount; when each
step in the Physical Simulation should happen |
| Output: | (double*) outTotalPhysSimDuration | Total elapsed time Physical Simulation
should have taken |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\AssemblyDoc\AssemblyDoc__GetPhysicalSimulationComponents.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$PhysicalSimulation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\AssemblyDoc\AssemblyDoc__GetPhysicalSimulationComponents.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXGetPhysicalSimulation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\AssemblyDoc\AssemblyDoc__GetPhysicalSimulationComponents.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
