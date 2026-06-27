---
title: "ModelDoc::SketchFillet1"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchFillet1.htm"
---

# ModelDoc::SketchFillet1

This method is obsolete and has been superseded by[ModelDoc::SketchFillet2](ModelDoc__SketchFillet2.htm).

Description

This method creates a fillet between the two selected sketch entities.

Syntax (OLE Automation)

(void) ModelDoc.SketchFillet1 ( rad
)

(Table)=========================================================

| Input: | (double) rad | Radius for the fillet |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SketchFillet1
( rad )

(Table)=========================================================

| Input: | (double)rad | Radius for the fillet |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If one of the sketch entities is constrained (for example, the length
is dimensioned), then this method maintains the original corner geometry.
If neither of the sketch entities are dimensioned, then the geometry is
removed in the fillet operation.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SketchFillet1.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
