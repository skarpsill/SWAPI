---
title: "ModelDoc::DeleteFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteFeatureMgrView.htm"
---

# ModelDoc::DeleteFeatureMgrView

This
method is obsolete and has been superseded by[ModelDoc2::DeleteFeatureMgrView](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DeleteFeatureMgrView.htm).

Description

This method removes a tab from the FeatureManager design tree view.
On the appropriate notification, you can call this method to clean up
and delete your FeatureManager design tree view.

Syntax (OLE Automation)

void ModelDoc.DeleteFeatureMgrView
( appView)

(Table)=========================================================

| Input: | (long*) appView | View handle of the FeatureManager design tree view that you wish to
delete |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->DeleteFeatureMgrView
( appView )

(Table)=========================================================

| Input: | (long*) appView | View handle of the FeatureManager design tree view that you wish to
delete |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method with ModelDoc::AddFeatureMgrView or ModelDoc::CreateFeatureMgrView.

If your Feature Manager design tree view was created using ModelDoc::CreateFeatureMgrView,
then calling this method destroys the CView object used for the FeatureManager
design tree view. If your FeatureManager design tree view was created
using ModelDoc::AddFeatureMgrView, then your application allocated the
Cview object and calling this method does not destroy the Cview object.
You are responsible for destroying the Cview object using the appropriate
destructor. Never use the delete operator directly on the view object.
Always use one of the appropriate MFC view destructors.

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
<param name="Items" value="ModelDoc_Object$$**$$ZDeleting$$**$$ZModifyFeatMgrView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__DeleteFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
