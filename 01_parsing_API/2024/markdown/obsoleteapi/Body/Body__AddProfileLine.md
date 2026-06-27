---
title: "Body::AddProfileLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__AddProfileLine.htm"
---

# Body::AddProfileLine

This method is obsolete and has been superseded by[Body2::AddProfileLine](sldworksAPI.chm::/Body2/Body2__AddProfileLine.htm).

Description

This method creates a line profile curve and returns a pointer to that
curve.

Syntax (OLE Automation)

retval
= Body.AddProfileLine ( rootPoint, direction)

(Table)=========================================================

| Input: | (VARIANT)
rootPoint | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT)
direction | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH)
retval | Pointer
to dispatch object, the line profile curve |

Syntax (COM)

status = Body->IAddProfileLineDLL
( rootPoint, direction, &retval )

(Table)=========================================================

| Input: | (double*) rootPoint | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) direction | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPCURVE) retval | Pointer to the line profile curve. |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method with Body::CreateRevolutionSurface to generate
a cylindrical surface of revolution or with Body::CreateExtrusionSurface
to generate a tabulated cylinder.

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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__AddProfileLine.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
