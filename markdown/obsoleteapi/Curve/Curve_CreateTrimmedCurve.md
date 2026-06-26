---
title: "Curve::CreateTrimmedCurve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Curve/Curve_CreateTrimmedCurve.htm"
---

# Curve::CreateTrimmedCurve

This method is obsolete and has been superseded
by[Curve::CreateTrimmedCurve2](sldworksAPI.chm::/Curve/Curve__CreateTrimmedCurve2.htm).

Description

This method creates a trimmed curve using the
specified 3D points.

Syntax (OLE Automation)

retval = Curve.CreateTrimmedCurve( x1, y1, z1, x2, y2, z2)

(Table)=========================================================

| Input: | (double) x1 | X start point |
| --- | --- | --- |
| Input: | (double) y1 | Y start point |
| Input: | (double) z1 | Z start point |
| Input: | (double) x2 | X end point |
| Input: | (double) y2 | Y end point |
| Input: | (double) z2 | Z end point |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created
curve or NULL if the operation fails |

Syntax (COM)

status = Curve->ICreateTrimmedCurve ( startPt,
endPt, &retval )

(Table)=========================================================

| Input: | (double*) startPt | Pointer to an array of 3 doubles, the x, y, z
startpoint |
| --- | --- | --- |
| Input: | (double*) endPt | Pointer to an array of 3 doubles, the x, y, z
endpoint |
| Output: | (LPCURVE) retval | Pointer to the newly created curve or NULL if
the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use the resulting curve for surface
trimming operations (for example,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Surface::CreateTrimmedSheet).

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
<param name="Items" value="Curve_Object$$**$$ZCreateCurve$$**$$ZModelerSewingRoutines$$**$$Curve::IsTrimmedCurve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Curve\Curve_CreateTrimmedCurve.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
