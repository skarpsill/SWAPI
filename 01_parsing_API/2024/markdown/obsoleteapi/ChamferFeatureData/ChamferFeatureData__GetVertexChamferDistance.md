---
title: "ChamferFeatureData::GetVertexChamferDistance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__GetVertexChamferDistance.htm"
---

# ChamferFeatureData::GetVertexChamferDistance

This
method is obsolete and has been superseded by[ChamferFeatureData2::GetVertexChamferDistance](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__GetVertexChamferDistance.htm).

Description

This method gets the vertex chamfer distance.

Syntax (OLE Automation)

distance= ChamferFeatureData.GetVertexChamferDistance
(side)

(Table)=========================================================

| Input: | (int) side | Feature direction, set to a value between 0 and
1 |
| --- | --- | --- |
| Return: | (double) distance | Vertex chamfer distance |

Syntax (COM)

status = ChamferFeatureData ->GetVertexChamferDistance
(side, &distance)

(Table)=========================================================

| Input: | (int) side | Feature direction, set to a value between 0 and 1 |
| --- | --- | --- |
| Output: | (double) distance | Vertex chamfer distance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Relevant only for vertex-type chamfers.

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
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ChamferFeatureData\ChamferFeatureData__GetVertexChamferDistance.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
