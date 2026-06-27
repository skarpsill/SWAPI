---
title: "ModelDoc::CreateFeatureMgrView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateFeatureMgrView2.htm"
---

# ModelDoc::CreateFeatureMgrView2

This method is obsolete
and has been superseded by[ModelDoc::CreateFeatureMgrView3](ModelDoc__CreateFeatureMgrView3.htm).

Description

This method creates a new FeatureManager design tree view. This method
also provides a parameter for adding a tab, which the user can click to
activate your view.

Syntax (OLE Automation)

retval = ModelDoc.CreateFeatureMgrView2
( bitmap, toolTip)

(Table)=========================================================

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design
tree tab; the bitmap should be no larger than 16x18 this standard pointer
is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the Feature Manager view |

Syntax (COM)

status = ModelDoc->ICreateFeatureMgrView2
( bitmap, toolTip, &retval )

(Table)=========================================================

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design
tree tab; the bitmap should be no larger than 16x18 this standard pointer
is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the newly created FeatMgrView object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd
to get the new view handle. Because the view created is empty, you can
use the new view handle in combination with standard MFC calls to draw,
as desired, into the view.

The FeatureManager design tree view added to this document is not persistent.
The FeatureManager design tree view is not stored with this document and
must be recreated upon reloading the document.

This method will be automatically set up to receive FeatMgrView::ActivateNotify
and DeactivateNotify events. On the appropriate notification, you can
call ModelDoc2::DeleteFeatureMgrView to cleanup and delete your view.

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
<param name="Items" value="ModelDoc_Object$$**$$ZAccessorByCreate$$**$$ZCreateFeatMgrView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateFeatureMgrView2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
