---
title: "Body::CreateOffsetSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateOffsetSurface.htm"
---

# Body::CreateOffsetSurface

This method is obsolete and has been superseded by[Body2::CreateOffsetSurface](sldworksAPI.chm::/Body2/Body2__CreateOffsetSurface.htm).

Description

This method creates a new surface which is offset from an existing surface
object.

Syntax (OLE Automation)

retval
= Body.CreateOffsetSurface ( surfaceIn, distance)

(Table)=========================================================

| Input: | (LPDISPATCH)
surfaceIn | Pointer
to a dispatch object, the surface from which you want to offset |
| --- | --- | --- |
| Input: | (double)
distance | Offset
distance |
| Return: | (LPDISPATCH)
retval | Pointer
to a Dispatch object, the newly created surface |

Syntax (COM)

status
= Body->ICreateOffsetSurface ( surfaceIn, distance, &retval )

(Table)=========================================================

| Input: | (LPSURFACE)
surfaceIn | Pointer
to a dispatch object, the surface from which you want to offset |
| --- | --- | --- |
| Input: | (double)
distance | Offset
distance |
| Output: | (LPSURFACE)
retval | Pointer
to the newly created surface |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

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
<param name="Items" value="Body_Object$$**$$ZCreateSurface$$**$$ZAccessorByCreate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateOffsetSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
