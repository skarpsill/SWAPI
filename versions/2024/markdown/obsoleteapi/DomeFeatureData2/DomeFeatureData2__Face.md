---
title: "DomeFeatureData2::Face"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData2/DomeFeatureData2__Face.htm"
---

# DomeFeatureData2::Face

This property is obsolete and has been superseded
by[DomeFeatureData2::Faces](sldworksAPI.chm::/DomeFeatureData2/DomeFeatureData2__Faces.htm),[DomeFeatureData2::IGetFaces](sldworksAPI.chm::/DomeFeatureData2/DomeFeatureData2__IGetFaces.htm),
and[DomeFeatureData2::ISetFaces](sldworksAPI.chm::/DomeFeatureData2/DomeFeatureData2__ISetFaces.htm).

Description

This
property gets or sets the planar face associated with this dome feature.

Syntax (OLE Automation)

Set
Face= DomeFeatureData2.Face (VB Get property)

Set
DomeFeatureData2.Face= Face (VB Set property)

Face=
DomeFeatureData2.GetFace ( ) (C++ Get property)

DomeFeatureData2.SetFace
( Face) (C++ Set property)

(Table)=========================================================

| Property: | (LPDISPATCH)
Face | Dispatch
pointer for the face associated with the dome |
| --- | --- | --- |

Syntax (COM)

status
= DomeFeatureData2-> get_IFace( &face)

status
= DomeFeatureData2-> put_IFace( face)

(Table)=========================================================

| Property: | (LPFACE2)
face | Pointer
to the face associated with the dome |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This property does not affect geometry until you call Feature::ModifyDefinition.

See Accessing Selections that Define Features
for additional details on using this property.Metadata type="DesignerControl" startspan
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
<param name="Items" value="DomeFeatureData2_Object$$**$$Face2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DomeFeatureData2\DomeFeatureData2__Face.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXChangeHeightDome$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DomeFeatureData2\DomeFeatureData2__Face.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
