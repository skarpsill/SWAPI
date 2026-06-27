---
title: "DisplayData::GetPolyLineAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayData/DisplayData__GetPolyLineAtIndex.htm"
---

# DisplayData::GetPolyLineAtIndex

This method is obsolete and has been superseded
by[DisplayData::GetPolyLineAtIndex2](sldworksAPI.chm::/DisplayData/DisplayData__GetPolylineAtIndex2.htm).

Description

This method gets the number of polylines in this display item.

Syntax (OLE Automation)

retval
= DisplayData.GetPolyLineAtIndex ( index )

(Table)=========================================================

| Input: | (long)
index | Index
of the desired line where the index begins at zero |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles (see below) |

Syntax (COM)

status
= DisplayData->GetPolyLineAtIndex ( index, retval )

(Table)=========================================================

| Input: | (long)
index | Index
of the desired line where the index begins at zero |
| --- | --- | --- |
| Output: | (double*)
retval | Array
of doubles (see below) |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

Format of return values is an array ofdoubleswith the format:

[Color, LineType, Unused, Unused, NumPolyPoints,
[x,y,z]]

where the[x,y,z]parameter is an array ofNumPolyPointsand LineType is the line type as defined in swLineTypes_e.

Use[DisplayData::GetPolyLineSizeAtIndex](DisplayData__GetPolyLineSizeAtIndex.htm)to determine the number of elements returned in this array.

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
<param name="_CURRENTFILEPATH" value="D:\sw2003\DisplayData\DisplayData__GetPolyLineAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
