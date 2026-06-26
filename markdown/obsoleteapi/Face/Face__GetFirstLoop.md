---
title: "Face::GetFirstLoop"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetFirstLoop.htm"
---

# Face::GetFirstLoop

This
method is obsolete and has been superseded by[Face2::GetFirstLoop](sldworksAPI.chm::/Face2/Face2__GetFirstLoop.htm).

Description

Thismethodreturns the first loop in the face.

Syntax (OLE Automation)

retval
= Face.GetFirstLoop ()

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Dispatch
pointer to the first loop |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetFirstLoop ( &retval
)

(Table)=========================================================

| Output: | (LPLOOP) retval | Pointer to the first loop |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The first loop in the face is not necessarily
the outer loop.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face_Object$$**$$ZGetLoop$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__GetFirstLoop.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
