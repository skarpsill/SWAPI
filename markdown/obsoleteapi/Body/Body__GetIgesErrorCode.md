---
title: "Body::GetIgesErrorCode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetIgesErrorCode.htm"
---

# Body::GetIgesErrorCode

This method is obsolete and has been superseded by[Body2::GetIgesErrorCode](sldworksAPI.chm::/Body2/Body2__GetIgesErrorCode.htm).

Description

This method gets the current IGES error code.

Syntax (OLE Automation)

retval
= Body.GetIgesErrorCode ( index)

(Table)=========================================================

| Input: | (long)
index | Indexed
position of the error within the current list of errors |
| --- | --- | --- |
| Return: | (long)
retval | IGES
error code |

Syntax (COM)

status
= Body->GetIgesErrorCode ( index, &retval )

(Table)=========================================================

| Input: | (long) index | Indexed position of the error within the current list of errors |
| --- | --- | --- |
| Output: | (long) retval | IGES error code |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is intended for use during IGES
processing only.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Body\Body__GetIgesErrorCode.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
