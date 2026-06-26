---
title: "ModelDoc2::CreateTangentArc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateTangentArc2.htm"
---

# ModelDoc2::CreateTangentArc2

This method is obsolete and has been superseded
by[SketchManager::CreateTangentArc.](sldworksAPI.chm::/SketchManager/SketchManager__CreateTangentArc.htm)

Description

This method creates a tangent arc.

Syntax (OLE Automation)

retval = ModelDoc2.CreateTangentArc2 ( p1x, p1y,
p1z, p2x, p2y, p2z, arcTypeIn )

(Table)=========================================================

| Input: | (double) p1x | x coordinate of start point in meters |
| --- | --- | --- |
| Input: | (double) p1y | y coordinate of start point in meters |
| Input: | (double) p1z | z coordinate of start point in meters |
| Input: | (double) p2x | x coordinate of end point in meters |
| Input: | (double) p2y | y coordinate of end point in meters |
| Input: | (double) p2z | z coordinate of end point in meters |
| Input: | (long) arcTypeIn | Type of tangent arc as defined in swTangentArcTypes_e |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc2->CreateTangentArc2 ( p1x, p1y,
p1z, p2x, p2y, p2z, arcTypeIn, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (double) p1x | x coordinate of start point in meters |
| --- | --- | --- |
| Input: | (double) p1y | y coordinate of start point in meters |
| Input: | (double) p1z | z coordinate of start point in meters |
| Input: | (double) p2x | x coordinate of end point in meters |
| Input: | (double) p2y | y coordinate of end point in meters |
| Input: | (double) p2z | z coordinate of end point in meters |
| Input: | (long) arcTypeIn | Type of tangent arc as defined in swTangentArcTypes_e |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateTangentArc2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateTangentArc2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
