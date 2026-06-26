---
title: "Edge::GetCurveParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Edge/Edge__GetCurveParams.htm"
---

# Edge::GetCurveParams

This
method is obsolete and has been superseded by[Edge::GetCurveParams2](sldworksAPI.chm::/Edge/Edge__GetCurveParams2.htm).

Description

This function returns the parameterization of the edge.

Syntax (OLE Automation)

retval
= Edge.GetCurveParams ()

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
of type SafeArray describing the parameterization of the edge |
| --- | --- | --- |

Syntax (COM)

status
= Edge->IGetCurveParams ( &retval )

(Table)=========================================================

| Output: | (double*)
retval | Pointer
to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

You must precede calls to this by a call toEdge::GetCurvebecause SolidWorks does not keep the underlying curve
information. Edge::GetCurve generates this information and you can extract
the curve parameters.

You can use the data returned by this method to determine if a circular
edge is a complete circle or an arc.

The return value is the following array of 10 doubles:

[StartPtX, StartPtY, StartPtZ, EndPtX,
EndPtY, EndPtZ, StartUParam, EndUParam, PackDouble1, PackDouble2]

wherePackDouble1andPackDouble2are each a set
of two integers packed into a double. They hold the following pair of
integers:

(Table)=========================================================

| PackDouble1 | Two packed integers: Unused curveType as documented
in Curve::Identity |
| --- | --- |
| PackDouble2 | Two packed integers: Unused curveTag |

If the curve is closed and it starts and ends at the same point, thenStartUParamandEndUParamare a period apart.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Edge_Object$$**$$ZGetInfoCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Edge\Edge__GetCurveParams.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Edge\Edge__GetCurveParams.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
