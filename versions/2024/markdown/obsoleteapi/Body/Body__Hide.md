---
title: "Body::Hide"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Hide.htm"
---

# Body::Hide

This
method is obsolete and has been superseded by[Body2::Hide](sldworksAPI.chm::/Body2/Body2__Hide.htm).

Description

This method hides a temporary body object using the specified part's
context.

Syntax (OLE Automation)

void
Body.Hide ( part)

(Table)=========================================================

| Input: | (LPDISPATCH)
part | Pointer
to dispatch object, the part |
| --- | --- | --- |

Syntax (COM)

status
= Body->IHide ( part )

(Table)=========================================================

| Input: | (LPPARTDOC)
part | Pointer
to the part |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

While SolidWorks is displaying your body object with[Body::Display](Body__Display.htm),
do not release it explicitly or implicitly. Before releasing or allowing
other applications to release the body object, you must stop it from being
displayed using[Body::Hide](Body__Hide.htm).

COM applications should avoid explicitly releasing the body object by
calling Body->Release() while it is displayed by SolidWorks. Dispatch
applications should avoid allowing the body object to go out of scope
while it is displayed by SolidWorks, and destroyed when ReleaseDispatch
is automatically called. Dispatch applications should also avoid explicitly
releasing the body object by calling ReleaseDispatch while it is displayed
by SolidWorks.

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
<param name="Items" value="Body_Object$$**$$ZGetObjectDisplay$$**$$ZModifyObjectDisplay$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Body\Body__Hide.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
