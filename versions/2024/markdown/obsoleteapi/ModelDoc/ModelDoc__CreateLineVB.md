---
title: "ModelDoc::CreateLineVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLineVB.htm"
---

# ModelDoc::CreateLineVB

This
method is obsolete and has been superseded by[ModelDoc::CreateLine2](ModelDoc__CreateLine2.htm).

Description

This method:

- Creates a line from P1 to P2
- Provided for use in Visual Basic and other forms
  of Basic that do not support SafeArrays.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
- Enables automatic relations for the line, which
  may not be suitable for creating very small segments in database.

Syntax (OLE Automation)

void ModelDoc.CreateLineVB ( x1, y1,
z1, x2, y2, z2)

(Table)=========================================================

| Input: | (double) x1 | Start Point X, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Start Point Y, in meters |
| Input: | (double) z1 | Start Point Z, in meters |
| Input: | (double) x2 | End Point X, in meters |
| Input: | (double) y2 | End Point Y, in meters |
| Input: | (double) z2 | End Point Z, in meters |

Syntax (COM)

status = ModelDoc->CreateLineVB
( x1, y1, z1, x2, y2, z2 )

(Table)=========================================================

| Input: | (double) x1 | Start Point X, in meters |
| --- | --- | --- |
| Input: | (double) y1 | Start Point Y, in meters |
| Input: | (double) z1 | Start Point Z, in meters |
| Input: | (double) x2 | End Point X, in meters |
| Input: | (double) y2 | End Point Y, in meters |
| Input: | (double) z2 | End Point Z, in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__CreateLineVB.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Compound_Note_Example$$**$$Direct_Add_to_Database_Example$$**$$Line_From_User_Selection_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__CreateLineVB.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
