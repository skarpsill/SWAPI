---
title: "CustomSymbol::GetTriangleAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetTriangleAtIndex.htm"
---

# CustomSymbol::GetTriangleAtIndex

This method is obsolete and has been superseded
by[Note::GetTriangleAtIndex](sldworksAPI.chm::/Note/Note__GetTriangleAtIndex.htm).

Description

This method gets the triangle at the specified index.

Syntax (OLE Automation)

retval
= CustomSymbol.GetTriangleAtIndex ( index)

(Table)=========================================================

| Input: | (long)
index | Index
of the triangle where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles (see below) |

Syntax (COM)

status
= CustomSymbol->IGetTriangleAtIndex ( index, retval )

(Table)=========================================================

| Input: | (long)
index | Index
of the triangle where the index begins at zero |
| --- | --- | --- |
| Output: | (double*)
retval | Pointer
to an array of doubles (see below) |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The return value is the following array of doubles:

[vertexPt1[3],vertexPt2[3],vertexPt3[3],isFilled,lineType]

(Table)=========================================================

| vertexPt1 [3] | First XYZ vertex point |
| --- | --- |
| vertexPt2 [3] | Second XYZ vertex point |
| vertexPt3 [3] | Third XYZ vertex point |
| isFilled | Boolean returned as a double and is TRUE if the triangle is filled,
FALSE otherwise |
| lineType | Line type as defined in swLineTypes_e |

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
<param name="Items" value="CustomSymbol_Object$$**$$ZGetInfoDa$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\CustomSymbol\CustomSymbol__GetTriangleAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
