---
title: "ModelDoc::InsertBendTableNew"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertBendTableNew.htm"
---

# ModelDoc::InsertBendTableNew

This
method is obsolete and has been superseded by[ModelDoc2::InsertBendTableNew](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertBendTableNew.htm).

Description

This method inserts a new bend table into the
model document.

Syntax (OLE Automation)

ok = ModelDoc.InsertBendTableNew ( filename, units,
type )

(Table)=========================================================

| Input: | (BSTR) filename | Filename of this new bend table |
| --- | --- | --- |
| Input: | (BSTR) units | Value for units to use for this operation. |
| Input: | (BSTR) type | Value for table type |
| Return: | (BOOL) ok | TRUE if the new table is successfully inserted,
FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertBendTableNew ( filename,
units, type, &ok )

(Table)=========================================================

| Input: | (BSTR) filename | Filename of this new bend table |
| --- | --- | --- |
| Input: | (BSTR) units | Value for units to use for this operation |
| Input: | (BSTR) type | Value for table type |
| Output: | (VARIANT_BOOL) ok | TRUE if the new table is successfully inserted,
FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use these values for:

units: "Millimeters", "Centimeters",
"Meters","Inches", or "Feet"

type: "Bend Allowance"
or "Bend Deduction"

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertBendTableNew.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertBendTableNew.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
