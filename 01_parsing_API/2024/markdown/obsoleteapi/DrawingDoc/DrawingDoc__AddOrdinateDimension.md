---
title: "DrawingDoc::AddOrdinateDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__AddOrdinateDimension.htm"
---

# DrawingDoc::AddOrdinateDimension

This method is obsolete and has been superseded
by[DrawingDoc::AddOrdinateDimension2](DrawingDoc__AddOrdinateDimension2.htm).

Description

This
method inserts an ordinate dimension, based on the current selections.

Syntax (OLE Automation)

retval = DrawingDoc.AddOrdinateDimension
( DimType, LocX, LocY, LocZ )

(Table)=========================================================

| Input: | (long) DimType | Dimension type as defined in swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Return: | (BOOL) retval | TRUE if created, FALSE if not |

Syntax (COM)

status = DrawingDoc->AddOrdinateDimension
( DimType, LocX, LocY, LocZ, &retval )

(Table)=========================================================

| Input: | (long) DimType | Dimension type as defined in swAddOrdinateDims_e |
| --- | --- | --- |
| Input: | (double) LocX | X location for the dimension |
| Input: | (double) LocY | Y location for the dimension |
| Input: | (double) LocZ | Z location for the dimension |
| Output: | (VARIANT_BOOL) retval | TRUE if created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a complete set of ordinate
dimensions based on the current set of selections. First, select your
0 location from which all other dimensions are measured. SolidWorks uses
all other selections to create additional ordinate measurements.

Selections made after the method is called continue
to add ordinate measurements to the set. When you have finished adding
measurements for an ordinate dimension set, use ModelDoc2::SetPickMode
to clear the state.

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
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__AddOrdinateDimension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
