---
title: "ModelDoc::CreatePlaneAtOffset2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneAtOffset2.htm"
---

# ModelDoc::CreatePlaneAtOffset2

This
method is obsolete and has been superseded by[ModelDoc2::CreatePlaneAtOffset2](../ModelDoc2/ModelDoc2__CreatePlaneAtOffset2.htm).

Description

This method creates a construction (reference)
plane at an offset from the selected plane or planar face.

Syntax (OLE Automation)

retval = ModelDoc.CreatePlaneAtOffset2 (val, flipDir)

(Table)=========================================================

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the offset direction for the resulting
plane, FALSE to not |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
RefPlane object |

Syntax (COM)

status = ModelDoc->ICreatePlaneAtOffset2 ( val,
flipDir, &retval )

(Table)=========================================================

| Input: | (double) val | Offset distance from selected plane in meters |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the offset direction for the resulting
plane, FALSE to not |
| Output: | (LPREFPLANE) retval | Pointer to the newly created RefPlane object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method follows the current document setting
for displaying of the reference plane as it is created. If display of
reference planes is disabled, then you do not see the reference plane
on the screen as it is created. If display of reference planes is enabled,
then you dokadov_tag{{<spaces>}}kadov_tag{{</spaces>}}see
it as it is created. ModelDoc2::GetUserPreferenceToggle and ModelDoc2::SetUserPreferenceToggle
with swDisplayPlanes enum value get or set this display preference.

This method does not select the reference plane
after it is created. Objects that are selected before running this method
are still be selected when the method completeskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}rather
than the newly created reference plane.

This method returns a RefPlane object. YOu can
use this object for further operations on the reference plane feature.
Just having a reference plane may not be terribly useful, except that
it is a fFeature, which is an entity, so methods available on those objects
are available. For an OLE user, those functions are directly accessible;for
a COM user, those functions are available via use of a QueryInterface.
For example, to select the reference plane, use Entity::Select.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePlaneAtOffset2.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
