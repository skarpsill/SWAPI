---
title: "ModelDoc2::SplitOpenSegment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SplitOpenSegment.htm"
---

# ModelDoc2::SplitOpenSegment

This
method is obsolete and has been superseded to[SketchManager::SplitOpenSegment.](sldworksAPI.chm::/SketchManager/SketchManager__SplitOpenSegment.htm)

Description

This method splits the selected sketch segment
into two sketch segments.

Syntax (OLE Automation)

retval = ModelDoc2.SplitOpenSegment ( x1, y1, z1
)

(Table)=========================================================

| Input: | (double)x | X value of the point that splits the sketch segment
in two |
| --- | --- | --- |
| Input: | (double)y | Y value of the point that splits the sketch segment
in two |
| Input: | (double)z | Z value of the point that splits the sketch segment
in two |

Syntax (COM)

status = ModelDoc2->SplitOpenSegment ( x1, y1,
z1 )

(Table)=========================================================

| Input: | (double) x | X value of the point that splits the sketch segment
in two |
| --- | --- | --- |
| Input: | (double) y | Y value of the point that splits the sketch segment
in two |
| Input: | (double) z | Z value of the point that splits the sketch segment
in two |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selected sketch segment must be an open
entity; for example, the start and end points cannot be the same.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SplitOpenSegment.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SplitOpenSegment.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
