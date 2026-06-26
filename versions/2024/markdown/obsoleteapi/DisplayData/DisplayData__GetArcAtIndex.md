---
title: "DisplayData::GetArcAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetArcAtIndex.htm"
---

# DisplayData::GetArcAtIndex

This
method is obsolete and has been superseded by[DisplayData::GetArcAtIndex2](sldworksAPI.chm::/DisplayData/DisplayData__GetArcAtIndex2.htm).

Description

This method gets information for the specified arc.

Syntax (OLE Automation)

retval
= DisplayData.GetArcAtIndex ( index)

(Table)=========================================================

| Input: | (long)
index | Index
of the desired arc where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles (see below) |

Syntax (COM)

status
= DisplayData->IGetArcAtIndex ( index, retval )

(Table)=========================================================

| Input: | (long)
index | Index
of the desired arc where the index begins at zero |
| --- | --- | --- |
| Output: | (double*)
retval | Pointer
to an array of doubles (see below) |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The return value is the following array of doubles
:

[lineType,startPt[3],endPt[3],centerPt[3],rotationDir]

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
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DisplayData_Object$$**$$ZGetInfoDisplayData$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\DisplayData\DisplayData__GetArcAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
