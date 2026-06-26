---
title: "Face::IGetSilhoutteEdgeCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetSilhoutteEdgeCount.htm"
---

# Face::IGetSilhoutteEdgeCount

This
method is obsolete and has been superseded by[Face2::IGetSilhoutteEdgeCount](sldworksAPI.chm::/Face2/Face2__IGetSilhoutteEdgeCount.htm).

Description

This method gets the number of silhouette edges for this face.

Syntax (OLE Automation)

Not
available.

Syntax (COM)

status
= Face->IGetSilhoutteEdgeCount ( root, normal, &ret )

(Table)=========================================================

| Input: | (double*)
root | Array
of doubles defining the root point |
| --- | --- | --- |
| Input: | (double*)
normal | Array
of doubles defining the direction vector |
| Output: | (long)
ret | Number
of silhouette edges |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

For a given vector root point (root) and
a vector direction (normal), this method calculates the number of edges
that returned by[Face::IGetSilhoutteEdges](Face__GetSilhoutteEdges.htm).

The siledgesout array returned by[Face::IGetSilhoutteEdges](Face__GetSilhoutteEdges.htm)contains
two elements for each edge: the silhouette edge and an unused parameter.
To allocate data to hold the returned information, allocate double the
elements returned by this method.

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
<param name="Items" value="Face_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Face\Face__IGetSilhoutteEdgeCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
