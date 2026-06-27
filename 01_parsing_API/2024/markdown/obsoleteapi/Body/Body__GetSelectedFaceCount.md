---
title: "Body::GetSelectedFaceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetSelectedFaceCount.htm"
---

# Body::GetSelectedFaceCount

This method is obsolete and has been superseded by[Body2::GetSelectedFaceCount](sldworksAPI.chm::/Body2/Body2__GetSelectedFaceCount.htm).

Description

This method gets the number of selected
faces.

Syntax (OLE Automation)

retval
= Body.GetSelectedFaceCount ()

(Table)=========================================================

| Return: | (long)
retval | Number
of selected faces |
| --- | --- | --- |

Syntax (COM)

status
= Body->GetSelectedFaceCount ( &retval )

(Table)=========================================================

| Output: | (long)
retval | Number
of selected faces |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This method is used iwith[Body::GetProcessedBodyWithSelFace](Body__GetProcessedBodyWithSelFace.htm)and is intended for IGES routines.

Do not use this method for general selection
handling. If you want to get items selected by the user or items selected
with[ModelDoc::SelectByID](../ModelDoc/ModelDoc__SelectByID.htm),
use SelectionMgr::GetSelectedObjectCount.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Body\Body__GetSelectedFaceCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
