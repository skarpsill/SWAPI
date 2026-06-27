---
title: "Body::GetType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body_GetType.htm"
---

# Body::GetType

This method is obsolete and has been superseded
byBody2::GetType .

Description

This method gets the body type.

Syntax (OLE Automation)

retval = Body.GetType ( )

(Table)=========================================================

| Return: | (long) retval | Body type as defined in swBodyType_e |
| --- | --- | --- |

Syntax (COM)

status = Body->GetType ( &retval )

(Table)=========================================================

| Output: | (long) retval | Body type as defined in swBodyType_e |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Empty is a special case that SolidWorks returns
if the interface pointer or underlying body pointer is NULL, indicating
the body is non-existent.

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
<param name="Items" value="Body_Object$$**$$ZGetInfoBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\Body\Body_GetType.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
