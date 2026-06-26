---
title: "ModelDoc2::CreateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateFeatureMgrView.htm"
---

# ModelDoc2::CreateFeatureMgrView

This
method is obsolete and has been superseded by[ModelDoc2::CreateFeatureMgrView2](ModelDoc2__CreateFeatureMgrView2.htm).

Description

This method creates a new FeatureManager design tree view. This method
also provides a parameter for adding a tab, which the user clicks to activate
your view.

Syntax (OLE Automation)

retval = ModelDoc2.CreateFeatureMgrView
( bitmap)

(Table)=========================================================

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design
tree tab; the bitmap should be no larger than 16x18; this standard pointer
is created by performing a New on CBitmap |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the FeatMgrView created |

Syntax (COM)

status = ModelDoc2->ICreateFeatureMgrView
( bitmap, &retval )

(Table)=========================================================

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design
tree tab; the bitmap should be no larger than 16x18; this standard pointer
is created by performing a New on CBitmap |
| --- | --- | --- |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the FeatMgrView created |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd
to get the new view handle. Because the view created is empty, you may
use the new view handle in combination with standard MFC calls to draw,
as desired, into the view.

The FeatureManager design tree view added to this document is not persistent.
In other words, the FeatureManager design tree view is not stored with
this document and must be recreated upon reloading the document.

This method will be automatically set up to receive FeatMgrView::ActivateNotify
and DeactivateNotify events. On the appropriate notification, you can
call ModelDoc2::DeleteFeatureMgrView to cleanup and delete your view.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__CreateFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__CreateFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
