---
title: "DrawingDoc::CreateLinearDim"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateLinearDim.htm"
---

# DrawingDoc::CreateLinearDim

This method is obsolete and has been superseded
byDrawingDoc::CreateLinearDim2.

Description

This
method creates a non-associative linear dimension.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateLinearDim ( p0, p1, p2, p3, p4, angle, arrowSize, text,
textHeight, witnessGap, witnessOvershoot)

(Table)=========================================================

| Input: | (VARIANT)
p0 | VARIANT
of type SafeArray of 3 doubles (x,y,z), dimension point |
| --- | --- | --- |
| Input: | (VARIANT)
p1 | VARIANT
of type SafeArray of 3 doubles (x,y,z), dimension end |
| Input: | (VARIANT)
p2 | VARIANT
of type SafeArray of 3 doubles (x,y,z), normal to the plane of sketch |
| Input: | (VARIANT)
p3 | VARIANT
of type SafeArray of 3 doubles (x,y,z), extension line 1 reference point |
| Input: | (VARIANT)
p4 | VARIANT
of type SafeArray of 3 doubles (x,y,z), extension line 2 reference point |
| Input: | (double)
angle | Inclination
angle of the text in radians |
| Input: | (double)
arrowSize | Arrow
size meters |
| Input: | (BSTR)
text | Dimension
text string |
| Input: | (double)
textHeight | Text
height in meters |
| Input: | (double)
witnessGap | Extension
line gap in meters |
| Input: | (double)
witnessOvershoot | Extension
line overshoot in meters |
| Return: | (BOOL)
retval | TRUE
for success, FALSE for failure |

Syntax (COM)

status
= DrawingDoc->ICreateLinearDim ( P0, P1, P2, P3, P4, Angle, ArrowSize,
Text, TextHeight, WitnessGap, WitnessOvershoot )

(Table)=========================================================

| Input: | (double*)
P0 | Pointer
to an array of 3 doubles (x,y,z), dimension point |
| --- | --- | --- |
| Input: | (double*)
P1 | Pointer
to an array of 3 doubles (x,y,z), dimension end |
| Input: | (double*)
P2 | Pointer
to an array of 3 doubles (x,y,z), normal to the plane of sketch |
| Input: | (double*)
P3 | Pointer
to an array of 3 doubles (x,y,z), extension line 1 reference point |
| Input: | (double*)
P4 | Pointer
to an array of 3 doubles (x,y,z), extension line 2 reference point |
| Input: | (double)
Angle | Inclination
angle of the text in radians |
| Input: | (double)
ArrowSize | Arrow
size meters |
| Input: | (BSTR)
Text | Dimension
text string |
| Input: | (double)
TextHeight | Text
height in meters |
| Input: | (double)
WitnessGap | Extension
gap in meters |
| Input: | (double)
WitnessOvershoot | Extension
overshoot in meters |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

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
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateNonAssociativeDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__CreateLinearDim.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
