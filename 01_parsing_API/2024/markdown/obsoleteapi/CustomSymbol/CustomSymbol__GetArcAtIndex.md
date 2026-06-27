---
title: "CustomSymbol::GetArcAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetArcAtIndex.htm"
---

# CustomSymbol::GetArcAtIndex

This method are obsolete and has been superseded
by[Note::GetArcAtIndex](sldworksAPI.chm::/Note/Note__GetArcAtIndex.htm).

Description

This
method gets information for the specified arc.

Syntax (OLE Automation)

retval
= CustomSymbol.GetArcAtIndex ( index)

(Table)=========================================================

| Input: | (long)
index | Index
of the desired arc where the index begins at 0 |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles (see Remarks ) |

Syntax (COM)

status
= CustomSymbol->IGetArcAtIndex ( index, retval )

(Table)=========================================================

| Input: | (long)
index | Index
of the desired arc where the index begins at 0 |
| --- | --- | --- |
| Output: | (double*)
retval | Pointer
to an array of doubles (see Remarks ) |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The return value is the following array of doubles
:

[lineType,startPt[3],endPt[3],centerPt[3],rotationDir]

where:

(Table)=========================================================

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ arc start point |
| endPt [3] | XYZ arc end point |
| centerPt [3] | XYZ arc center point |
| rotationDir | Boolean returned as a double and represents the rotation direction,
where CCW = TRUE and CW = FALSE |

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
<param name="Items" value="CustomSymbol_Object$$**$$ZGetInfoCustomSymbol$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\CustomSymbol\CustomSymbol__GetArcAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
