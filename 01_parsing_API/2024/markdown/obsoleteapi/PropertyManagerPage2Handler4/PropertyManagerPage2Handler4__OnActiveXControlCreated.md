---
title: "PropertyManagerPage2Handler4::OnActiveXControlCreated"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnActiveXControlCreated.htm"
---

# PropertyManagerPage2Handler4::OnActiveXControlCreated

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnActiveXControlCreated](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnActiveXControlCreated.htm).

Description

This method is called when
an attempt to create an ActiveX control on the PropertyManager occurs.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler4.OnActiveXControlCreated
( Id, Status )

(Table)=========================================================

| Input: | (long) Id | ID of this ActiveX control |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Status | TRUE if the ActiveX control creation was successful, FALSE if not |
| Output: | (long) retval | Action to take if the creation of the ActiveX control failed as defined
in swHandleActiveXCreationFailure (see Remarks ) |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnActiveXControlCreated
( Id, Status, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of this ActiveX control |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) Status | TRUE if the creation of the ActiveX control was successful, FALSE if
not |
| Output: | (long) retval | Action to take if the creation of the ActiveX control failed as defined
in swHandleActiveXCreationFailure (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When the ActiveX control is created, the program
creating the PropertyManager page should receive notification from this
handler. Specify one of the available enumerators for this handler's retval
argument:

- swHandleActiveXCreationFailure_Cancel.
  Continue creating the PropertyManager page without the ActiveX control.
  This is the default.
- swHandleActiveXCreationFailure_Retry.
  Try to create the ActiveX control again. You can reuse the PropertyManagerPageActiveX::SetClass
  method to change the control ID or the license key to perhaps use another
  similar control or another version of the control, and then specify swHandleActiveXCreationFailure_Retry.
  Avoid an endless loop situation.
- swHandleActiveXCreationFailure_Continue.
  Cancel creating PropertyManager page. For example, it might be that the
  PropertyManager page is useless without the control, so the calling add-in
  might want to quit and handle the situation on its own.

Do not call PropertyManagerPageActiveX::GetControl
to get the interface object for this ActiveX control.

You cannot get a reference to the ActiveX
control inside this event handler because the page is notkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}displayed
when this notification is sent. You can only get the reference to the
control after the PropertyManager page is displayed.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PropertyManagerPage2Handler4_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnActiveXControlCreated.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
