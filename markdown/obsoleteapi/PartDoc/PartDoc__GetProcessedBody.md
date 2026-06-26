---
title: "PartDoc::GetProcessedBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetProcessedBody.htm"
---

# PartDoc::GetProcessedBody

The
OLE version of this method is obsolete and has been superseded by[Body2::GetProcessedBody](../Body2/Body2__GetProcessedBody.htm).

The
COM version of this method is obsolete and has been superseded by PartDoc::IGetProcessedBody2 .

Description

This method preprocesses the geometry of a body so that:

- Closed periodic faces are split into two faces
  (for example, the lateral face of a cylinder).
- Any faces that straddle the seam of the underlying
  surface are split into two faces.

Syntax (OLE Automation)

retval = PartDoc.GetProcessedBody ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, a body, which is a copy of the body for
this part |
| --- | --- | --- |

Syntax (COM)

status = PartDoc->IGetProcessedBody (
&retval )

(Table)=========================================================

| Output: | (LPBODY) retval | Pointer to the body, which is a copy of the body for this part |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This type of preprocessing is sometimes necessary (for example, IGES)
for exporting to systems that have difficulty with periodic conditions
.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PartDoc_Object$$**$$ZAccessorByCreate$$**$$ZGetBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PartDoc\PartDoc__GetProcessedBody.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
