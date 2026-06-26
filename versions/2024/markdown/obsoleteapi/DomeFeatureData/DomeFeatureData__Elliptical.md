---
title: "DomeFeatureData::Elliptical"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__Elliptical.htm"
---

# DomeFeatureData::Elliptical

This property is obsolete and has been
superseded by DomeFeatureData2::Elliptical .

Description

If the face on which the dome is defined is a circular or elliptical
face, then this flag controls whether the dome is a half ellipsoid, with
a height equal to one of the ellipsoid radii.

Syntax (OLE Automation)

Elliptical=
DomeFeatureData.Elliptical (VB Get property)

DomeFeatureData.Elliptical=
Elliptical (VB Set property)

Elliptical=
DomeFeatureData.GetElliptical ( ) (C++ Get property)

DomeFeatureData.SetElliptical
( Elliptical) (C++ Set property)

(Table)=========================================================

| Property: | (BOOL)
Elliptical | TRUE
if the dome is elliptical, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status
= DomeFeatureData-> get_Elliptical( &Elliptical)

status
= DomeFeatureData-> put_Elliptical( Elliptical)

(Table)=========================================================

| Property: | (VARIANT_BOOL)
Elliptical | TRUE
if the dome is elliptical, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\DomeFeatureData\DomeFeatureData__Elliptical.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
