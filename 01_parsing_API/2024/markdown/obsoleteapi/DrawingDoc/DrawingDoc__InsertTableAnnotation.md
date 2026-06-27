---
title: "DrawingDoc::InsertTableAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertTableAnnotation.htm"
---

# DrawingDoc::InsertTableAnnotation

This method is obsolete and has been superseded
by[DrawingDoc::InsertTableAnnotation2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertTableAnnotation2.htm).

Description

This method inserts a table
annotation in this drawing.

Syntax (OLE Automation)

retval = DrawingDoc.InsertTableAnnotation ( X, Y,
AnchorType, Rows, Columns)

(Table)=========================================================

| Input: | (double) X | X coordinate at which to insert this table annotation |
| --- | --- | --- |
| Input: | (double) Y | Y coordinate at which to insert this table annotation |
| Input: | (long) AnchorType | Type of anchor as defined by swBOMConfigurationAnchorType_e
(see Remarks ) |
| Input: | (long) Rows | Number of rows in the table annotation |
| Input: | (long) Columns | Number of columns in the table annotation |
| Output: | (LPTABLEANNOTATION*) retval | Pointer to the newly created TableAnnotation
object |

Syntax (COM)

status = DrawingDoc->InsertTableAnnotation ( X,
Y, AnchorType, Rows, Columns, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (double) X | X coordinate at which to insert this table annotation |
| --- | --- | --- |
| Input: | (double) Y | Y coordinate at which to insert this table annotation |
| Input: | (long) AnchorType | Type of anchor as defined by swBOMConfigurationAnchorType_e
(see Remarks ) |
| Input: | (long) Rows | Number of rows in the table annotation |
| Input: | (long) Columns | Number of columns in the table annotation |
| Output: | (LPTABLEANNOTATION*) retval | Pointer to the newly created TableAnnotation
object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The anchor helps to define
which corner is represented by the X and Y values. After the table is
inserted, the anchor does not mean anything in the context of the general
table. Because this method is used for general, BOM, and revision tables,
TableAnnotation::Anchored is only meaningful for the BOM and revision
tables.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\DrawingDoc\DrawingDoc__InsertTableAnnotation.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\DrawingDoc\DrawingDoc__InsertTableAnnotation.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXInsertTable$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\DrawingDoc\DrawingDoc__InsertTableAnnotation.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
