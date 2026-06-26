---
title: "ModelDoc::InsertExtendSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertExtendSurface.htm"
---

# ModelDoc::InsertExtendSurface

This
method is obsolete and has been superseded by[ModelDoc2::InsertExtendSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertExtendSurface.htm).

Description

This method extends a surface along the selected
faces or edges.

Syntax (OLE Automation)

void ModelDoc.InsertExtendSurface (extendLinear, endCondition, distance)

(Table)=========================================================

| Input: | (BOOL) extendLinear | TRUE to extend surface linearly, FALSE to extend
along the same surface |
| --- | --- | --- |
| Input: | (long) endCondition | 0
– Extend surface by given distance 1
– Extend surface up to a selected point 2
– Extend surface up to a selected surface |
| Input: | (double) distance | Distance to extend surface along |

Syntax (COM)

status = ModelDoc->InsertExtendSurface ( extendLinear,
endCondition, distance )

(Table)=========================================================

| Input: | (VARIANT_BOOL) extendLinear | TRUE to extend surface linearly, FALSE to extend
along the same surface |
| --- | --- | --- |
| Input: | (long) endCondition | 0
– Extend surface by given distance 1
– Extend surface up to a selected point 2
– Extend surface up to a selected surface |
| Input: | (double) distance | Distance to extend surface along |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selection list can contain faces or edges from
the surface. These selected entities will be extended away from the surface
according to the input arguments.

The selected point or surface to extend to should
be in the selection list. If endCondition is to a selected surface, then
currently only faces from solids are supported.

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertExtendSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
