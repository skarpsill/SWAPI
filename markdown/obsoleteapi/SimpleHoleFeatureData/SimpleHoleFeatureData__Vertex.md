---
title: "SimpleHoleFeatureData::Vertex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__Vertex.htm"
---

# SimpleHoleFeatureData::Vertex

This
property is obsolete and has been superseded by SimpleHoleFeatureData2::Vertex .

Description

This property gets or sets the simple hole
feature end condition vertex.

Syntax (OLE Automation)

vertex= SimpleHoleFeatureData.Vertex (VB
Get property)

SimpleHoleFeatureData.Vertex =vertex(VB
Set property)

vertex= SimpleHoleFeatureData.GetVertex ( ) (C++ Get property)

SimpleHoleFeatureData.SetVertex (vertex )(C++ Set property)

(Table)=========================================================

| Property: | (LPDISPATCH) vertex | Pointer to a dispatch object, the end condition vertex or NULL if the operation fails |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_IVertex (
&vertex)

status = WizardHoleFeatureData ->put_IVertex (vertex)

(Table)=========================================================

| Property: | (LPVERTEX) vertex | Pointer to a dispatch object, the end condition
vertex or NULL if the operation fails |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call SimpleHoleFeatureData::AccessSelections before using this property.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SimpleHoleFeatureData\SimpleHoleFeatureData__Vertex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
