---
title: "ModelDoc::SetUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUnits.htm"
---

# ModelDoc::SetUnits

This method is obsolete
and has been superseded by[ModelDoc2::SetUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUnits.htm).

Description

This method sets the units used by the user for the model. This setting
does not affect the units used by the SolidWorks API, which consistently
requires and returns meters unless otherwise noted.

Syntax (OLE Automation)

void ModelDoc.SetUnits ( uType, fractBase,
fractDenom, sigDigits, roundToFraction)

(Table)=========================================================

| Input: | (short) uType | The desired model units as defined in swLengthUnit_e |
| --- | --- | --- |
| Input: | (short) fractBase | Decimal vs. fraction as defined in swFractionDisplay_e |
| Input: | (short) fractDenom | Used only for fractional inches and is the denominator for the smallest
fraction to be used; for example, 64 for 1/64 |
| Input: | (short) sigDigits | Significant digits if using decimal units |
| Input: | (BOOL) roundToFraction | Flag denoting whether or not to round to the fraction; for example,
if 4 was the denominator value given in fractDenom and the actual value
is 0.27, it would be rounded to 0.25 |

Syntax (COM)

status = ModelDoc->SetUnits ( uType,
fractBase, fractDenom, sigDigits, roundToFraction)

(Table)=========================================================

| Input: | (short) uType | The desired model units as defined in swLengthUnit_e |
| --- | --- | --- |
| Input: | (short) fractBase | Decimal vs. fraction as defined in swFractionDisplay_e |
| Input: | (short) fractDenom | Used only for fractional inches and is the denominator for the smallest
fraction to be used; for example, 64 for 1/64 |
| Input: | (short) sigDigits | Significant digits if using decimal units |
| Input: | (VARIANT_BOOL) roundToFraction | Fag denoting whether or not to round to the fraction; for example, if
4 was the denominator value given in fractDenom and the actual value is
0.27, it would be rounded to 0.25 |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Fractional units are only valid if uType is swINCHES or swFEETINCHES.

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
<param name="Items" value="ModelDoc_Object$$**$$ZSetInfoUserPreference$$**$$ZSetGetUnits$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetUnits.htm" >
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
<param name="Items" value="Get_and_Set_Units_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetUnits.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
