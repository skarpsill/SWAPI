---
title: "Simulation::Duration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__Duration.htm"
---

# Simulation::Duration

This
property is:

- obsolete and has not been
  superseded.
- nonfunctional in SolidWorks
  2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks
  2008 to access animation and simulation.

Description

This property gets the
elapsed time of the Physical Simulation.

Syntax (OLE Automation)

VB_GET

Retval = Simulation.Duration (VB Get
property)

END_VB_GET

VB_SET--<P class="apiSyntaxOLE">Simulation.[OLEMemberName][VB_ArgList] = [SetVal] (VB
Set property)</P> --END_VB_SET

Retval = Simulation.GetDuration ( ) (C++ Get property)

END_VC_GET

VC_SET--<P class="apiSyntaxOLE">Simulation.Set[OLEMemberName] [C_ArgList]
(C++ Set property)</P> --END_VC_SET

(Table)=========================================================

| Output: | (double) Retval | Elapsed time in seconds |
| --- | --- | --- |

Syntax (COM)

COM_GET

status = Simulation->get_Duration
( &Retval )

END_COM_GET

COM_SET--<P class="apiSyntaxOLE">status =
Simulation->put_[COMMemberName] ( [Args] )</P> --END_COM_SET

Parameters Table Start

(Table)=========================================================

| Output: | (double) Retval | Elapsed time in seconds |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the Physical Simulation
has not yet been calculated, then Retval is 0.0.

The return value represents
the length of time that the simulation is expected to last. This means
that if a bouncing ball takes 15 seconds to come to a stop, then this
property returns a value of 15.

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
<param name="Items" value="ZReleaseNotes005plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\sldworksapi\Simulation\Simulation__Duration.htm" >
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
<param name="Items" value="Simulation_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\sldworksapi\Simulation\Simulation__Duration.htm" >
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
<param name="Items" value="EXGetPhysicalSimulationData$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\sldworksapi\Simulation\Simulation__Duration.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
