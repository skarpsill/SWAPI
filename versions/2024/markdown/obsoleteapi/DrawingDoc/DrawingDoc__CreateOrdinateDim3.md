---
title: "DrawingDoc::CreateOrdinateDim3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateOrdinateDim3.htm"
---

# DrawingDoc::CreateOrdinateDim3

This method is obsolete and has been superseded
by[DrawingDoc::CreateOrdinateDim4](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateOrdinateDim4.htm).

Description

This method creates a non-associative ordinate dimension.

Syntax (OLE Automation)

retval = DrawingDoc.CreateOrdinateDim3
( p0, p1, p2, p3, p4, angle, arrowSize, text, textHeight, witnessGap,
witnessOvershoot, p5 )

(Table)=========================================================

| Input: | (VARIANT) p0 | VARIANT of type SafeArray of 3 doubles (x,y,z), the dimension point. |
| --- | --- | --- |
| Input: | (VARIANT) p1 | VARIANT of type SafeArray of 3 doubles (x,y,z); this variable is a unit
vector and specifies the direction of the ordinate dimension |
| Input: | (VARIANT) p2 | VARIANT of type SafeArray of 3 doubles (x,y,z), the extension line start
point. |
| Input: | (VARIANT) p3 | VARIANT of type SafeArray of 3 doubles (x,y,z), the extension line end
point |
| Input: | (VARIANT) p4 | VARIANT of type SafeArray of 3 doubles (x,y,z); this variable is a unit
vector and specifies the orientation of the text; for example, values
(1, 0, 0) would result in horizontal text that is read from left to right |
| Input: | (double) angle | Inclination angle of the text in radians (character slant) |
| Input: | (double) arrowSize | Arrow size meters |
| Input: | (BSTR) text | Dimension text string |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) witnessGap | Extension gap in meters |
| Input: | (double) witnessOvershoot | Extension overshoot in meters |
| Input: | (VARIANT) p5 | Pointer to an array of 3 doubles
(x,y,z), position of text |
| Return: | (LPDISPATCH)retval | Dispatch pointer to DisplayDimension object |

Syntax (COM)

status = DrawingDoc->ICreateOrdinateDim3
( p0, p1, p2, p3, p4, angle, arrowSize, text, textHeight, witnessGap,
witnessOvershoot, p5, &retval )

(Table)=========================================================

| Input: | (double*) p0 | Pointer to an array of 3 doubles (x,y,z), the dimension point. |
| --- | --- | --- |
| Input: | (double*) p1 | Pointer to an array of 3 doubles (x,y,z). This variable is a unit vector
and specifies the direction of the ordinate dimension. |
| Input: | (double*) p2 | Pointer to an array of 3 doubles (x,y,z), the extension line start point. |
| Input: | (double*) p3 | Pointer to an array of 3 doubles (x,y,z), the extension line end point |
| Input: | (double*) p4 | Pointer to an array of 3 doubles (x,y,z); this variable is a unit vector
and specifies the orientation of the text; for example, values (1, 0,
0) would result in horizontal text that is read from left to right |
| Input: | (double) angle | Inclination angle of the text in radians (character slant) |
| Input: | (double) arrowSize | Arrow size meters |
| Input: | (BSTR) text | Dimension text string |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) witnessGap | Extension gap in meters |
| Input: | (double) witnessOvershoot | Extension overshoot in meters |
| Input: | (double) p5 | Pointer to an array of 3 doubles
(x,y,z), position of text |
| Output: | (LPDISPLAYDIMENSION) retval | Pointer to DisplayDimension object |
| Return: | (HRESULT)status | S_OK if successful. |

Remarks

SolidWorks creates this type of dimension between
the two specified points. It has no relation to your geometry.

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
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateNonAssociativeDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__CreateOrdinateDim3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
