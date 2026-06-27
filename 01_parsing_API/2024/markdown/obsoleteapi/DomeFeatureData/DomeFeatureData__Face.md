---
title: "DomeFeatureData::Face"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__Face.htm"
---

# DomeFeatureData::Face

This method is obsolete and has been superseded by[DomeFeatureData2::Face](../DomeFeatureData2/DomeFeatureData2__Face.htm).

Description

This property gets or sets the planar face associated with the dome.

Syntax (OLE Automation)

Set Face = DomeFeatureData.Face (VB
Get property)

Set DomeFeatureData.Face= Face (VB
Set property)

Face = DomeFeatureData.GetFace ( ) (C++
Get property)

DomeFeatureData.SetFace ( Face) (C++
Set property)

(Table)=========================================================

| Property: | (LPDISPATCH) Face | Dispatch pointer for the face associated with the dome |
| --- | --- | --- |

Syntax (COM)

status = DomeFeatureData-> get_Face(
&Face)

status = DomeFeatureData-> put_Face(
Face)

(Table)=========================================================

| Property: | (LPFACE) Face | Pointer to the face associated with the dome |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property does not affect geometry until you call Feature::ModifyDefinition.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DomeFeatureData\DomeFeatureData__Face.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
