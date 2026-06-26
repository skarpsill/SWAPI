---
title: "Animation::Speed"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__Speed.htm"
---

# Animation::Speed

This property
is:

- obsolete and has not been
  superseded.
- nonfunctional in SolidWorks
  2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks
  2008 to access animation and simulation.

Description

This method gets the speed
at which the animation plays.

Syntax (OLE Automation)

VB_GET

Speed = Animation.Speed (VB Get property)

END_VB_GET

VB_SET

Animation.Speed = Speed (VB Set property)

END_VB_SET

Speed = Animation.GetSpeed ( ) (C++ Get property)

END_VC_GET

VC_SET

Animation.SetSpeed ( Speed ) (C++
Set property)

END_VC_SET

(Table)=========================================================

| Output: | (long) Speed | Speed at which the animation
plays as defined by swAnimationPlaySpeed_e |
| --- | --- | --- |

Syntax (COM)

COM_GET

status = Animation->get_Speed (
&Speed )

END_COM_GET

COM_SET

status = Animation->put_Speed
( Speed )

END_COM_SET

Parameters Table Start

(Table)=========================================================

| Output: | (long) Speed | Speed at which the animation
plays as defined by swAnimationPlaySpeed_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property affects
the duration of the animation. It allows you to specify whether or not
to play the animation at half speed or double speed, which halves or doubles
the animation duration.

If you use Animation::Duration
while an animation is playing, then you may not get the same result as
when the animation is not running.

(Table)=========================================================

| If you get the Animation object using... | And then use... | Then the duration... |
| --- | --- | --- |
| Simulation::Animation | Animation::Duration | Is at the normal playing speed |
| Simulation::PlayAnimation | Animation::Duration | May be different a different value because the animation is playing
and the Animation Controller speed
may be set to Normal , Slow
Play , or Fast Play |

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}.

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
<param name="Items" value="ZReleaseNotes006$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Animation\Animation__Speed.htm" >
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
<param name="Items" value="Animation_Object$$**$$ZGetAnimationPlay$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Animation\Animation__Speed.htm" >
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
<param name="Items" value="EXPlayAnimation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Animation\Animation__Speed.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
