---
title: "ModelDoc2::CreateCenterLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateCenterLine.htm"
---

# ModelDoc2::CreateCenterLine

This method is obsolete and has been superseded
by[SketchManager::CreateCenterLine](sldworksAPI.chm::/SketchManager/SketchManager__CreateCenterLine.htm).

Description

This method creates a center line from P1 to P2.

NOTE:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Use
ModelDoc2::CreateCenterLineVB for Visual Basic and other forms of Basic
that do not support SafeArrays.

Syntax (OLE Automation)

retval = ModelDoc2.CreateCenterLine
( P1, P2)

(Table)=========================================================

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters that describe
the first point of the line |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters that describe
the second point of the line |
| Return: | (VARIANT_BOOL) retval | TRUE if success, FALSE if failure |

Syntax (COM)

status = ModelDoc2->ICreateCenterLine
( P1, P2 )

(Table)=========================================================

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x,y,z) in meters that describe the
line start point |
| --- | --- | --- |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x,y,z) in meters that describe the
line start point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also create centerline construction geometry
using ModelDoc2::CreateLine2 and SketchSegment::ConstructionGeometry.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateCenterLine.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateCenterLine.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
