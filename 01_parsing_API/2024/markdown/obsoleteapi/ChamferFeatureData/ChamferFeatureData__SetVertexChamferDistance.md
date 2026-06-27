---
title: "ChamferFeatureData::SetVertexChamferDistance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ChamferFeatureData/ChamferFeatureData__SetVertexChamferDistance.htm"
---

# ChamferFeatureData::SetVertexChamferDistance

This
method is obsolete and has been superseded by[ChamferFeatureData2::SetVertexChamferDistanc](sldworksAPI.chm::/ChamferFeatureData2/ChamferFeatureData2__SetVertexChamferDistance.htm)e.

Description

This method sets the vertex chamfer distance.

Syntax (OLE Automation)

void ChamferFeatureData.SetVertexChamferDistance
(side, distance)

(Table)=========================================================

| Input: | (int) side | Feature direction, set to a value between 0 and
1 |
| --- | --- | --- |
| Input: | (double) distance | vertex chamfer distance |

Syntax (COM)

status = ChamferFeatureData ->SetVertexChamferDistance
(side,distance)

(Table)=========================================================

| Input: | (int) side | Feature direction, set to a value between 0 and
1 |
| --- | --- | --- |
| Input: | (double) distance | Vertex chamfer distance |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Relevant only for vertex-type chamfers. Currently, only vertex chamfers
with three edges are supported.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ChamferFeatureData\ChamferFeatureData__SetVertexChamferDistance.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
