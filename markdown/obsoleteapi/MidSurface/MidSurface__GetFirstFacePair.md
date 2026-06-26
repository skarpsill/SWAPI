---
title: "MidSurface::GetFirstFacePair"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFirstFacePair.htm"
---

# MidSurface::GetFirstFacePair

This method is obsolete
and has been superseded by[MidSurface2::GetFirstFacePair](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFirstFacePair.htm).

Description

This method returns the first face pair in this MidSurface feature along
with the thickness (in meters) between the two faces. The two face objects
returned are the two parallel faces from the original part body that were
used to generate the first neutral face in this MidSurface feature.

Syntax (OLE Automation)

retval = MidSurface.GetFirstFacePair
( &thickness, &partnerFaceDisp)

(Table)=========================================================

| Output: | (double) thickness | Distance between the two parallel faces, from Face1 and from Face2 |
| --- | --- | --- |
| Output: | (LPDISPATCH) partnerFaceDisp | Pointer to a Dispatch object, a face on the original part body used
in generating the neutral face |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, a face on the original part body used
in generating the neutral face |

Syntax (COM)

status = MidSurface->IGetFirstFacePair
( &thickness, &partnerFaceDisp, &retval )

(Table)=========================================================

| Output: | (double) thickness | Distance between the two parallel faces, fromFace1 and fromFace2 |
| --- | --- | --- |
| Output: | (LPFACE) partnerFaceDisp | Pointer to a face on the original part body used in generating the neutral
face |
| Output: | (LPFACE) retval | Pointer to a face on the original part body used in generating the neutral
face |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to MidSurface::GetFirstFace except this method
does not return the neutral face.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\MidSurface\MidSurface__GetFirstFacePair.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
