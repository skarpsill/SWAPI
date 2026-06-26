---
title: "ModelDoc::InsertOffsetSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertOffsetSurface.htm"
---

# ModelDoc::InsertOffsetSurface

This
method is obsolete and has been superseded by[ModelDoc2::InsertOffsetSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertOffsetSurface.htm).

Description

This method inserts an offset surface.

Syntax (OLE Automation)

void ModelDoc.InsertOffsetSurface
( thickness, reverse )

(Table)=========================================================

| Input: | (double) offset | Offset of surface from reference |
| --- | --- | --- |
| Input: | (BOOL) reverse | TRUE to reverse the direction of the offset, FALSE
to not |

Syntax (COM)

status = ModelDoc->InsertOffsetSurface
( thickness, reverse )

(Table)=========================================================

| Input: | (double) offset | Offset of surface from reference |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverse | TRUE to reverse the direction of the offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as interactively creating a planar surface by
selectingInsert,
Reference Geometry, Offset Surface.
See the SolidWorks Help for more information about what entities
are valid for selection.

Make the selections using ModelDoc::SelectByID before
calling this method.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertOffsetSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
