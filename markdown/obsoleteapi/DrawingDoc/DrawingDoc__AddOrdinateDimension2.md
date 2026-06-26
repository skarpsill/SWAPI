---
title: "DrawingDoc::AddOrdinateDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AddOrdinateDimension2.htm"
---

# DrawingDoc::AddOrdinateDimension2

This method is obsolete and has been superseded
by[ModelDocExtension::AddOrdinateDimension](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__AddOrdinateDimension.htm).

Description

This method inserts an ordinate
dimension.

Syntax (OLE Automation)

retval = DrawingDoc.AddOrdinateDimension2 ( DimType,
LocX, LocY, LocZ)

(Table)=========================================================

| Input: | (long) DimType | Dimension type as defined in
swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Output: | (long*) retval | Error as defined by swCreateOrdDimError_e |

Syntax (COM)

status = DrawingDoc->AddOrdinateDimension2 ( DimType,
LocX, LocY, LocZ, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (long) DimType | Dimension type as defined in
swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Output: | (long*) retval | Error as defined by swCreateOrdDimError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method:

- Requires
  that you select two or more parallel edges. The ordinate origin is relative
  to the sheet origin and, depending on the type of ordinate dimension,
  either the X or Y value is ignored.
- Creates a
  complete set of ordinate dimensions based on the current set of selections.
  First, select your 0 location from which all other dimensions are measured.
  All other selections are used to create additional ordinate measurements.

Selections made after the method is called continue
to add ordinate measurements to the set. When you have finished adding
measurements for an ordinate dimension set, use ModelDoc2::SetPickMode
to clear the state.

Any errors are returned as error codes, not dialog
boxes.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AddOrdinateDimension2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AddOrdinateDimension2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXOrdinateDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AddOrdinateDimension2.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
