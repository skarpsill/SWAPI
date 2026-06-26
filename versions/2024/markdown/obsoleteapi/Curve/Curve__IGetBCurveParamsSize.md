---
title: "Curve::IGetBCurveParamsSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__IGetBCurveParamsSize.htm"
---

# Curve::IGetBCurveParamsSize

This method is obsolete and has been superseded
by[Curve::IGetBCurveParamsSize2](Curve__IGetBCurveParamsSize2.htm).

Description

This method gets the B-curve size.

Syntax (OLE Automation)

Not
available.

Syntax (COM)

status
= Curve->IGetBCurveParamsSize ( wantCubicIn, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL)
wantCubicIn | TRUE for cubic curves, FALSE if not |
| --- | --- | --- |
| Output: | (long)
retval | Size
of the data set |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This method is used with Curve::GetBCurveParams.

If wantCubicIn is set to TRUE, then SolidWorks
forces the output from a subsequent call to Curve::IGetBCurveParams to
cubic. This might come out as rational if the underlying curve is a conic
section, such as a circle or an ellipse.

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
<param name="Items" value="Curve_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Curve\Curve__IGetBCurveParamsSize.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
