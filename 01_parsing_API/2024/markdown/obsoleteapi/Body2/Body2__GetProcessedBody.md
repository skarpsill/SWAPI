---
title: "Body2::GetProcessedBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__GetProcessedBody.htm"
---

# Body2::GetProcessedBody

This method is obsolete and has been superseded
byBody2::GetProcessedBody2 .

Description

This method pre-processes the geometry of a body so that:

- Closed periodic faces (for example, the lateral
  face of a cylinder) are split into two faces.
- Faces that straddle the seam, if any, of the underlying
  surface are split into two faces.

Syntax (OLE Automation)

retval = Body2.GetProcessedBody ( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to dispatch object, a body; this body is a processed copy of
the body for this part |
| --- | --- | --- |

Syntax (COM)

status = Body2->IGetProcessedBody
( &retval )

(Table)=========================================================

| Output: | (LPBODY2) retval | Pointer to the body; this body is a processed copy of the body for this
part |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

Pre-processing (for example, IGES) is sometimes necessary for exporting
to systems that have difficulty with periodic conditions.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
dtcid=2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body2\Body2__GetProcessedBody.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
dtcid=3
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
<param name="Items" value="Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body2\Body2__GetProcessedBody.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
