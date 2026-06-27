---
title: "ModelDoc2::ActivateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ActivateFeatureMgrView.htm"
---

# ModelDoc2::ActivateFeatureMgrView

This method is obsolete and has been superseded
by[FeatMgrView::ActivateView](sldworksAPI.chm::/FeatMgrView/FeatMgrView__ActivateView.htm).

Description

This method activates a tab in the FeatureManager
design tree view.

Syntax (OLE Automation)

retval = ModelDoc2.ActivateFeatureMgrView (appView)

(Table)=========================================================

| Input: | (long) appView | CView to activate in the FeatureManager design
tree view |
| --- | --- | --- |
| Return: | (long) retval | Pane in which the view is activated as defined
in swFeatMgrPane_e |

Syntax (COM)

status = ModelDoc2->ActivateFeatureMgrView ( appView,
&retval )

(Table)=========================================================

| Input: | (long) appView | CView to activate in the FeatureManager design
tree view |
| --- | --- | --- |
| Output: | (long) retval | Pane in which the view is activated as defined
in swFeatMgrPane_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The activated tab may be in a pane that is hidden.
The retval argument indicates the pane in which the tab is activated and
if that pane is hidden.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__ActivateFeatureMgrView.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__ActivateFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
