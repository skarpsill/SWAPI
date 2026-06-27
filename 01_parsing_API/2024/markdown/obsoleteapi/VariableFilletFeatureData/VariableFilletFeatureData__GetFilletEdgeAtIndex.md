---
title: "VariableFilletFeatureData::GetFilletEdgeAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__GetFilletEdgeAtIndex.htm"
---

# VariableFilletFeatureData::GetFilletEdgeAtIndex

This
method is obsolete and has been superseded by VariableFilletFeatureData2::GetFilletEdgeAtIndex .

Description

This method gets the filleted edge at the specified
index.

Syntax (OLE Automation)

pFilletEdge = VariableFilletFeatureData.GetFilletEdgeAtIndex
(index)

(Table)=========================================================

| Input: | (int) index | Index at which filleted edge is required |
| --- | --- | --- |
| Return: | (LPDISPATCH) pFilletEdge | Pointer to a dispatch object, the filleted edge
or NULL if the operation fails |

Syntax (COM)

status = VariableFilletFeatureData ->IGetFilletEdgeAtIndex
( index, &pFilletEdge )

(Table)=========================================================

| Input: | (int) index | Index at which filleted edge is required |
| --- | --- | --- |
| Output: | (LPEDGE) pFilletEdge | Pointer the filleted edge or NULL if the operation
fails |
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
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\VariableFilletFeatureData\VariableFilletFeatureData__GetFilletEdgeAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
