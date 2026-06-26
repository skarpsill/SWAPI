---
title: "DomeFeatureData::ReverseDir"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__ReverseDir.htm"
---

# DomeFeatureData::ReverseDir

This property is obsolete and has been
superseded by DomeFeatureData2::ReverseDir .

Description

This property controls whether the dome is convex or concave.

Syntax (OLE Automation)

ReverseDir=
DomeFeatureData.ReverseDir (VB Get property)

DomeFeatureData.ReverseDir=
ReverseDir (VB Set property)

ReverseDir=
DomeFeatureData.GetReverseDir ( ) (C++ Get property)

DomeFeatureData.SetReverseDir
( ReverseDir) (C++ Set property)

(Table)=========================================================

| Property: | (BOOL)
ReverseDir | TRUE
if the dome is concave, FALSE if it is convex |
| --- | --- | --- |

Syntax (COM)

status
= DomeFeatureData-> get_ReverseDir( &ReverseDir)

status
= DomeFeatureData-> put_ReverseDir( ReverseDir)

(Table)=========================================================

| Property: | (VARIANT_BOOL)
ReverseDir | TRUE
if the dome is concave, FALSE if it is convex |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

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
<param name="_CURRENTFILEPATH" value="C:\Home\sw2004\obsoleteapi\DomeFeatureData\DomeFeatureData__ReverseDir.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
