---
title: "ModelDoc::SketchChamfer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchChamfer.htm"
---

# ModelDoc::SketchChamfer

This
method is obsolete and has been superseded by[ModelDoc2::SketchChamfer](../ModelDoc2/ModelDoc2__SketchChamfer.htm).

Description

This method creates a chamfer between two selected
sketch entities.

Syntax (OLE Automation)

void ModelDoc.SketchChamfer ( angleORdist, dist1,
options)

(Table)=========================================================

| Input: | (double) angleORdist | Angle of the chamfer if using the angle-distance
option or the distance of the second distance if using the distance-distance
option |
| --- | --- | --- |
| Input: | (double) dist1 | Distance of the chamfer |
| Input: | (long) options | 0
= angle–distance chamfer 1
= distance–distance chamfer |

Syntax (COM)

status = ModelDoc->SketchChamfer ( angleORdist,
dist1, options )

(Table)=========================================================

| Input: | (double) angleORdist | Angle of the chamfer if using the angle-distance
option or the distance of the second distance if using the distance-distance
option |
| --- | --- | --- |
| Input: | (double) dist1 | Distance of the chamfer |
| Input: | (long) options | 0
= angle–distance chamfer 1
= distance–distance chamfer |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SketchChamfer.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SketchChamfer.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
