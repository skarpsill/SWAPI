---
title: "ModelDoc2::InsertWeldSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertWeldSymbol2.htm"
---

# ModelDoc2::InsertWeldSymbol2

This method is obsolete and has been superseded
by[ModelDoc2::InsertWeldSymbol3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertWeldSymbol3.htm).

Description

This method creates a weld symbol on the last
edge selection.

Syntax (OLE Automation)

ModelDoc2.InsertWeldSymbol2 ( dim1, symbol, dim2,
symmetric, fieldWeld, showOtherSide, dashOnTop, peripheral, hasProcess,
processValue )

(Table)=========================================================

| Input: | (BSTR) dim1 | First text value to the left of the symbol |
| --- | --- | --- |
| Input: | (BSTR) symbol | Weld symbol name |
| Input: | (BSTR) dim2 | Text value to the right of the symbol |
| Input: | (VARIANT_BOOL) symmetric | TRUE puts the symbol both above and below the horizontal line |
| Input: | (VARIANT_BOOL) fieldWeld | TRUE puts a flag for field welding |
| Input: | (VARIANT_BOOL) showOtherSide | Not used; pass 0 |
| Input: | (VARIANT_BOOL) dashOnTop | TRUE puts the dash line on top |
| Input: | (VARIANT_BOOL) peripheral | TRUE puts a peripheral symbol |
| Input: | (VARIANT_BOOL) hasProcess | TRUE to specify a processValue |
| Input: | (BSTR) processValue | Process value if hasProcess is set to TRUE |

Syntax (COM)

status = ModelDoc2->InsertWeldSymbol2 ( dim1,
symbol, dim2, symmetric, fieldWeld, showOtherSide, dashOnTop, peripheral,
hasProcess, processValue )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) dim1 | First text value to the left of the symbol |
| --- | --- | --- |
| Input: | (BSTR) symbol | Weld symbol name |
| Input: | (BSTR) dim2 | Text value to the right of the symbol |
| Input: | (VARIANT_BOOL) symmetric | TRUE puts the symbol both above and below the horizontal line |
| Input: | (VARIANT_BOOL) fieldWeld | TRUE puts a flag for field welding |
| Input: | (VARIANT_BOOL) showOtherSide | Not used; pass 0 |
| Input: | (VARIANT_BOOL) dashOnTop | TRUE puts the dash line on top |
| Input: | (VARIANT_BOOL) peripheral | TRUE puts a peripheral symbol |
| Input: | (VARIANT_BOOL) hasProcess | TRUEto specify a processValue |
| Input: | (BSTR) processValue | Process value if hasProcess is set to TRUE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The symbol argument specifies the weld symbol name. A list of names
can be found in the text filegtol.sym,
which is located in the SolidWorks default installation folder<installation_dir>\lang\english.
The currently supported list is:

- BUTT
- BUSQ
- BUSV
- BUSB
- BUSVBR
- BUSBR
- BUSU
- BUSJ
- BACK
- FILL
- PLUG
- SPOT
- SEAM

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertWeldSymbol2.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertWeldSymbol2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
