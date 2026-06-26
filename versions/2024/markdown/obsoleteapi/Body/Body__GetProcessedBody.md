---
title: "Body::GetProcessedBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetProcessedBody.htm"
---

# Body::GetProcessedBody

This
method is obsolete and has been superseded by[Body2::GetProcessedBody2](sldworksAPI.chm::/Body2/Body2__GetProcessedBody2.htm).

Description

This method pre-processes the geometry of a body so that:

- Closed periodic faces (for
  example, the lateral face of a cylinder) are split into two faces.
- Faces that straddle the
  seam, if any, of the underlying surface are split into two faces.

Syntax (OLE Automation)

retval
= Body.GetProcessedBody ( )

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to Dispatch object, a body; this body is a copy of the body for this part,
processed as previously described |
| --- | --- | --- |

Syntax (COM)

status
= Body->IGetProcessedBody ( &retval )

(Table)=========================================================

| Output: | (LPBODY)
retval | Pointer
to the body; this body is a copy of the body for this part, processed
as previously described |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

Such pre-processing is sometimes necessary (for example, IGES), for
exporting into systems that have difficulty with periodic conditions.

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
<param name="Items" value="Body_Object$$**$$ZAccessorByCreate$$**$$ZGetBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__GetProcessedBody.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_GetProcessed_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__GetProcessedBody.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
