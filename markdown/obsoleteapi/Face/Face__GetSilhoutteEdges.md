---
title: "Face::GetSilhoutteEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetSilhoutteEdges.htm"
---

# Face::GetSilhoutteEdges

This
method is obsolete and has been superseded by[Face2::GetSilhoutteEdgesVB](sldworksAPI.chm::/Face2/Face2__GetSilhoutteEdgesVB.htm).

Description

This method generates and returns the silhouette edges for this face
with the specified root point and in the specified direction.

Syntax (OLE Automation)

retval
= Face.GetSilhoutteEdgesVB ( xroot, yroot, zroot, xnormal, ynormal, znormal
)

(Table)=========================================================

| Input: | (double)
xroot | X
component of the root point |
| --- | --- | --- |
| Input: | (double)
yroot | Y
component of the root point |
| Input: | (double)
zroot | Z
component of the root point |
| Input: | (double)
xnormal | X
component of the direction vector |
| Input: | (double)
ynormal | Y
component of the direction vector |
| Input: | (double)
znormal | Z
component of the direction vector |
| Return: | (VARIANT)
retval | SafeArray
containing an array of Dispatch pointers for the edges |

Syntax (COM)

status
= Face->IGetSilhoutteEdges ( root, normal, siledgesout )

(Table)=========================================================

| Input: | (double*)
root | Array
of doubles defining the root point |
| --- | --- | --- |
| Input: | (double*)
normal | Array
of doubles defining the direction vector |
| Output: | (LPEDGE*)
siledgesout | Array
to hold the edge pointers |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The edges are not added to the face and, therefore, are not returned
by Face::GetEdges. These edges are created and handed back to the caller
as an array of edges or as a Variant packed with edges.

The vector root point and a vector direction define the orientation
for the desired silhouette edge creation.

The siledgesout array contains two elements for each edge: the silhouette
edge and an unused parameter. To iterate through the edges an application,
you need to step through every second element.

If you are using the COM implementation, then you must call Face::IGetSilhoutteEdgeCount
to get the size of array required to hold the edges before you call this
method.

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
<param name="Items" value="Face_Object$$**$$Edge_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__GetSilhoutteEdges.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
