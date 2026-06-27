---
title: "Simulation::PlayAnimation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__PlayAnimation.htm"
---

# Simulation::PlayAnimation

This
method is:

- obsolete and has not been
  superseded.
- nonfunctional in SolidWorks
  2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks
  2008 to access animation and simulation.

Description

This method plays an animation
of this simulation.

Syntax (OLE Automation)

Retval = Simulation.PlayAnimation ()

(Table)=========================================================

| Output: | (LPANIMATION) Retval | Pointer to Animation object |
| --- | --- | --- |

Syntax (COM)

status = Simulation->PlayAnimation ( &Retval)

Parameters Table Start

(Table)=========================================================

| Output: | (LPANIMATION) Retval | Pointer to Animation object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If an animation is playing
when this method is used, then this method returns the Animation object
for that animation. To check to see if an animation is currently playing,
use Simulation::IsAnimationPlaying.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes006$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Simulation\Simulation__PlayAnimation.htm" >
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
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Simulation\Simulation__PlayAnimation.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
