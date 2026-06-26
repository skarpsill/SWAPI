---
title: "ModelDoc::ActivateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ActivateFeatureMgrView.htm"
---

# ModelDoc::ActivateFeatureMgrView

This
method is obsolete and has been superseded by[ModelDoc2::ActivateFeatureMgrView](../ModelDoc2/ModelDoc2__ActivateFeatureMgrView.htm).

Description

This method activates a given tab in the FeatureManager
design tree view.

Syntax (OLE Automation)

retval = ModelDoc.ActivateFeatureMgrView (appView)

(Table)=========================================================

| Input: | (long) appView | CView to activate in the FeatureManager design
tree view |
| --- | --- | --- |
| Return: | (long) retval | Pane in which the view was activated as defined
in swFeatMgrPane_e |

Syntax (COM)

status = ModelDoc->ActivateFeatureMgrView ( appView,
&retval )

(Table)=========================================================

| Input: | (long) appView | CView to activate in the FeatureManager design
tree view |
| --- | --- | --- |
| Output: | (long) retval | Pane in which the view was activated as defined
in swFeatMgrPane_e |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

The activated tab may be in a pane that is hidden.
The retval argument will indicate if which pane the tab is activated in
and if that pane is hidden.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__ActivateFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
