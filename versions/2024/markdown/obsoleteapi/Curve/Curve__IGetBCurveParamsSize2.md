---
title: "Curve::IGetBCurveParamsSize2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__IGetBCurveParamsSize2.htm"
---

# Curve::IGetBCurveParamsSize2

This method is obsolete and has been superseded
by[Curve::IGetBCurveParamsSize3](sldworksAPI.chm::/Curve/Curve__IGetBCurveParamsSize3.htm).

Description

This
method gets the b-curve size.

Syntax (OLE Automation)

Not available.

Syntax
(COM)

status = Curve->IGetBCurveParamsSize2
( wantCubicIn, wantNRational, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) wantCubicIn | TRUE for cubic curves, FALSE if not |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) wantNRational | TRUE for non-rational curves, FALSE if not |
| Output: | (long) retval | Size of the data set returned by Curve::IGetBCurveParams. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method to control the type of information returned in the subsequent
call to Curve::IGetBCurveParams.

To control the accuracy of the curve data, see Modeler::SetToleranceValue.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Curve_Object$$**$$ZGetInfoCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Curve\Curve__IGetBCurveParamsSize2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
