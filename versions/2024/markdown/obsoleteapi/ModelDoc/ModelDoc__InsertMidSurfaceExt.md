---
title: "ModelDoc::InsertMidSurfaceExt"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertMidSurfaceExt.htm"
---

# ModelDoc::InsertMidSurfaceExt

This
method is obsolete and has been superseded by[ModelDoc2::InsertMidSurfaceExt](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertMidSurfaceExt.htm).

Description

This method inserts a midsurface feature. A midsurface feature is calculated
from the solid body in your part document.

Syntax (OLE Automation)

retval = ModelDoc.InsertMidSurfaceExt
( placement, knitFlag)

(Table)=========================================================

| Input: | (double) placement | Value from -1 to 1, which indicates the desired location of the midsurface
relative to the face pair; a value of 0.0 will place the midsurface equally
between the face pair |
| --- | --- | --- |
| Input: | (BOOL) knitFlag | TRUE if you wish to knit all the Reference surfaces (neutral sheets)
into a single sheet body, FALSE if you want the midsurface feature to
contain individual reference surface geometry |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the midsurface feature created |

Syntax
(COM)

status = ModelDoc->IInsertMidSurfaceExt
( placement, knitFlag, &retval )

(Table)=========================================================

| Input: | (double) placement | Value from -1 to 1, which indicates the desired location of the midsurface
relative to the face pair; a value of 0.0 will place the midsurface equally
between the face pair |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) knitFlag | TRUE if you wish to knit all the Reference surfaces (neutral sheets)
into a single sheet body, FALSE if you want the midsurface feature to
contain individual reference surface geometry |
| Output: | (LPMIDSURFACE) retval | Pointer to the midsurface feature created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method first finds all parallel pairs of faces from the part solid.
For each pair of parallel faces found, it creates a neutral reference
surface between the two faces. The placement position of the reference
surface is controlled by the placement parameter. This process repeats
itself until all parallel body faces have been processed. At the end of
this process, all the reference surfaces are knitted into a single reference
surface if knitFlag is set to TRUE.

The hierarchy of a midSurface feature is as follows:

A midsurface feature will contain one or more reference surfaces. If
sewn successfully using the knitFlag = TRUE option, then the midsurface
feature will contain only one reference surface. Each reference surface
is considered a sheet body. The sheet body has the normal topology that
you would expect to find on a body object (for example, faces, edges,
and so on). See the MidSurface object for methods, which provide access
to this topology.

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
<param name="Items" value="ModelDoc_Object$$**$$ZAccessorByCreate$$**$$ZCreateMidSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertMidSurfaceExt.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
