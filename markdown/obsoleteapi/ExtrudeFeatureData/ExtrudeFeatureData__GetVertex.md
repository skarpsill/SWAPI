---
title: "ExtrudeFeatureData::GetVertex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetVertex.htm"
---

# ExtrudeFeatureData::GetVertex

This
method is obsolete and has been superseded by ExtrudeFeatureData2::GetVertex .

Description

This method gets the extrusion feature end
condition vertex in forward or reverse direction.

Syntax (OLE Automation)

vertex = ExtrudeFeatureData.GetVertex (forward)

(Table)=========================================================

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for
reverse |
| --- | --- | --- |
| Return: | (LPDISPATCH) vertex | Dispatch pointer to the end condition vertex
(or NULL if the operation fails) |

Syntax (COM)

status = ExtrudeFeatureData->IGetVertex ( forward,
&vertex )

(Table)=========================================================

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for
reverse |
| --- | --- | --- |
| Output: | (LPVERTEX) vertex | pointer to the end condition vertex (or NULL
if the operation fails) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use[ExtrudeFeatureData::AccessSelections](ExtrudeFeatureData__AccessSelections.htm)before calling this method.

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
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ExtrudeFeatureData\ExtrudeFeatureData__GetVertex.htm" >
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
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ExtrudeFeatureData\ExtrudeFeatureData__GetVertex.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
