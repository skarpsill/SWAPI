---
title: "ModelDoc::InsertAxis"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertAxis.htm"
---

# ModelDoc::InsertAxis

This method is obsolete
and has been superseded by[ModelDoc2::InsertAxis](../ModelDoc2/ModelDoc2__InsertAxis.htm).

Description

This method inserts a reference axis based on the currently selected
items.

Syntax (OLE Automation)

retval = ModelDoc.InsertAxis ( )

(Table)=========================================================

| Return: | (Boolean) retval | TRUE if the reference axis is created successfully, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertAxis (
&retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if the reference axis is created successfully, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The behavior of this method is identical to that used to interactively
create axes. SolidWorks creates the reference axis based on the combination
of items selected (for example, two vertices, an edge, a cylindrical surface,
and so on). The set of valid selection combinations will match the set
of valid selection combinations for the interactive operation.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefPlane$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertAxis.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="InsertAxis_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertAxis.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
