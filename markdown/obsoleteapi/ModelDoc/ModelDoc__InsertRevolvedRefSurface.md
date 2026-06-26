---
title: "ModelDoc::InsertRevolvedRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertRevolvedRefSurface.htm"
---

# ModelDoc::InsertRevolvedRefSurface

This method is obsolete
and has been superseded by[ModelDoc2::InsertRevolvedRefSurface](../ModelDoc2/ModelDoc2__InsertRevolvedRefSurface.htm).

Description

The method creates a revolved reference surface
by revolving a profile around a centerline.

Syntax (OLE Automation)

void ModelDoc.InsertRevolvedRefSurface
( Angle, ReverseDir, Angle2, RevType )

(Table)=========================================================

| Input: | (double) Angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) ReverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) Angle2 | Angle of revolution in radians |
| Input: | (int) RevType | Type of revolution |

Syntax (COM)

status = ModelDoc->InsertRevolvedRefSurface
( Angle, ReverseDir, Angle2, RevType )

(Table)=========================================================

| Input: | (double) Angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ReverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) Angle2 | Angle of revolution in radians |
| Input: | (int) RevType | Type of revolution |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

This method is the same as interactively creating a planar surface by
selecting Insert, Reference Geometry,
Revolved Surface. See SolidWorks Help for more information about
what entities are valid for selection.

Make the selections using ModelDoc::SelectByID before
calling this function.

The RevType argument canbe one of
the following values:

- 0 - One direction revolution.
- 1 - MidPlane revolution. For this type of
  revolve, the angle specification specifies the full revolution. The angle
  to be revolved is (angle/2 ) on either side of the sketch. The ReverseDir
  argument has no affect.
- 2 - Two direction revolution. For a two direction
  revolve, the angle is the angle to be revolved in direction 1 and angle2
  is the angle to be revolved in direction 2.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__InsertRevolvedRefSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
