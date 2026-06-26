---
title: "Curve::GetLength"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve__GetLength.htm"
---

# Curve::GetLength

This method is obsolete and has been superseded
byCurve::GetLength2.

Description

This
method gets the length of the curve between the specified parameters.

Syntax (OLE Automation)

retval
= Curve.GetLength ( startParam, endParam)

(Table)=========================================================

| Input: | (double)
startParam | Start
parameter |
| --- | --- | --- |
| Input: | (double)
endParam | End
parameter |
| Return: | (double)
retval | Curve
length between the two parameters |

Syntax (COM)

status = Curve->GetLength ( startParam,
endParam, &retval )

(Table)=========================================================

| Input: | (double) startParam | Start parameter |
| --- | --- | --- |
| Input: | (double) endParam | End parameter |
| Output: | (double) retval | Curve length between the two parameters |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use Edge::GetCurve to get the Curve object from the Edge object.

Use[Edge::GetCurveParams](../Edge/Edge__GetCurveParams.htm)to determine the startParam and endParam input for this method.

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
<param name="Items" value="Curve_Object$$**$$ZGetInfoCurve$$**$$Edge::GetCurveParams$$**$$Edge::GetCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Curve\Curve__GetLength.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Edge_Data_By_Name_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Curve\Curve__GetLength.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
