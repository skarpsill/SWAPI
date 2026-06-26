---
title: "ModelDoc::CreatePlaneThru3Points2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneThru3Points2.htm"
---

# ModelDoc::CreatePlaneThru3Points2

This
method is obsolete and has been superseded by[ModelDoc2::CreatePlaneThru3Points2](../ModelDoc2/ModelDoc2__CreatePlaneThru3Points2.htm).

Description

This method creates a construction (reference) plane through three currently
selected points.

Syntax (OLE Automation)

retval = ModelDoc.CreatePlaneThru3Points2 ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
RefPlane object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->ICreatePlaneThru3Points2 (
&retval )

(Table)=========================================================

| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method follows the current document setting
for displaying of the reference plane as it is created. If display of
reference planes is disabled, then you do not see the reference plane
on the screen as it is created. If display of reference planes is enabled,
then you do see it as it is created. ModelDoc2::GetUserPreferenceToggle
and ModelDoc2::SetUserPreferenceToggle with swDisplayPlanes enum value
get or set this display preference.

This method does not select the reference plane
after it is created. Objects that are selected before running this method
are still selected when the method completes rather than the newly created
reference plane.

This method returns a RefPlane object. This object
can then be used for operations on the reference plane feature. Just having
a RefPlane may not be terribly useful, except that it is a reature, which
is an entity, so methods available on those objects are available. For
an OLE user, those functions are directly accessible; for a COM user,
those functions arekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}available
via use of a QueryInterface. For example, if the reference plane must
be selected, use Entity::Select.

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePlaneThru3Points2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
