---
title: "ModelDoc::GetAngularUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetAngularUnits.htm"
---

# ModelDoc::GetAngularUnits

This
method is obsolete and has been superseded by[ModelDoc2::GetAngularUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetAngularUnits.htm).

Description

This method gets the current angular unit settings.

Syntax (OLE Automation)

retval = ModelDoc.GetAngularUnits ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT
of type SafeArray of 5 shorts |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetAngularUnits
( &retval )

(Table)=========================================================

| Output: | (short) retval | Pointer to an array of 5 shorts |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the returned data is an array of fiveshorts:

[AngleUnit,
FractionBase, FractionValue, SignificantDigits, RoundToFraction]

where

AngleUnit= The current angular units. The most up-to-date unit types can
be found in theswAngleUnit_eenumeration

FractionBase=Not Currently Supported. The
return value in this field should not be used.

FractionValue=Not Currently Supported. The return
value in this field should not be used.

SignificantDigits= The significant digits if using
Decimal units.

RoundToFraction=Not
Currently Supported. The return value in this field should not be used.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoUserPreference$$**$$ZGetSetAngularUnits$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetAngularUnits.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
