---
title: "DrawingDoc::GetLineFontInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetLineFontInfo.htm"
---

# DrawingDoc::GetLineFontInfo

This
method is obsolete and has been superseded by[DrawingDoc::GetLineFontInfo2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__GetLineFontInfo2.htm).

Description

This method gets the detailed information about the line font style,
including the line weight and segment lengths.

Syntax (OLE Automation)

retval
= DrawingDoc.GetLineFontInfo ( index)

(Table)=========================================================

| Input: | (long)
index | Index
position of the line font |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
containing the line font style information |

Syntax (COM)

status
= DrawingDoc->GetLineFontInfo ( index, &retval )

(Table)=========================================================

| Input: | (long)
index | Index
position of the Line font. |
| --- | --- | --- |
| Output: | (VARIANT)
retval | VARIANT
containing the line font style information |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

You can use DrawingDoc::GetLineFontInfo2 to get
line font information.

Lines are repeating patterns of space and solid
segments. The segCount argument returns the number of segments that define
the pattern, and segLengths[] specifies the length of each segment. A
negative length value indicates space.

For example:

Solid line: segCount = 1, segLenghts[]
= {0.5}

Dashed line: segCount = 2, segLengths[]
= {0.25, -0.25}

VARIANT format:

double weight -
THIN = 0.0, NORMAL = 1.0, LW_THICK = 2.0

double segCount -
Number of segments in the pattern

double segLengths[segCount] - Length of
each segment

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
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__GetLineFontInfo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
