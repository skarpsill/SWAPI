---
title: "MidSurface::GetFirstFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFirstFace.htm"
---

# MidSurface::GetFirstFace

This method is obsolete
and has been superseded by[MidSurface2::GetFirstFace](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFirstFace.htm).

Description

This method returns the first face in this MidSurface feature along
with three other items. The first two return values are the two faces
from the original part body that were used to generate this MidSurface
face. The next return value is the thickness (in meters) between the two
parallel faces from the original part body. The last return value is the
first face in this MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetFirstFace (
&fromFace1Disp, &fromFace2Disp, &thickness)

(Table)=========================================================

| Output: | (LPDISPATCH) fromFace1Disp | Pointer to a Dispatch object, a face on the original part body used
in generating the neutral face |
| --- | --- | --- |
| Output: | (LPDISPATCH) fromFace2Disp | Pointer to a Dispatch object, a face on the original part body used
in generating the neutral face |
| Output: | (double) thickness | Distance between the two parallel faces, fromFace1Disp and fromFace2Disp |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first face in this MidSurface feature |

Syntax
(COM)

status = MidSurface->IGetFirstFace
( &fromFace1Disp, &fromFace2Disp, &thickness, &retval
)

(Table)=========================================================

| Output: | (LPFACE) fromFace1Disp | Pointer to a Dispatch object, a face on the original part body used
in generating the neutral face |
| --- | --- | --- |
| Output: | (LPFACE) fromFace2Disp | Pointer to a Dispatch object, a face on the original part body used
in generating the neutral face |
| Output: | (double) thickness | Distance between the two parallel faces, fromFace1Disp and fromFace2Disp |
| Output: | (LPFACE) retval | First face in this MidSurface feature |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="MidSurface_Object$$**$$ZGetFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\MidSurface\MidSurface__GetFirstFace.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_All_Edges_and_Vertices_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\MidSurface\MidSurface__GetFirstFace.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
