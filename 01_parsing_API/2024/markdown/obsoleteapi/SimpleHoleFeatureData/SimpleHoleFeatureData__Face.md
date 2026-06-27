---
title: "SimpleHoleFeatureData::Face"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__Face.htm"
---

# SimpleHoleFeatureData::Face

This
property is obsolete and has been superseded by SimpleHoleFeatureData2::Face .

Description

This property gets or sets the simple hole
feature end condition face.

Syntax (OLE Automation)

face= SimpleHoleFeatureData.Face (VB
Get property)

SimpleHoleFeatureData.Face =face(VB
Set property)

face= SimpleHoleFeatureData.GetFace ( ) (C++ Get property)

SimpleHoleFeatureData.SetFace (face
)(C++ Set property)

(Table)=========================================================

| Property: | (LPDISPATCH) face | Pointer to a dispatch object, the end condition
face or NULL if the operation fails |
| --- | --- | --- |

Syntax (COM)

status = SimpleHoleFeatureData ->get_IFace ( &face)

status = SimpleHoleFeatureData ->put_IFace (face)

(Table)=========================================================

| Property: | (LPFACE) face | Pointer to a dispatch object, the end condition
face or NULL if the operation fails |
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SimpleHoleFeatureData\SimpleHoleFeatureData__Face.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
