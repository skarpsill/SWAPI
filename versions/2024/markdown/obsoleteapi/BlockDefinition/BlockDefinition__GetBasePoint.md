---
title: "BlockDefinition::GetBasePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockDefinition/BlockDefinition__GetBasePoint.htm"
---

# BlockDefinition::GetBasePoint

This method is obsolete and has been superseded
by[SketchBlockDefinition::InsertionPoint](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__InsertionPoint.htm).

Description

This method gets the base
point of this block definition.

Syntax (OLE Automation)

retval = BlockDefinition.GetBasePoint ()

(Table)=========================================================

| Output: | (VARIANT) retval | VARIANT of type SafeArray identifying
the x,y,z values of the base point |
| --- | --- | --- |

Syntax (COM)

status = BlockDefinition->IGetBasePoint ( retval)

Parameters Table Start

(Table)=========================================================

| Output: | (double) retval | Array of doubles identifying
the x,y,z values of the base point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The base point of a block definition is the point
around which instances of the block rotate or scale. It is the origin
of the sketch containing the geometry that is part of the block definition.
This implies that the base point of a block definition is always (0,0,0),
because the sketch origin is (0,0). Therefore, BlockDefinition::GetBasePoint
always returns (0,0,0).

The BlockDefinition::SetBasePoint values are specified
relative to the current base point. However, when the base point is changed,
it must become the sketch origin again, that is, it must become the (0,0,0)
point again. So, if you use the this method and then immediately use BlockDefintion::GetBasePoint,
it returns (0,0,0).

Changing the base point does not affect how instances
of the block look in a drawing, so when the base point changes, the sketch
geometry in the definition is adjusted to allow for that behavior. This
means that if you get the block definition sketch and sketch geometry,
the sketch geometry coordinates will be different after the base point
is changed.

If you use Annotation::GetPosition and Annotation::SetPosition
on instances of the block, you will notice that the instance position
is also affected by a change in the block definition base point, even
though the instance does not appear different on the drawing. The instance
position is where the base point of the definition is in the instance,
so if the base point of the definition changes, the instance position
value will be different.

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
<param name="Items" value="ZReleaseNotes005$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\BlockDefinition\BlockDefinition__GetBasePoint.htm" >
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
<param name="Items" value="BlockDefinition_Object$$**$$BlockDefinitionBasePoint$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\BlockDefinition\BlockDefinition__GetBasePoint.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
