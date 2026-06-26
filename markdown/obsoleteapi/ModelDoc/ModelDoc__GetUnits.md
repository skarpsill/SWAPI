---
title: "ModelDoc::GetUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUnits.htm"
---

# ModelDoc::GetUnits

This
method is obsolete and has been superseded by[ModelDoc2::GetUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUnits.htm).

Description

This method gets the current unit settings, along with the fraction
base, the fraction value, and the significant digits being used. You can
also use ModelDoc::LengthUnit, which provides access to the LengthUnit
parameter.

Syntax (OLE Automation)

retval = ModelDoc.GetUnits ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 5 shorts |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetUnits ( &retval
)

(Table)=========================================================

| Output: | (short) retval | Pointer to an array of 5 shorts |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the returned data is an array of shorts:

[LengthUnit,
FractionBase, FractionValue, SignificantDigits, RoundToFraction]

where:

LengthUnit= the current
model units as defined in swLengthUnit_e.

FractionBase= decimal vs. fraction. This return is one oftheswFractionDisplay_eenumerations.Fractional
units are only valid if the user has specified swINCHES or swFEETINCHES.

FractionValue= the denominator value if using fractional units.

SignificantDigits= the significant digits if using
decimal units.

RoundToFraction= a flag denoting whether or not
to round the fraction.For example, if 4 was the
denominator value and the actual value was .27, then it would be rounded
to .25.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoUserPreference$$**$$ZSetGetUnits$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUnits.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Current_Unit_Settings_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUnits.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
