---
title: "Body::GetFirstSelectedFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetFirstSelectedFace.htm"
---

# Body::GetFirstSelectedFace

This method is obsolete and has been superseded by[Body2::GetFirstSelectedFace.](sldworksAPI.chm::/Body2/Body2__GetFirstSelectedFace.htm)

Description

This method is used in combination with Body::GetProcessedBodyWithSelFace
and is intended for IGES type routines.

Syntax (OLE Automation)

retval
= Body.GetFirstSelectedFace ()

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to dispatch object, the first selected face |
| --- | --- | --- |

Syntax (COM)

status
= Body->IGetFirstSelectedFace ( &retval )

(Table)=========================================================

| Output: | (LPFACE)
retval | Pointer
to the first selected face |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

Do not use this method for general selection handling. To handle items
selected by the user or items selected with ModelDoc2::SelectByID, use
SelectionMgr::GetSelectedObject2.

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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003old\Body\Body__GetFirstSelectedFace.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
