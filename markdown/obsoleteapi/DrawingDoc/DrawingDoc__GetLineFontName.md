---
title: "DrawingDoc::GetLineFontName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__GetLineFontName.htm"
---

# DrawingDoc::GetLineFontName

This
method is obsolete and has been superseded by[DrawingDoc::GetLineFontName2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__GetLineFontName2.htm).

Description

This method returns the descriptive name for the line font style at
the specified index.

Syntax (OLE Automation)

retval
= DrawingDoc.GetLineFontName ( index)

(Table)=========================================================

| Input: | (long)
index | Index
position of the line font style |
| --- | --- | --- |
| Return: | (BSTR)
retval | Line
font style name |

Syntax (COM)

status
= DrawingDoc->GetLineFontName ( index, &retval )

(Table)=========================================================

| Input: | (long)
index | Index
position of the line font style |
| --- | --- | --- |
| Output: | (BSTR)
retval | Line
font style name |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

Example or style names are:

- Visible
- Hidden
- Sketch
- Detail
- Section
- Dimensions
- Centerlines
- Crosshatch
- TanVisible

You can also use DrawingDoc::GetLineFontName2,
which returns the actual name of the line fonts (for example, Solid, Center,
Dashed, Centerline, and so on.).

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
<param name="Items" value="DrawingDoc_Object$$**$$GetLineFontCount$$**$$GetLineFontCount2$$**$$GetLineFontInfo$$**$$GetLineFontInfo2$$**$$GetLineFontName$$**$$GetLineFontName2$$**$$ZGetNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__GetLineFontName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
