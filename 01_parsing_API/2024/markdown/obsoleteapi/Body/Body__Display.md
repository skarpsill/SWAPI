---
title: "Body::Display"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Display.htm"
---

# Body::Display

This method is obsolete and has been superseded by[Body2::Display](../Body2/Body2__Display2.htm).

Description

This method displays a temporary body object in the context of the specified
part.

Syntax (OLE Automation)

void Body.Display ( part, color)

(Table)=========================================================

| Input: | (LPDISPATCH) part | Pointer to dispatch object, the part |
| --- | --- | --- |
| Input: | (long) color | Desired color |

Syntax (COM)

status = Body->IDisplay ( part,
color )

(Table)=========================================================

| Input: | (LPPARTDOC) part | Pointer to the part |
| --- | --- | --- |
| Input: | (long) color | Desired color |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

While SolidWorks is using this method to display this Body object, it
cannot be explicitly or implicitly released. Before releasing or allowing
the Body object to be released, use Body::Hide to prevent SolidWorks from
displaying the body.

COM applications can use Body->Release() to avoid explicitly releasing
the body object while it is displayed. Dispatch applications should not
allow the Body object to go out of scope while it is displayed, or be
destroyed when the ReleaseDispatch method is called automatically. Dispatch
applications should also avoid calling ReleaseDispatch to explicitly release
the body object while it is displayed.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Body\Body__Display.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
