---
title: "ModelDoc::CreateFeatureMgrView3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateFeatureMgrView3.htm"
---

# ModelDoc::CreateFeatureMgrView3

This
method is obsolete and has been superseded by[ModelDoc2::CreateFeatureMgrView3](../ModelDoc2/ModelDoc2__CreateFeatureMgrView3.htm).

Description

This method creates a new FeatureManager design
tree view and provides a parameter for adding a tab, which the user can
click to activate your view.

Syntax (OLE Automation)

retval = ModelDoc.CreateFeatureMgrView3 (bitmap, toolTip, whichPane)

(Table)=========================================================

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design
tree tab; the bitmap should be no larger than 16x18; this standard pointer
is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | ToolTip string |
| Input: | (long) whichPane | Pane to add the view to as defined in swFeatMgrPane_e |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the new FeatMgrView object |

Syntax (COM)

status = ModelDoc->ICreateFeatureMgrView3 ( bitmap,
toolTip, whichPane, &retval )

(Table)=========================================================

| Input: | (long*) bitmap | Pointer to the bitmap you wish to use for the FeatureManager design
tree tab; the bitmap should be no larger than 16x18; this standard pointer
is created by performing a New on CBitmap |
| --- | --- | --- |
| Input: | (BSTR) toolTip | Tooltip string |
| Input: | (long) whichPane | Pane to add the view to as defined in swFeatMgrPane_e |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the new FeatMgrView object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method provides the ability to place your newly created FeatureManager
design tree view tab on either the top or bottom pane. The pane may or
may not be visible. However, the tab will be added to the specified pane.

Under certain conditions, for example while theSurface, Extendcommand is active
in the user interface, SolidWorks locks the bottom pane and does allow
the activation of any other tab. If your application needs the ability
to activate your new tab at all times, consider adding it either to the
top pane or to both panes. If you add it to the top pane only, it may
not be apparent to the user until the top pane is made visible.

If you receive a non-NULL return value, you can use FeatMgrView::GetFeatMgrViewWnd
to get the new view handle. Since the view created is empty, you may use
the new view handle in combination with standard MFC calls to draw, as
desired, into the view.

The FeatureManager design tree view added to this document is not persistant.
In other words, the FeatureManager design tree view is not stored with
this document and must be recreated upon reloading the document.

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateFeatureMgrView3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
