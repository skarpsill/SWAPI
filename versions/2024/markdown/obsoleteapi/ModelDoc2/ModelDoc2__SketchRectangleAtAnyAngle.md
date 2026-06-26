---
title: "ModelDoc2::SketchRectangleAtAnyAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchRectangleAtAnyAngle.htm"
---

# ModelDoc2::SketchRectangleAtAnyAngle

This method is obsolete and has been superseded
by[SketchManager::Create3PointCornerRectangle](sldworksAPI.chm::/SketchManager/SketchManager__Create3PointCornerRectangle.htm).

Description

This method creates a sketched rectangle at
the specified angle.

Syntax (OLE Automation)

void ModelDoc2.SketchRectangleAtAnyAngle ( x1, y1,
z1, x2, y2, z2, x3, y3, z3, autoConstrain )

(Table)=========================================================

| Input: | (double) x1 | X value of corner 1 |
| --- | --- | --- |
| Input: | (double) y1 | Y value of corner 1 |
| Input: | (double) z1 | Z value of corner 1 |
| Input: | (double) x2 | X value of corner 2 defining the bottom line
from corner 1 |
| Input: | (double) y2 | Y value of corner 2 defining the bottom line
from corner 1 |
| Input: | (double) z2 | Z value of corner 2 defining the bottom line
from corner 1 |
| Input: | (double) x3 | X value of corner 3; diagonal to corner 1 |
| Input: | (double) y3 | Y value of corner 3; diagonal to corner 1 |
| Input: | (double) z3 | Z value of corner 3; diagonal to corner 1 |
| Input: | (BOOL) autoConstrain | TRUE to add automatic constraints to the rectangle
geometry, FALSE to not |

Syntax (COM)

status = ModelDoc2->SketchRectangleAtAnyAngle
( x1, y1, z1, x2, y2, z2, x3, y3, z3, autoConstrain )

(Table)=========================================================

| Input: | (double) x1 | X value of corner 1 |
| --- | --- | --- |
| Input: | (double) y1 | Y value of corner 1 |
| Input: | (double) z1 | Z value of corner 1 |
| Input: | (double) x2 | X value of corner 2 defining the bottom line
from corner 1 |
| Input: | (double) y2 | Y value of corner 2 defining the bottom line
from corner 1 |
| Input: | (double) z2 | Z value of corner 2 defining the bottom line
from corner 1 |
| Input: | (double) x3 | X value of corner 3; diagonal to corner 1 |
| Input: | (double) y3 | Y value of corner 3; diagonal to corner 1 |
| Input: | (double) z3 | Z value of corner 3; diagonal to corner 1 |
| Input: | (BOOL) autoConstrain | TRUE to add automatic constraints to the rectangle
geometry, FALSE to not |
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchRectangleAtAnyAngle.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchRectangleAtAnyAngle.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
