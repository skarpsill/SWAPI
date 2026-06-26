---
title: "Body::IGetIntersectionEdgeCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__IGetIntersectionEdgeCount.htm"
---

# Body::IGetIntersectionEdgeCount

This method is obsolete and has been superseded by[Body2::IGetIntersectionEdgeCount](sldworksAPI.chm::/Body2/Body2__IGetIntersectionEdgeCount.htm).

Description

This method gets the number of intersection edges between this body
and the specified tool body.

Syntax (OLE Automation)

Not available.

Syntax
(COM)

status = Body->IGetIntersectionEdgeCount
( toolBodyIn, &retval )

(Table)=========================================================

| Input: | (LPBODY) toolBodyIn | Pointer to the temporary body object used to perform the intersection |
| --- | --- | --- |
| Output: | (long) retval | Number of edges generated when these two bodies intersect |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use the return value from this method
with[Body::GetIntersectionEdges](Body__GetIntersectionEdges.htm).

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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body\Body__IGetIntersectionEdgeCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
