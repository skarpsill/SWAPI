---
title: "ModelDoc2::CreatePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePoint.htm"
---

# ModelDoc2::CreatePoint

This
method is obsolete and has been superseded by[ModelDoc2::CreatePoint2](ModelDoc2__CreatePoint2.htm).

Description

This method creates a point entity at the specified (x, y, z) location
in the current sketch.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePoint ( pointX,
pointY, pointZ)

(Table)=========================================================

| Input: | (double) pointX | x value of point in meters |
| --- | --- | --- |
| Input: | (double) pointY | y value of point in meters |
| Input: | (double) pointZ | z value of point in meters; this value is not recognized; points created
in a sketch must be in the particular sketch plane; you should pass in
a value of 0.0 for this argument |
| Return: | (BOOL) retval | TRUE if created, FALSE if not |

Syntax (COM)

status = ModelDoc2->CreatePoint
( pointX, pointY, pointZ, &retval )

(Table)=========================================================

| Input: | (double) pointX | x value of point in meters |
| --- | --- | --- |
| Input: | (double) pointY | y value of point in meters |
| Input: | (double) pointZ | z value of point in meters; this value is not recognized; points created
in a sketch must be in the particular sketch plane; you should pass in
a value of 0.0 for this argument |
| Output: | (VARIANT_BOOL) retval | TRUE if created, FALSE if not |
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreatePoint.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreatePoint.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
